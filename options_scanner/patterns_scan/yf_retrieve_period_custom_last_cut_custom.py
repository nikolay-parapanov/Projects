import datetime as dt
import os.path

import pandas as pd
import yfinance as yf
import ta

import warnings
warnings.filterwarnings('ignore', category=FutureWarning)

def data_retrieval_period_custom_last_cut_custom(period, interval, cut_last, tickers_list_option, output_file):
    tickers_list_requested = tickers_list_option
    period_selected = period
    interval_selected = interval
    cut_last = cut_last
    output_file = output_file
    # tickers_list_requested = tickers_list_requested_atr3

    # cut_last_60 = 60
    # cut_last_120 = 120
    #
    # cut_last = cut_last_60
    # # cut_last = cut_last_120
    # period_selected = "2y"
    # interval_selected = "1d"

    combined_df_daily = pd.DataFrame()  # Initialize an empty DataFrame to store the final result

    for t in tickers_list_requested:
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
        df_current_ticker['Avg_Volume_10'] = df_current_ticker['Volume'].rolling(window=10).mean()
        df_current_ticker['RSI'] = ta.momentum.rsi(df_current_ticker['Close'], window=14)

        if len(df_current_ticker) >= 14:
            df_current_ticker['ATR'] = ta.volatility.average_true_range(df_current_ticker['High'], df_current_ticker['Low'], df_current_ticker['Close'],window=14)
        else:
            print("Not enough data to calculate ATR. The DataFrame needs at least 14 rows.")

        df_current_ticker['vol_vs_avrg_vol'] = df_current_ticker['Volume'] / df_current_ticker['Avg_Volume_10']

        df_current_ticker['SMA_20'] = ta.trend.sma_indicator(df_current_ticker['Close'], window=20)
        df_current_ticker['SMA_50'] = ta.trend.sma_indicator(df_current_ticker['Close'], window=50)
        df_current_ticker['SMA_200'] = ta.trend.sma_indicator(df_current_ticker['Close'], window=200)
        df_current_ticker['SMA_65'] = ta.trend.sma_indicator(df_current_ticker['Close'], window=65)


        # Only keep the last 20 rows of data
        df_current_ticker = df_current_ticker.tail(cut_last)

        # Append the current ticker's data to the combined DataFrame
        combined_df_daily = pd.concat([combined_df_daily, df_current_ticker])

    # Drop "Dividends" and "Stock Splits" columns, ignoring if they don't exist
    combined_df_daily = combined_df_daily.drop(columns=["Dividends", "Stock Splits"], errors='ignore')

    # Add a descending number column for each ticker group
    combined_df_daily['desc_number'] = combined_df_daily.groupby('Ticker').cumcount(ascending=False) + 1

    print(f"Total rows in the combined DataFrame: {combined_df_daily.index.size}")

    # Sort tickers (optional, but included as in the original code)
    tickers_list_requested.sort()

    today_date = dt.datetime.today().strftime('%Y-%m-%d')

    output_filename = f"step1_retrieve_-_perdiod_{period}-_interval_{interval}-_cut_last_{cut_last}-_tickers_list-date_{today_date}.csv"
    combined_df_daily.to_csv(output_filename, index=True)

    folder_path_single_use = r'C:\Users\npara\coding\np-github\Projects\options_scanner\rsi_divergence_files'
    full_path_single_use = os.path.join(folder_path_single_use, output_file)
    combined_df_daily.to_csv(full_path_single_use, index=True)
    print(combined_df_daily)

    return combined_df_daily

