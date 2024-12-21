import datetime as dt
import os

import pandas as pd
import yfinance as yf
import ta


def data_retrieval_daily():

    csv_file_path = r'C:\Users\npara\coding\np-github\Projects\options_scanner\rsi_divergence_files\tickers_list_options_favourites.csv'  # Replace with the path to your CSV file
    df = pd.read_csv(csv_file_path)
    tickers_list_options_favourites = df['Ticker'].tolist()

    csv_file_path = r'C:\Users\npara\coding\np-github\Projects\options_scanner\rsi_divergence_files\tickers_list_finviz_beta.csv'  # Replace with the path to your CSV file
    df = pd.read_csv(csv_file_path)
    tickers_list_beta = df['Ticker'].tolist()

    combined_tickers = list(set(tickers_list_options_favourites + tickers_list_beta))

    print("Combined Tickers List:")
    print(combined_tickers)
    print(f"Total unique tickers: {len(combined_tickers)}")

    cut_last = 1
    period_selected = "2y"
    interval_selected = "1d"

    combined_df_daily = pd.DataFrame()  # Initialize an empty DataFrame to store the final result

    for t in combined_tickers:
        print(t)
        current_ticker = yf.Ticker(t)
        df_current_ticker = current_ticker.history(period=period_selected, interval=interval_selected)

        # Skip tickers with no data returned
        if df_current_ticker.empty:
            print(f"No data for {t}")
            continue

        # Add Ticker and Interval columns once, not inside the loop
        df_current_ticker.insert(0, 'Ticker', t)
        df_current_ticker.insert(0, 'Interval', interval_selected)

        # Calculate Technical Indicators
        df_current_ticker['Avg_Volume_14_daily'] = df_current_ticker['Volume'].rolling(window=14).mean()
        df_current_ticker['RSI_daily'] = ta.momentum.rsi(df_current_ticker['Close'], window=14)
        df_current_ticker['SMA_20_daily'] = ta.trend.sma_indicator(df_current_ticker['Close'], window=20)
        df_current_ticker['SMA_50_daily'] = ta.trend.sma_indicator(df_current_ticker['Close'], window=50)
        df_current_ticker['SMA_200_daily'] = ta.trend.sma_indicator(df_current_ticker['Close'], window=200)
        df_current_ticker['ATR_daily'] = ta.volatility.average_true_range(df_current_ticker['High'],
                                                                          df_current_ticker['Low'],
                                                                          df_current_ticker['Close'], window=14)
        df_current_ticker['SMA20 vs SMA50_daily'] = df_current_ticker.apply(
            lambda row: "Long" if row['SMA_20_daily'] > row['SMA_50_daily'] else "Short", axis=1)
        df_current_ticker['SMA50 vs SMA200_daily'] = df_current_ticker.apply(
            lambda row: "Long" if row['SMA_50_daily'] > row['SMA_200_daily'] else "Short", axis=1)

        # Only keep the last 20 rows of data
        df_current_ticker = df_current_ticker.tail(cut_last)

        # Append the current ticker's data to the combined DataFrame
        combined_df_daily = pd.concat([combined_df_daily, df_current_ticker])

    print(combined_df_daily)

    # Drop "Dividends" and "Stock Splits" columns, ignoring if they don't exist
    combined_df_daily = combined_df_daily.drop(columns=["Dividends", "Stock Splits"], errors='ignore')


    print(f"Total rows in the combined DataFrame: {combined_df_daily.index.size}")

    folder_path_single_use = r'C:\Users\npara\coding\np-github\Projects\options_scanner\rsi_divergence_files'
    output_filename = f"step0_retrieve_daily.csv"

    full_path_single_use = os.path.join(folder_path_single_use, output_filename)
    combined_df_daily.to_csv(full_path_single_use, index=True)

    print(combined_df_daily)
    return

