from general_functions import data_retrieve


def rsi_indicator_data_retrieve_code():
    daily_data = data_retrieve.data_collection_daily('database/tickers_list/finviz_2200.csv', 'database/daily/rsi/step_1_-_all_symbols_daily_initial_finviz_2200.csv')
    # print(daily_data)

    return print('data retrieved')
