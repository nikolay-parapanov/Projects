import datetime as dt
import pandas as pd
import yfinance as yf
from pandas_datareader import data as pdr

if __name__ == '__main__':

    tickers_list_requested = ['AAPL', 'MSFT', 'TSLA', 'GOOG']

    period_selected = "3mo"
    interval_selected = "60m"

    combined_df = pd.DataFrame()

    for t in tickers_list_requested:
        current_ticker = yf.Ticker(t)
        print(current_ticker)

        df_current_ticker = current_ticker.history(period=period_selected, interval=interval_selected)

        new_ticker_column = []
        for i in range(df_current_ticker.index.size):
            new_ticker_column.append(t)

        df_current_ticker.insert(0, 'Ticker', new_ticker_column)
        # print(df_current_ticker)
        # print(df_current_ticker.index.size)

        combined_df = pd.concat([combined_df, df_current_ticker])

    print(combined_df)
    print(combined_df.index.size)

    tickers_list_requested.sort()

    name = '';
    for t in tickers_list_requested:
        name += str(t) + '-'

    csv_file_name = str(f'{dt.datetime.now()} + {name}')
    print(csv_file_name)
    # combined_df.insert(0,'Datetime2', '')
    # for row in combined_df:
    print(combined_df[['Datetime']].to_string(index=False))
        # row['Datetime2'] = row['Datetime']
    combined_df.to_csv('proba1.csv', index=False, date_format='%Y%M%S')

    print('the end :)')
