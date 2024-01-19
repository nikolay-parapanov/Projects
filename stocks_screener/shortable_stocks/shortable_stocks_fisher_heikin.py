from general_functions import import_data_as_list_from_csv_file
import pandas as pd

def check_if_list_contains_predefined_tickers(predefined_tickers, current_list_to_be_checked):
    ticker_list = []
    with open(predefined_tickers) as f:
        lines = f.read().splitlines()

    for line in lines:
        ticker_list.append(line.split(',')[0])

    result_list = []
    for ticker in current_list_to_be_checked:
        if ticker in ticker_list:
            result_list.append(ticker)

    return result_list


def shortable_data_fisher_heikin_code():
    path = 'database/shortable_stocks/shortable_stocks_initial_screener_db.csv'
    imported_list = import_data_as_list_from_csv_file.import_data_as_list_from_csv_file_code(path)

    fisher_list = []
    heikin_ashi_uptrends = []
    heikin_ashi_downtrends = []

    for list in imported_list:
        if list[1] == 'Fisher_Transform_Cross_Up':
            fisher_list = list[2]
        if list[1] == 'Heikin-Ashi_Uptrends':
            heikin_ashi_uptrends = list[2]
        if list[1] == 'Heikin-Ashi_Downtrends':
            heikin_ashi_downtrends = list[2]

    # print('fisher_list:', len(fisher_list))
    # print('hau:', heikin_ashi_uptrends)
    # print('had:', heikin_ashi_downtrends)

    predefined_ticker_path = 'database/tickers_list/finviz_2200.csv'
    fisher_list_filtered = check_if_list_contains_predefined_tickers(predefined_ticker_path, fisher_list)
    len_fl = len(fisher_list_filtered)
    heikin_ashi_uptrends_filtered = check_if_list_contains_predefined_tickers(predefined_ticker_path, heikin_ashi_uptrends)
    len_hau = len(heikin_ashi_uptrends_filtered)
    heikin_ashi_downtrends_filtered = check_if_list_contains_predefined_tickers(predefined_ticker_path, heikin_ashi_downtrends)
    len_had = len(heikin_ashi_downtrends_filtered)

    cross_fisher_heikin = []
    for ticker in heikin_ashi_uptrends_filtered:
        if ticker in fisher_list_filtered:
            cross_fisher_heikin.append(ticker)

    len_cfh = len(cross_fisher_heikin)
    return fisher_list_filtered, heikin_ashi_uptrends_filtered, heikin_ashi_downtrends_filtered, len_fl, len_hau, len_had, len_cfh, cross_fisher_heikin
    # return [], [], heikin_ashi_downtrends_filtered
