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


def calculate_support_and_resistance():
    return


def support(df, l, n1, n2):
    for i in range(l - n1 + 1, l + 1):
        if (df.Low[i] > df.Low[i - 1]):
            return 0
    for i in range(l + 1, l + n2 + 1):
        if (df.Low[i] < df.Low[i - 1]):
            return 0
    return 1


def resistance(df, l, n1, n2):
    for i in range(l - n1 + 1, l + 1):
        if (df.High[i] < df.High[i - 1]):
            return 0
    for i in range(l + 1, l + n2 + 1):
        if (df.High[i] > df.High[i + 1]):
            return 0
    return 1


def create_candlestick_and_RSI_chart(df_hourly, ticker, start_date, today, figsize):

    df_hourly['EMA20'] = ta.ema(df_hourly.Close, 20)
    df_hourly['EMA50'] = ta.ema(df_hourly.Close, 50)

    df_hourly['RSI'] = ta.rsi(df_hourly.Close, length=14)
    df_hourly['RSI_oversold_line'] = 30
    df_hourly['RSI_overbought_line'] = 70

    EMA_RSI = [
        mpf.make_addplot(df_hourly.RSI, type='line', color='b', panel=1,width=0.6),
        mpf.make_addplot(df_hourly['RSI_oversold_line'], type='line', color='g', panel=1,width=0.7), 
        mpf.make_addplot(df_hourly['RSI_overbought_line'], type='line', color='r', panel=1,width=0.6),
        mpf.make_addplot(df_hourly.EMA20, type='line', color='y', panel=0,width=0.3),
        mpf.make_addplot(df_hourly.EMA50, type='line', color='g', panel=0, width=0.6)]

    sr = []
    n1, n2 = 2, 2

    for row in range(n1, len(df_hourly) - n2):
        if support(df_hourly, row, n1, n2):
            sr.append((row, df_hourly.Low[row], 1))
        if resistance(df_hourly, row, n1, n2):
            sr.append((row, df_hourly.High[row], 2))
    print(sr)

    plotlist_support = [x[1] for x in sr if x[2] == 1]
    plotlist_resistance = [x[1] for x in sr if x[2] == 2]
    plotlist_support.sort()
    plotlist_resistance.sort()

    for i in range(5, len(plotlist_support)-1):
        if (i > len(plotlist_support)-1):
            break
        diff_abs = (plotlist_support[i] - plotlist_support[i - 1])
        avrg = (plotlist_support[i] + plotlist_support[i - 1]) / 2
        if ((diff_abs / avrg) <= 0.03):
            plotlist_support.pop(i)

    for i in range(5, len(plotlist_resistance)-1):
        if (i > len(plotlist_resistance))-1:
            break
        diff_abs = (plotlist_resistance[i] - plotlist_resistance[i - 1])
        avrg = (plotlist_resistance[i] + plotlist_resistance[i - 1]) / 2
        if ((diff_abs / avrg) <= 0.05):
            plotlist_resistance.pop(i)

    print('plotlist resistance:\n')
    print(plotlist_resistance)
    print('plotlist support:\n')
    print(plotlist_support)

    # fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(20, 25))

    hlines_arranged_for_visualization = []
    colors_arranged_for_visualization = []
    for item in plotlist_support:
        hlines_arranged_for_visualization.append(item)
        colors_arranged_for_visualization.append('g')
    for item in plotlist_resistance:
        hlines_arranged_for_visualization.append(item)
        colors_arranged_for_visualization.append('r')

    mpf.plot(df_hourly,
             type='candle',
             style='yahoo',
             hlines=
                dict(hlines=hlines_arranged_for_visualization,
                     colors=colors_arranged_for_visualization,
                     linestyle='-',
                     linewidths=0.6),
             volume=True,
             addplot=EMA_RSI,
             figsize=(12.8,10))

    plt.tight_layout()
    img_buf = BytesIO()
    plt.savefig(img_buf, format='png')
    # plt.close(fig)

    img_buf.seek(0)

    return img_buf
