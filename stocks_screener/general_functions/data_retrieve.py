import pandas as pd
import yfinance as yf
import datetime as dt


# Downloading daily data from Yahoo based on predefined tickers list (in database/tickers/ folder)
def data_collection_daily(ticker_list, saving_file_path):

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

        # # Drop unnecessary columns ("Adj. Close")
        all_symbols_df_dropped = all_symbols_df.drop(all_symbols_df.columns[[5]], axis=1)

        all_symbols_df_dropped.to_csv(saving_file_path)
        return all_symbols_df_dropped
