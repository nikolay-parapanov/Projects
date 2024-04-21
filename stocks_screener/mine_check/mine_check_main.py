import pandas as pd
import pandas_ta as ta

from general_functions import data_retrieve

def yahoo_download():

    df = data_retrieve.data_collection_daily('../database/tickers_list/finviz_1500_test5.csv', '../database/mine/step_1_-_finviz_1500_mine_yahoo_daily.csv')
    print(df)

    return df

# yahoo_download()

df = pd.read_csv('../database/mine/step_1_-_finviz_1500_mine_yahoo_daily.csv')
# Calculate RSI
df = df.assign(RSI='')
unique_tickers = df["Ticker"].unique()
print(len(unique_tickers))

for ticker in unique_tickers:
    subdf = df.loc[df.Ticker == ticker]
    rsi_values = ta.rsi(subdf.Close, length=14)
    df.loc[df.Ticker == ticker, 'RSI'] = rsi_values

    # Compute SMA and high/low for the current ticker
    df.loc[df.Ticker == ticker, 'SMA_7'] = subdf['Close'].rolling(window=7).mean().round(2)
    df.loc[df.Ticker == ticker, 'SMA_10'] = subdf['Close'].rolling(window=10).mean().round(2)
    df.loc[df.Ticker == ticker, 'SMA_20'] = subdf['Close'].rolling(window=20).mean().round(2)
    df.loc[df.Ticker == ticker, 'SMA_50'] = subdf['Close'].rolling(window=50).mean().round(2)
    df.loc[df.Ticker == ticker, 'SMA_150'] = subdf['Close'].rolling(window=150).mean().round(2)
    df.loc[df.Ticker == ticker, 'SMA_200'] = subdf['Close'].rolling(window=200).mean().round(2)

    # Extract the final values for each metric for the current ticker
    mov_avg_7 = df.loc[(df.Ticker == ticker), 'SMA_7'].iloc[-1]
    mov_avg_10 = df.loc[(df.Ticker == ticker), 'SMA_10'].iloc[-1]
    mov_avg_20 = df.loc[(df.Ticker == ticker), 'SMA_20'].iloc[-1]
    mov_avg_50 = df.loc[(df.Ticker == ticker), 'SMA_50'].iloc[-1]
    mov_avg_150 = df.loc[(df.Ticker == ticker), 'SMA_150'].iloc[-1]
    mov_avg_200 = df.loc[(df.Ticker == ticker), 'SMA_200'].iloc[-1]
    mov_avg_200_20 = df.loc[(df.Ticker == ticker), 'SMA_200'].iloc[-32]
    low_of_52week = min(subdf['Close'][-250:])
    high_of_52week = max(subdf['Close'][-250:])

    current_close = subdf['Close'].iloc[-1]
    previous_close = subdf['Close'].iloc[-2]
    turnover = subdf['Volume'].iloc[-1] * subdf['Close'].iloc[-1]
    true_range_10d = (max(subdf['Close'].iloc[-10:-1]) - min(subdf['Close'].iloc[-10:-1]))

    # Add conditions to df using .loc (close and SMAs alignment)
    if (current_close > mov_avg_50 and mov_avg_50> mov_avg_150 and mov_avg_150 > mov_avg_200 and mov_avg_200 > mov_avg_200_20) :
        df.loc[(df.Ticker == ticker) & (df.index == df[df.Ticker == ticker].index[-1]), 'sma_condition_1-5'] = 1

    # Current Price is at least 40% above 52 week low (Many of the best are up 100-300% before coming out of consolidation)
    if (current_close >= (1.40*low_of_52week)) and (current_close >= (0.75*high_of_52week)):
        df.loc[(df.Ticker == ticker) & (df.index == df[df.Ticker == ticker].index[-1]), 'sma_condition_6&7'] = 1

    print(f"Ticker: {ticker}")
    print(f"SMA_7: {mov_avg_7}")
    print(f"SMA_10: {mov_avg_10}")
    print(f"SMA_20: {mov_avg_20}")
    print(f"SMA_50: {mov_avg_50}")
    print(f"SMA_150: {mov_avg_150}")
    print(f"SMA_200: {mov_avg_200}")
    print(f"SMA_200_20: {mov_avg_200_20}")
    print(f"52-Week Low: {low_of_52week}")
    print(f"52-Week High: {high_of_52week}")
    print("\n")

print(df)

# mov_avg_200_20 = df['SMA_200'][-32]  # SMA 200 1 month before (for calculating trending condition)
# low_of_52week = min(df['Close'][-250:])
# high_of_52week = max(df['Close'][-250:])





df.to_csv('result.csv')