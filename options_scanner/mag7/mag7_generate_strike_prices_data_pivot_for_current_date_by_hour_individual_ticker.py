import csv

import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import os

from pandas import to_numeric

from individual_stock_analysis_code.yahoo_finance_data import get_tickers_prices


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

def extract_date_and_hour(time_str):
    try:
        # Extract date and hour parts
        date_str = time_str[:10]
        hour_str = time_str[10:13]  # Adjusted to extract the hour part only
        # Combine date and hour
        return f"{hour_str}:00"  # Set minutes to :00
    except Exception as e:
        print(f"Error processing time_str: {time_str}, error: {e}")
        return None

def mag7_generate_strike_prices_data_pivot_for_individual_ticker_current_date_by_hour(individual_ticker):
    ticker = individual_ticker.upper()
    raw_file = 'noa/notable_options_activity.csv'
    output_file1 = 'individual_analysis_results/mag7_strike_prices_for_all_tickers_current_date_by_hour.csv'
    print("Reading existing data...")
    df = pd.read_csv(raw_file)
    print("NOA current date:")
    print(df)  # Print only the first few rows for better readability

    unique_tickers_list = ['AAPL', 'TSLA', 'META', 'NVDA', 'GOOG', 'AMZN', 'MSFT']

    unique_tickers_current_prices_df = get_tickers_prices(unique_tickers_list)

    print('Unique tickers list: ........................')
    print(unique_tickers_list)

    # Filter df to include only the rows where 'Stock Symbol' is in unique_tickers_list
    df_filtered = df[df['Stock Symbol'].isin(unique_tickers_list)]

    print("Extracting and converting 'Reporting Date'...")
    df_filtered['Report Date'] = df_filtered['Time'].apply(extract_date_and_hour)

    print("EXTRACTED DATE AND TIME: /////////////////////////////////////////////")
    print(df_filtered)

    # Extract unique reporting dates and hours
    unique_report_dates_hours = df_filtered['Report Date'].dropna().unique()
    print("Unique Reporting Dates and Hours:")
    print(unique_report_dates_hours)

    # Ensure 'Volume' is numeric and handle non-numeric gracefully
    df_filtered['Volume'] = pd.to_numeric(df['Volume'], errors='coerce')

    pivot_df = df_filtered.pivot_table(
        index=["Expiration Date","Stock Symbol","Strike Price"],  # Rows
        columns=["Report Date","Type"],  # Columns
        values="Volume",
        aggfunc='sum',  # Aggregation function
        fill_value=0  # Replace NaN values with 0
    )

    print("Pivot table:")
    print(pivot_df)  # Print only the first few rows for better readability

    # Extract call and put columns
    call_columns = pivot_df.xs('Call', level='Type', axis=1)
    put_columns = pivot_df.xs('Put', level='Type', axis=1)

    # Calculate total Call and Put
    total_call = call_columns.sum(axis=1)
    total_put = put_columns.sum(axis=1)
    total_call_df = pd.DataFrame(total_call, columns=[f'Total Calls'])
    total_put_df = pd.DataFrame(total_put, columns=[f'Total Puts'])

    # Create a single empty column
    empty_column = pd.DataFrame(index=pivot_df.index, columns=['Separator'])

    # Concatenate the original pivot table, empty columns, ratio DataFrame, and total columns
    final_df = pd.concat([pivot_df, empty_column, total_call_df, total_put_df], axis=1)

    # Reset index to make 'Expiration Date' a column for sorting
    final_df_reset = final_df.reset_index()

    # Sort by 'Expiration Date' in ascending order and 'Total Call' in descending order
    final_df_sorted = final_df_reset.sort_values(by=['Expiration Date', 'Stock Symbol', 'Strike Price'], ascending=[True, True, True])

    def format_numbers(x):
        if isinstance(x, (int, float)):
            return '{:,}'.format(x)
        return x

    # Merge with the current prices DataFrame
    final_df_with_prices = final_df_sorted.merge(unique_tickers_current_prices_df, on='Stock Symbol', how='left')

    print("MERGED DF: .....")
    print(final_df_with_prices)

    # Check for 'Current Price' column
    if 'Current Price' not in final_df_with_prices.columns:
        print("Column 'Current Price' is missing from the merged DataFrame.")
        return

    # Calculate 'Diff' column
    final_df_with_prices['Diff'] = final_df_with_prices.apply(
        lambda row: row['Strike Price'] - row['Current Price'] if pd.notna(row['Current Price']) else np.nan,
        axis=1
    )

    # Calculate 'Diff' as a percentage of 'Strike Price'
    final_df_with_prices['Diff Percentage'] = final_df_with_prices.apply(
        lambda row: (row['Diff'] / row['Strike Price'] * 100) if pd.notna(row['Diff']) and row[
            'Strike Price'] != 0 else np.nan,
        axis=1
    )

    # Format columns
    final_df_with_prices['Current Price'] = final_df_with_prices['Current Price'].apply(
        lambda x: f'{x:.2f}' if pd.notna(x) else 'N/A'
    )
    final_df_with_prices['Diff'] = final_df_with_prices['Diff'].apply(
        lambda x: f'{x:.2f}' if pd.notna(x) else 'N/A'
    )
    final_df_with_prices['Diff Percentage'] = final_df_with_prices['Diff Percentage'].apply(
        lambda x: f'{x:.2f}%' if pd.notna(x) else 'N/A'
    )

    # Identify ratio columns
    ratio_columns = [col for col in final_df_with_prices.columns if '(Put/Call)' in col]
    # Format ratio columns with 2 decimal places
    final_df_with_prices[ratio_columns] = final_df_with_prices[ratio_columns].applymap(lambda x: f'{x:.2f}')

    # Apply the formatting function to all numeric columns
    final_df_with_prices = final_df_with_prices.applymap(format_numbers)

    final_df_with_prices = final_df_with_prices[final_df_with_prices['Stock Symbol'] == ticker]

    print("FINAL COMPREHENSIVE ++++++++++++++++++++++++++++++++++++++++++++++++")
    print(final_df_with_prices)
    final_df_with_prices.to_csv(output_file1, index=False)

    return final_df_with_prices
