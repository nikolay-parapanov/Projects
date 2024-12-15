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
        # Return as is if there isf a parsing error
        return date_str

def generate_pivot():
    raw_file = 'combined/ovl_combined.csv'
    output_file1 = 'ovl/comprehensive_pivot.csv'

    print("Reading existing data...")
    df = pd.read_csv(raw_file)

    print("RAW DATA:")
    print(df)  # Print only the first few rows for better readability

    # Convert dates in 'Expiration Date' and 'Report Date' columns if they are in '%Y-%m-%d' format
    print("Converting dates in 'Expiration Date' and 'Report Date' columns...")
    df['Expiration Date'] = df['Expiration Date'].apply(lambda x: convert_date_format(str(x)))
    df['Report Date'] = df['Report Date'].apply(lambda x: convert_date_format(str(x)))

    # Ensure 'Report Date' is in datetime format
    df['Report Date'] = pd.to_datetime(df['Report Date'], format='%m/%d/%Y', errors='coerce')
    df['Expiration Date'] = pd.to_datetime(df['Expiration Date'], format='%m/%d/%Y', errors='coerce')

    print('DF with aligned dates: .................')
    print(df)

    # Extract unique reporting dates
    unique_report_dates = df['Report Date'].dropna().dt.date.unique()
    print(unique_report_dates)

    # Ensure 'Volume' is numeric and handle non-numeric gracefully
    df['Volume'] = pd.to_numeric(df['Volume'], errors='coerce')

    pivot_df = df.pivot_table(
        index=["Expiration Date","VOI Ratio","Stock Symbol","Strike Price","Stock Last Price"],  # Rows
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

    # Reset index to make 'Expiration Date' a column for sorting
    final_df_reset = pivot_df.reset_index()

    # Sort by 'Expiration Date' in ascending order and 'Total Call' in descending order
    final_df_sorted = final_df_reset.sort_values(by=['Expiration Date', 'VOI Ratio'], ascending=[True, False])
    final_sort_df = final_df_sorted[final_df_sorted["VOI Ratio"] > 3]

    # Format the figures with a thousand separator
    def format_numbers(x):
        if isinstance(x, (int, float)):
            return '{:,}'.format(x)
        return x

    print("FINAL COMPREHENSIVE ++++++++++++++++++++++++++++++++++++++++++++++++")
    print(final_sort_df)
    final_sort_df.to_csv(output_file1, index=False)


    return
