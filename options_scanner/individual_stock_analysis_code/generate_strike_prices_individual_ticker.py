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

def generate_strike_prices_data_pivot_for_individual_ticker(ticker):
    ticker = ticker.upper()
    raw_file = 'individual_analysis_results/strike_prices_for_all_tickers.csv'
    output_file1 = 'individual_analysis_results/strike_prices_for_individual_ticker.csv'

    unique_tickers_file = 'individual_analysis_results/result_tickers_sorted_filtered_calls_all_tickers.csv'

    # Read unique tickers from the unique_tickers_file
    unique_tickers_df = pd.read_csv(unique_tickers_file, header=None)

    # Convert the first (and only) column to a list skipping first value as it is zero (probably index from previous iterations)
    unique_tickers_list = unique_tickers_df.iloc[:, 0].tolist()

    print("Reading existing Strike Price data for all tickers ...")
    df = pd.read_csv(raw_file)
    print(df)

    def format_numbers(x):
        if isinstance(x, (int, float)):
            return '{:,}'.format(x)
        return x

    print('Only ticker to remain in the table: ....................')
    print(ticker)

    df = df[df['Stock Symbol'] == ticker]

    # unique_tickers_current_prices_df = get_tickers_prices(unique_tickers_list)
    #
    # # Merge with the current prices DataFrame
    # final_df_with_prices = df.merge(unique_tickers_current_prices_df, on='Stock Symbol', how='left')

    print("MERGED DF: .....")
    print(df)

    # # Check for 'Current Price' column
    # if 'Current Price' not in final_df_with_prices.columns:
    #     print("Column 'Current Price' is missing from the merged DataFrame.")
    #     return
    #
    # # Calculate 'Diff' column
    # final_df_with_prices['Diff'] = final_df_with_prices.apply(
    #     lambda row: row['Strike Price'] - row['Current Price'] if pd.notna(row['Current Price']) else np.nan,
    #     axis=1
    # )
    #
    # # Calculate 'Diff' as a percentage of 'Strike Price'
    # final_df_with_prices['Diff Percentage'] = final_df_with_prices.apply(
    #     lambda row: (row['Diff'] / row['Strike Price'] * 100) if pd.notna(row['Diff']) and row[
    #         'Strike Price'] != 0 else np.nan,
    #     axis=1
    # )
    #
    # # Format columns
    # final_df_with_prices['Current Price'] = final_df_with_prices['Current Price'].apply(
    #     lambda x: f'{x:.2f}' if pd.notna(x) else 'N/A'
    # )
    # final_df_with_prices['Diff'] = final_df_with_prices['Diff'].apply(
    #     lambda x: f'{x:.2f}' if pd.notna(x) else 'N/A'
    # )
    # final_df_with_prices['Diff Percentage'] = final_df_with_prices['Diff Percentage'].apply(
    #     lambda x: f'{x:.2f}%' if pd.notna(x) else 'N/A'
    # )

    # Apply the formatting function to all numeric columns
    df = df.applymap(format_numbers)

    print("FINAL for individual ticker ++++++++++++++++++++++++++++++++++++++++++++++++")
    print(df)
    df.to_csv(output_file1, index=False)

    return df
