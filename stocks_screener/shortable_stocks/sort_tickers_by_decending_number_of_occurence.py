from collections import Counter
import pandas as pd

def get_all_tickers_in_flat_list(imported_list):
    all_tickers = []

    for row in imported_list:
        for ticker in row[2]:
            all_tickers.append(ticker)

    return all_tickers
def sort_tickers_by_decending_number_of_occurence(all_tickers):


    symbol_counts = Counter(all_tickers)
    sorted_symbol_counts = dict(sorted(symbol_counts.items(), key=lambda item: item[1], reverse=True))

    df = pd.DataFrame(list(sorted_symbol_counts.items()), columns=['ticker', 'occurrence'])
    #
    # filtered_df = df[df['occurrence'] > 6]
    # print(filtered_df)

    return df
