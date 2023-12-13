import pandas as pd
import numpy as np
import ta


def enrichment_sma(retrieved_df):
    df = retrieved_df

    df['RSI'] = ta.momentum.rsi(df.Close, window=14)
    df['ADX'] = ta.trend.ADXIndicator(df.High, df.Low, df.Close, window=14)
    df['MACD'] = ta.trend.MACDIndicator()
    df['SMA_50'] = ta.trend.sma_indicator(df.Close, window=50)
    df['SMA_200'] = ta.trend.sma_indicator(df.Close, window=200)


    for index in range(1, df.index.size):
        if (df.SMA_50.iloc[index-1] < df.SMA_200.iloc[index-1] and df.SMA_50.iloc[index] > df.SMA_200.iloc[index]):
            df['SMA_50-SMA_200-Crossover'] = 'bull'

        if (df.SMA_50.iloc[index-1] > df.SMA_200.iloc[index-1] and df.SMA_50.iloc[index] < df.SMA_200.iloc[index]):
            df['SMA_50-SMA_200-Crossover'] = 'bear'

    print(df)
    print(df.head())

    # df.to_csv('step2_1d-enriched_data.csv', index=True)

    return df
