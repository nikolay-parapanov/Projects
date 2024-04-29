import pandas as pd
import mappings.finviz_industry as ticker_dict
import csv
from collections import defaultdict
from copy import deepcopy

def rsi_results_visualization_code(input_file_csv):
    df = pd.read_csv(input_file_csv)
    ticker_list = df['Ticker']
    print(ticker_list)

    stock_dict = ticker_dict.stock_dict_code()

    tickers_by_industry = defaultdict(list)

    for ticker in ticker_list:
        industry = stock_dict.get(ticker, {}).get('industry')
        if industry:
            tickers_by_industry[industry].append(ticker)

    shortable_stocks_file_path = 'database/shortable_stocks/shortable_stocks_initial_screener_db.csv'
    button_dict = {}
    with open(shortable_stocks_file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader, None)
        for row in reader:
            button_name, tickers = row[1], row[2]
            button_dict[button_name.strip()] = tickers.strip().split(', ')

    tickers_by_industry_crossed = deepcopy(tickers_by_industry)

    for industry, ticker_list in tickers_by_industry_crossed.items():
        for index, ticker in enumerate(ticker_list):
            button_names = []
            for button_name, button_tickers in button_dict.items():
                if ticker in button_tickers:
                    button_names.append(button_name)
            tickers_by_industry_crossed[industry][index] = (ticker, button_names)

    print("TICKERS BY INDUSTRY CROSSED:")
    for industry, ticker_dict_industry in tickers_by_industry_crossed.items():
        print(f"Industry: {industry}")
        for ticker, button_names in ticker_dict_industry:
            print(f"  Ticker: {ticker}, Button Names: {button_names}")

    return ticker_list, tickers_by_industry, tickers_by_industry_crossed
