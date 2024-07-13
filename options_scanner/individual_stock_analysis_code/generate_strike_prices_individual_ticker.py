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

def generate_strike_prices_data_pivot_for_individual_ticker(ticker):
    ticker = ticker.upper()
    raw_file = 'individual_analysis_results/strike_prices_for_all_tickers.csv'
    output_file1 = 'individual_analysis_results/strike_prices_for_individual_ticker.csv'

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

    # Apply the formatting function to all numeric columns
    final_df_filtered = df.applymap(format_numbers)

    print("FINAL for individual ticker ++++++++++++++++++++++++++++++++++++++++++++++++")
    print(final_df_filtered)
    final_df_filtered.to_csv(output_file1, index=False)

    return df, ticker
