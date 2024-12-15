import csv
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import os

from pandas import to_numeric


def filter_noa_calls_details():

    # Define file paths
    raw_file = 'noa/comprehensive_pivot.csv'
    result_table_noa_sorted_filtered_calls_all_tickers = 'noa/result_filtered_calls.csv'
    result_tickers_sorted_filtered_calls_all_tickers = 'individual_analysis_results/result_tickers_sorted_filtered_calls_all_tickers.csv'


    df = pd.read_csv(raw_file)
    print("Reading comprehensive pivot data. ..........................")
    print(df)

    # Function to clean data and convert to numeric
    def clean_and_convert(value):
        if isinstance(value, str):
            value = value.strip()  # Remove leading and trailing whitespace
            value = value.replace(',', '')  # Remove commas if any
        return pd.to_numeric(value, errors='coerce')

    # Remove rows with Expiration Dates not in the current year
    current_year = datetime.now().year
    df['Expiration Date'] = pd.to_datetime(df['Expiration Date'])
    df = df[df['Expiration Date'].dt.year == current_year]

    # Remove rows with Expiration Dates not in the current year or later than one month from now
    current_date = datetime.now()
    one_month_from_now = current_date + timedelta(days=30)

    # Convert 'Total Calls' and ratio columns to numeric
    df['Total Calls'] = df['Total Calls'].apply(clean_and_convert)
    df['Total Puts'] = df['Total Puts'].apply(clean_and_convert)

    # Identify ratio columns
    ratio_columns = [col for col in df.columns if '(Put/Call)' in col]

    latest_ratio_column = ratio_columns[-2]  # Use the latest ratio column
    df[latest_ratio_column] = df[latest_ratio_column].apply(clean_and_convert)

    df['Expiration Date'] = pd.to_datetime(df['Expiration Date'], format='%m-%d', errors='coerce')
    df['Expiration Date'] = df['Expiration Date'].apply(
        lambda x: x.replace(year=current_date.year) if pd.notna(x) else pd.NaT)

    final_df_sorted = df[
        (df['Expiration Date'].dt.year == current_date.year) &
        (df['Expiration Date'] <= one_month_from_now)
        ]

    print(("FINAL DF SORTED ++++++++++++++++++++++++++++++++++++++++"))
    print(final_df_sorted)

    final_df_sorted.to_csv('noa/result_filtered_calls.csv', index=False)

    # Convert 'Expiration Date' to '%m-%d' format
    df['Expiration Date'] = pd.to_datetime(df['Expiration Date'], format='%m-%d', errors='coerce')

    # Format the figures with a thousand separator
    def format_numbers(x):
        if isinstance(x, (int, float)):
            return '{:,}'.format(x)
        return x

    # Perform numeric comparisons on the raw DataFrame
    latest_ratio_column = ratio_columns[-2]  # Use the latest ratio column
    filtered_df_calls = final_df_sorted[
        (final_df_sorted['Total Calls'] > 30000) &
        (final_df_sorted[latest_ratio_column] < 0.3)
        ]
    # Format the numbers for output
    filtered_df_calls = filtered_df_calls.applymap(format_numbers)

    # Convert 'Expiration Date' to string in the '%m-%d' format
    filtered_df_calls['Expiration Date'] = filtered_df_calls['Expiration Date'].dt.strftime('%m-%d')

    print('DF before filter out of last call column with zeros')
    print(filtered_df_calls)

    # Identify the last column containing 'Call)'
    call_columns = [col for col in df.columns if "'Call')" in col]
    if not call_columns:
        print("No 'Call)' columns found.")
        return

    last_call_column = call_columns[-1]  # The last column containing 'Call)'

    filtered_df_calls[last_call_column] = filtered_df_calls[last_call_column].apply(clean_and_convert)

    print('ALL Call columns')
    print(call_columns)
    print('Last Call column')
    print(last_call_column[0])

    # Filter out rows with zero values in the last 'Call)' column
    filtered_df_calls = filtered_df_calls[filtered_df_calls[last_call_column] != 0]

    # Format the numbers for output
    filtered_df_calls = filtered_df_calls.applymap(format_numbers)

    print("FINAL COMPREHENSIVE DF CALLS SORTED and FILTERED: ++++++++++++++++++++++++++++++++++++++++++++++++")
    print(filtered_df_calls)

    print("LIST FOR INDIVIDUAL STOCK ANALYSIS: .................................")
    unique_tickers = filtered_df_calls['Stock Symbol'].unique()
    unique_tickers_list = unique_tickers.tolist()
    print(unique_tickers)
    print(len(unique_tickers))

    # Save the final filtered data and unique stock symbols to CSV files
    filtered_df_calls.to_csv(result_table_noa_sorted_filtered_calls_all_tickers, index=False)
    pd.Series(unique_tickers).to_csv(result_tickers_sorted_filtered_calls_all_tickers, index=False)

    return unique_tickers_list, filtered_df_calls