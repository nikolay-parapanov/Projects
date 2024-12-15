import datetime as dt
import pandas as pd
import yfinance as yf
import ta


def data_retrieval_4h(list_of_tickers):
    tickers_list_requested = list_of_tickers

    period_selected = "1y"
    interval_selected = "1h"

    combined_df_1h = pd.DataFrame()  # Initialize an empty DataFrame to store the final result

    for t in tickers_list_requested:
        print(t)
        # current_ticker = yf.Ticker(t)
        df_current_ticker = yf.download(tickers=t, period=period_selected, interval=interval_selected)

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
        df_current_ticker['SMA_20'] = ta.trend.sma_indicator(df_current_ticker['Close'], window=20)
        df_current_ticker['SMA_50'] = ta.trend.sma_indicator(df_current_ticker['Close'], window=50)
        df_current_ticker['SMA_200'] = ta.trend.sma_indicator(df_current_ticker['Close'], window=200)

        # Only keep the last 20 rows of data
        df_current_ticker = df_current_ticker.tail(60)

        # Append the current ticker's data to the combined DataFrame
        combined_df_1h = pd.concat([combined_df_1h, df_current_ticker])

    # Drop "Dividends" and "Stock Splits" columns, ignoring if they don't exist
    combined_df_1h = combined_df_1h.drop(columns=["Dividends", "Stock Splits"], errors='ignore')


    print(f"Total rows in the combined DataFrame: {combined_df_1h.index.size}")

    # Sort tickers (optional, but included as in the original code)
    tickers_list_requested.sort()

    # Save the result to CSV
    combined_df_1h.to_csv('step1.4-1h-retrieved_data.csv', index=True)
    print(combined_df_1h)

    # combined_df_4h = combined_df_1h.resample('4H').agg({
    #     'Open': 'first',
    #     'High': 'max',
    #     'Low': 'min',
    #     'Close': 'last',
    #     'Volume': 'sum'
    # })
    #
    # combined_df_4h.to_csv('step1.2-4h-retrieved_data.csv', index=True)
    # combined_df_2h = combined_df_1h.resample('2H').agg({
    #     'Open': 'first',
    #     'High': 'max',
    #     'Low': 'min',
    #     'Close': 'last',
    #     'Volume': 'sum'
    # })
    #
    # combined_df_2h.to_csv('step1.3-2h-retrieved_data.csv', index=True)

    return combined_df_1h

