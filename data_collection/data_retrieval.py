import datetime as dt
import pandas as pd
import yfinance as yf


def data_retrieval_daily(list_of_tickers):
    tickers_list_requested = list_of_tickers

    period_selected = "5y"
    interval_selected = "1d"

    combined_df = pd.DataFrame()

    for t in tickers_list_requested:
        current_ticker = yf.Ticker(t)
        df_current_ticker = current_ticker.history(period=period_selected, interval=interval_selected)

        new_ticker_column = []
        interval_column = []
        for i in range(df_current_ticker.index.size):
            new_ticker_column.append(t)
            interval_column.append(interval_selected)

        df_current_ticker.insert(0, 'Ticker', new_ticker_column)
        df_current_ticker.insert(0, 'Interval', interval_column)

        combined_df = pd.concat([combined_df, df_current_ticker])

    print(combined_df.index.size)

    tickers_list_requested.sort()

    combined_df.to_csv('step1-1d-retrieved_data.csv', index=True)
    print(combined_df)

    return combined_df


# name = '';
# for t in tickers_list_requested:
#     name += str(t) + '-'

# csv_file_name = str(f'{str(dt.datetime.now())} + {name}')
# print(csv_file_name)
