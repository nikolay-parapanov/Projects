import datetime as dt
import pandas as pd
import yfinance as yf
import ta


def retrieves_for_signals(tickers_signals):

    period_selected = "2y"
    interval_selected = "1d"

    combined_df_daily = pd.DataFrame()  # Initialize an empty DataFrame to store the final result

    for t in tickers_signals:
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

        df_current_ticker = df_current_ticker.tail(150)

        # Append the current ticker's data to the combined DataFrame
        combined_df_daily = pd.concat([combined_df_daily, df_current_ticker])

    # Drop "Dividends" and "Stock Splits" columns, ignoring if they don't exist
    combined_df_daily = combined_df_daily.drop(columns=["Dividends", "Stock Splits"], errors='ignore')


    print(f"Total rows in the combined DataFrame: {combined_df_daily.index.size}")

    today_date = dt.datetime.today().strftime('%Y-%m-%d')
    output_filename = f"step1_retrieve_period_60_1d.csv_{today_date}.csv"
    combined_df_daily.to_csv(output_filename, index=True)
    print(combined_df_daily)

    combined_df_signals=combined_df_daily

    return combined_df_signals

