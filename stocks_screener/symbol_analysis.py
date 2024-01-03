from io import BytesIO
import mplfinance as mpf
import matplotlib

matplotlib.use('Agg')
import pandas as pd
import yfinance as yf
import datetime as dt
import pandas_ta as ta
from dateutil.relativedelta import relativedelta
from matplotlib.dates import DateFormatter
from ta.volatility import BollingerBands, AverageTrueRange
import matplotlib.pyplot as plt


# Downloading different intervals data from Yahoo based on preselected ticker
def individual_symbol_analysis(symbol):
    today = str(dt.date.today())
    twenty_months_ago = str(dt.date.today() - relativedelta(months=1))

    df_hourly = yf.download(symbol, interval="1h", start=twenty_months_ago, end=today)
    df_hourly.insert(0, 'Ticker', str(symbol))

    df_hourly['rsi'] = ta.rsi(df_hourly['Adj Close'], length=14)

    df_hourly.index = pd.to_datetime(df_hourly.index)

    print(df_hourly)

    fig = plt.subplots(1, sharex=True, figsize=(12, 8))

    # Plot candlestick chart on ax1
    mpf.plot(df_hourly, type='candle', volume=True,  mav=(5, 20, 50, 200))

    # Plot RSI on a separate subplot (ax2)
    fig_rsi, ax2 = plt.subplots(1, sharex=True, figsize=(8, 5))

    # Plot RSI on ax2
    ax2.plot(df_hourly.index, df_hourly['rsi'], label='RSI', color='purple')
    ax2.set_ylabel('RSI')


    img_buf_rsi = BytesIO()
    plt.savefig(img_buf_rsi, format='png')
    img_buf_rsi.seek(0)
    plt.close(fig_rsi)

    img_buf_candlestick = BytesIO()
    plt.savefig(img_buf_candlestick, format='png')
    img_buf_candlestick.seek(0)

    return img_buf_candlestick, img_buf_rsi

    # date_formatter = DateFormatter("%Y-%m-%d %H:%M:%S")
    # ax2.xaxis.set_major_formatter(date_formatter)

    # ax2.plot(df_hourly.index, df_hourly['rsi'], label='RSI', color='purple')
    # ax2.set_ylabel('RSI')
    # ax2.set_xlabel('Date')
