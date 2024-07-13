import csv
import pandas as pd
from datetime import datetime, timedelta
import os

from pandas import to_numeric
def convert_date_format(date_str):
    try:
        # Check if the date_str contains '-' and is in '%Y-%m-%d' format
        if '-' in date_str:
            # Parse the date in '%Y-%m-%d' format
            date_obj = datetime.strptime(date_str, '%Y-%m-%d')
            # Convert it to '%m/%d/%Y' format
            return date_obj.strftime('%m/%d/%Y')
        else:
            # Return as is if it doesn't match the expected format
            return date_str
    except ValueError:
        # Return as is if there is a parsing error
        return date_str

def generate_pivot():
    raw_file = 'combined/noa_combined.csv'
    output_file1 = 'noa/comprehensive_pivot.csv'

    print("Reading existing data...")
    df = pd.read_csv(raw_file)


    print("RAW DATA:")
    print(df)  # Print only the first few rows for better readability

    print("Before REP date")
    print(type(df.iloc[-1, 0]))
    print(df.iloc[-1, 0])

    print("Before EXP date")
    print(type(df.iloc[-1, 8]))
    print(df.iloc[-1, 8])

    # Convert dates in 'Expiration Date' and 'Report Date' columns if they are in '%Y-%m-%d' format
    print("Converting dates in 'Expiration Date' and 'Report Date' columns...")
    df['Expiration Date'] = df['Expiration Date'].apply(lambda x: convert_date_format(str(x)))
    df['Report Date'] = df['Report Date'].apply(lambda x: convert_date_format(str(x)))

    # Ensure 'Report Date' is in datetime format
    df['Report Date'] = pd.to_datetime(df['Report Date'], format='%m/%d/%Y', errors='coerce')
    df['Expiration Date'] = pd.to_datetime(df['Expiration Date'], format='%m/%d/%Y', errors='coerce')

    print('DF with aligned dates: .................')

    print(df)
    print("After REP date")
    print("After REP date")
    print(type(df.iloc[0, 0]))
    print(df.iloc[0, 0])
    print(type(df.iloc[-1, 0]))
    print(df.iloc[-1, 0])

    print("After EXP date")
    print(type(df.iloc[0, 8]))
    print(df.iloc[0, 8])
    print(type(df.iloc[-1, 8]))
    print(df.iloc[-1, 8])

    # Extract unique reporting dates
    unique_report_dates = df['Report Date'].dropna().dt.date.unique()
    print(unique_report_dates)

    # Ensure 'Volume' is numeric and handle non-numeric gracefully
    df['Volume'] = pd.to_numeric(df['Volume'], errors='coerce')

    pivot_df = df.pivot_table(
        index=["Expiration Date","Stock Symbol"],  # Rows
        columns=["Report Date","Type"],  # Columns
        values="Volume",
        aggfunc='sum',  # Aggregation function
        fill_value=0  # Replace NaN values with 0
    )

    # Ensure column headers are strings formatted as 'YYYY-MM-DD'
    pivot_df.columns = pivot_df.columns.set_levels([col.strftime('%Y-%m-%d') for col in pivot_df.columns.levels[0]],
                                                   level=0)
    print("Pivot table:")
    print(pivot_df)  # Print only the first few rows for better readability

    # Extract call and put columns
    call_columns = pivot_df.xs('Call', level='Type', axis=1)
    put_columns = pivot_df.xs('Put', level='Type', axis=1)

    # Get the last 2 Report Dates
    report_dates = sorted(call_columns.columns.get_level_values(0).unique(), reverse=True)
    last_2_dates = report_dates[:2]

    # Calculate Put/Call ratio
    call_columns_last_2 = call_columns[last_2_dates]
    put_columns_last_2 = put_columns[last_2_dates]
    ratio_df_last_2 = put_columns_last_2 / call_columns_last_2
    ratio_df_last_2.replace([float('inf'), -float('inf')], pd.NA, inplace=True)
    ratio_df_last_2.fillna(0, inplace=True)

    # Rename columns for the ratio DataFrame
    ratio_df_last_2.columns = [f'{col} (Put/Call)' for col in ratio_df_last_2.columns]

    # Calculate total Call and Put
    total_call = call_columns.sum(axis=1)
    total_put = put_columns.sum(axis=1)
    total_call_df = pd.DataFrame(total_call, columns=[f'Total Calls'])
    total_put_df = pd.DataFrame(total_put, columns=[f'Total Puts'])

    # Create a single empty column
    empty_column = pd.DataFrame(index=pivot_df.index, columns=['Separator'])

    # Concatenate the original pivot table, empty columns, ratio DataFrame, and total columns
    final_df = pd.concat([pivot_df, empty_column, ratio_df_last_2, total_call_df, total_put_df], axis=1)

    # Reset index to make 'Expiration Date' a column for sorting
    final_df_reset = final_df.reset_index()

    # Sort by 'Expiration Date' in ascending order and 'Total Call' in descending order
    final_df_sorted = final_df_reset.sort_values(by=['Expiration Date', 'Total Calls'], ascending=[True, False])

    # Format the figures with a thousand separator
    def format_numbers(x):
        if isinstance(x, (int, float)):
            return '{:,}'.format(x)
        return x

    # Identify ratio columns
    ratio_columns = [col for col in final_df_sorted.columns if '(Put/Call)' in col]
    # Format ratio columns with 2 decimal places
    final_df_sorted[ratio_columns] = final_df_sorted[ratio_columns].applymap(lambda x: f'{x:.2f}')

    # Apply the formatting function to all numeric columns
    final_df_sorted = final_df_sorted.applymap(format_numbers)


    print("FINAL COMPREHENSIVE ++++++++++++++++++++++++++++++++++++++++++++++++")
    print(final_df_sorted)
    final_df_sorted.to_csv(output_file1, index=False)


    return
