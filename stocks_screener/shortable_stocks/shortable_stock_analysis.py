import pandas as pd

from general_functions import import_data_as_list_from_csv_file
from shortable_stocks.sort_tickers_by_decending_number_of_occurence import sort_tickers_by_decending_number_of_occurence

path = '../database/shortable_stocks/shortable_stocks_initial_screener_db.csv'

imported_list = import_data_as_list_from_csv_file.import_data_as_list_from_csv_file_code(path)

# df_sorted = sort_tickers_by_decending_number_of_occurence(imported_list)

bearish_screens = ['ADX_Bearish_Trends', 'CCI_Sell_Signals', 'EMA_50/120_Bearish_Crossovers',
                   'Fast_Stochastic_Overbought', 'Heikin-Ashi_Downtrends', 'MACD_Bearish_Signal_Cross',
                   'Parabolic_SAR_Sell_Signals', 'Williams_%R_Overbought', 'TRIX_Bearish_Signal_Cross',
                   'RSI_Overbought']
bullish_screens = ['ADX_Bullish_Trends', 'CCI_Buy_Signals', 'EMA_50/120_Bullish_Crossovers', 'Fast_Stochastic_Oversold',
                   'Heikin-Ashi_Uptrends', 'MACD_Bullish_Signal_Cross', 'Parabolic_SAR_Buy_Signals', 'RSI_Oversold',
                   'TRIX_Bullish_Signal_Cross', 'Williams_%R_Oversold']

bearish_tickers = []
bullish_tickers = []

for row in imported_list:
    screen = row[1]
    if screen in bullish_screens:
        for item in row[2]:
            bullish_tickers.append(item)
    elif screen in bearish_screens:
        for item in row[2]:
            bearish_tickers.append(item)

print('Bullish tickers sorted descending order by number of occurrence:')
sorted_bullish_tickers = sort_tickers_by_decending_number_of_occurence(bullish_tickers)
filtered_bullish_df = sorted_bullish_tickers[sorted_bullish_tickers['occurrence'] > 2]
filtered_bullish_df.loc[:, 'patterns'] = '-'
filtered_bullish_df.insert(0, 'signal', 'BUY')

for i, bullish_row in filtered_bullish_df.iterrows():
    for row_list in imported_list:
        if bullish_row['ticker'] in row_list[2]:
            filtered_bullish_df.at[i, 'patterns'] = filtered_bullish_df.at[i, 'patterns'] + ' ' + str(row_list[1])

    print('Bearish tickers sorted descending order by number of occurrence:')
    sorted_bearish_tickers = sort_tickers_by_decending_number_of_occurence(bearish_tickers)
    filtered_bearish_df = sorted_bearish_tickers[sorted_bearish_tickers['occurrence'] > 2]
    filtered_bearish_df['patterns'] = '.'
    filtered_bearish_df.insert(0, 'signal', 'SELL')

    for i, bearish_row in filtered_bearish_df.iterrows():
        for row_list in imported_list:
            if bearish_row['ticker'] in row_list[2]:
                filtered_bearish_df.at[i, 'patterns'] = filtered_bearish_df.at[i, 'patterns'] + ' ' + str(row_list[1])

    combined_db = pd.concat([filtered_bullish_df, filtered_bearish_df], ignore_index=True)
    print(combined_db)

    combined_db.to_csv(
        'database/shortable_stocks/result_buy_sell.csv')
