import pandas as pd


def rsi_results_visualization_code(input_file_csv):

    df = pd.read_csv(input_file_csv)
    list = df['Ticker']
    print(list)

    return list