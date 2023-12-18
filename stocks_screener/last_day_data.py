import pandas as pd
import datetime as dt


def last_day_data():
    df = pd.read_csv('database/daily/all_symbols_daily_enriched_19.csv')

    print('Currently the model gets only last day data, but will be reworked for more options')
    how_many_days = 1

    unique_tickers = df["Ticker"].unique()
    print(unique_tickers)

    last_days_data_for_each_ticker = pd.DataFrame()

    subdf = pd.DataFrame()
    for ticker in unique_tickers:
        subdf = df.loc[df.Ticker == ticker]
        last_rows = subdf.tail(how_many_days)

        last_days_data_for_each_ticker = pd.concat([last_days_data_for_each_ticker, last_rows])

    print(last_days_data_for_each_ticker)

    return 'data from last day filtered'
