import pandas as pd
from pyxlsb import open_workbook

def signals_extraction():

    # Replace this with the path to your CSV file
    file_path = r'C:\Users\npara\OneDrive\Desktop\patterns\model_period_60_1d.xlsb'

    # Reading the .xlsb file starting from row 5
    with open_workbook(file_path) as wb:
        with wb.get_sheet(1) as sheet:
            data = []
            for row in sheet.rows():
                data.append([item.v for item in row])

    # Convert to a pandas DataFrame and skip the first 4 rows (to make row 5 the header)
    df = pd.DataFrame(data[4:], columns=data[4])  # 5th row is the header

    # Filter rows where Signal_3p contains "long last 3 peaks"
    filtered_df = df[df['Signal_3p'].str.contains("long last 3 peaks", na=False)]

    # Extract unique tickers from the filtered DataFrame
    tickers_with_signal = filtered_df['Ticker'].unique()

    # Convert to a list (optional)
    tickers_with_signal_list = tickers_with_signal.tolist()

    # Print the list of tickers
    print(tickers_with_signal_list)
    # Display the DataFrame
    print(df)

    return tickers_with_signal_list

