import datetime as dt
import pandas as pd
import yfinance as yf
import ta


def data_retrieval_daily(list_of_tickers):
    tickers_list_requested = list_of_tickers

    period_selected = "2y"
    interval_selected = "1d"

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
        df_current_ticker['SMA_20'] = ta.trend.sma_indicator(df_current_ticker['Close'], window=20)
        df_current_ticker['SMA_50'] = ta.trend.sma_indicator(df_current_ticker['Close'], window=50)
        df_current_ticker['SMA_200'] = ta.trend.sma_indicator(df_current_ticker['Close'], window=200)

        # Only keep the last 20 rows of data
        df_current_ticker = df_current_ticker.tail(60)

        # Append the current ticker's data to the combined DataFrame
        combined_df_daily = pd.concat([combined_df_daily, df_current_ticker])

    # Drop "Dividends" and "Stock Splits" columns, ignoring if they don't exist
    combined_df_daily = combined_df_daily.drop(columns=["Dividends", "Stock Splits"], errors='ignore')


    print(f"Total rows in the combined DataFrame: {combined_df_daily.index.size}")

    # Sort tickers (optional, but included as in the original code)
    tickers_list_requested.sort()

    # Save the result to CSV
    combined_df_daily.to_csv('step1-1d-retrieved_data.csv', index=True)
    print(combined_df_daily)

    return combined_df_daily

