import pandas as pd
import yfinance as yf
import datetime as dt


# Downloading daily data from Yahoo based on predefined tickers list (in database/tickers/ folder)
def data_collection_daily(ticker_list):

    today = str(dt.date.today())
    with open(ticker_list) as f:
        companies = f.read().splitlines()
        all_symbols_df = pd.DataFrame()
        for company in companies:
            symbol = company.split(',')[0]
            current_symbol_df = yf.download(symbol, start='2023-01-01', end=today)
            current_symbol_df.insert(0, 'Ticker' , str(symbol))
            all_symbols_df = pd.concat([all_symbols_df, current_symbol_df])

        # print(all_symbols_df)
        data_collected_df = all_symbols_df
        all_symbols_df.to_csv('database/daily/rsi/step_1_-_all_symbols_daily_initial_finviz_2200.csv')
        return data_collected_df
