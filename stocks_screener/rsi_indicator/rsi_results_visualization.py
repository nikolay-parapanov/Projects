import pandas as pd
import mappings.finviz_industry as ticker_dict

def rsi_results_visualization_code(input_file_csv):

    df = pd.read_csv(input_file_csv)
    list = df['Ticker']
    print(list)

    stock_dict = ticker_dict.stock_dict_code()
    print(stock_dict)

    return list, stock_dict

