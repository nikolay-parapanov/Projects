import pandas as pd
import yfinance as yf
import datetime as dt

from dateutil.relativedelta import relativedelta
from ta.volatility import BollingerBands, AverageTrueRange


# Downloading different intervals data from Yahoo based on preselected ticker
def individual_symbol_analysis(symbol):
    today = str(dt.date.today())
    twenty_months_ago = str(dt.date.today() - relativedelta(months=20))
    print(today)
    print(twenty_months_ago)

    current_symbol_hourly_df = yf.download(symbol, interval="1h", start=twenty_months_ago, end=today)
    current_symbol_hourly_df.insert(0, 'Ticker', str(symbol))

    print(current_symbol_hourly_df)

    bb_indicator = BollingerBands()

    return
