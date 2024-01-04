from io import BytesIO
import mplfinance as mpf
import matplotlib

matplotlib.use('Agg')
import pandas as pd
import yfinance as yf
import datetime as dt
import pandas_ta as ta
from dateutil.relativedelta import relativedelta
import matplotlib.pyplot as plt


# Downloading different intervals data from Yahoo based on preselected ticker
def individual_symbol_analysis(ticker):
    today = str(dt.date.today())
    start_date = str(dt.date.today() - relativedelta(months=2))

    df_hourly = yf.download(ticker, interval="1h", start=start_date, end=today)
    df_hourly.insert(0, 'Ticker', str(ticker))
    figsize = (12, 5)

    df_hourly.index = pd.to_datetime(df_hourly.index)

    print(df_hourly)

    img_buf_candlestick_EMA20_EMA50 = create_candlestick_and_RSI_chart(df_hourly, ticker, start_date, today,
                                                                       figsize)

    return img_buf_candlestick_EMA20_EMA50


def create_candlestick_and_RSI_chart(df_hourly, ticker, start_date, today, figsize):
    df_hourly['EMA20'] = ta.ema(df_hourly.Close, 20)
    df_hourly['EMA50'] = ta.ema(df_hourly.Close, 50)

    # EMA = [mpf.make_addplot(df_hourly.EMA20, type='line', color='y', width=0.3),
    #        mpf.make_addplot(df_hourly.EMA50, type='line', color='g', width=0.6)]
    df_hourly['RSI'] = ta.rsi(df_hourly.Close, length=14)

    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(20, 25))

    mpf.plot(df_hourly, ax=ax1, type='candle', style='yahoo')

    ax2.plot(df_hourly.index, df_hourly['RSI'], scalex=True, color='b')
    ax2.axhline(y=30, color='g', linestyle='--', label='RSI 30 Level')  # Add RSI 30 level line
    ax2.axhline(y=70, color='r', linestyle='--', label='RSI 70 Level')  # Add RSI 30 level line
    ax2.set_title('RSI Chart')
    ax2.set_xlabel('Date')
    ax2.set_ylabel('RSI')
    ax2.legend()

    ax3.plot(df_hourly.index, df_hourly['Volume'], color='r')
    ax3.set_title('Volume Chart')
    ax3.set_xlabel('Date')
    ax3.set_ylabel('Volume')
    ax3.legend()

    plt.tight_layout()
    img_buf = BytesIO()
    plt.savefig(img_buf, format='png')
    plt.close(fig)

    img_buf.seek(0)

    return img_buf
