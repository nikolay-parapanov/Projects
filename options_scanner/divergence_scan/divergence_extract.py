import os

import matplotlib
matplotlib.use('Agg')  # Use the non-interactive backend to avoid GUI issues

import mplfinance as mpf
import pandas as pd
from pyxlsb import open_workbook


def signals_extraction():
    filenames = []
    file_path_model = r'C:\Users\npara\coding\np-github\Projects\options_scanner\divergence_scan\model\divergence_excel_model.xlsb'

    # Delete old PNG files in the output directory
    print('Deleting all previous charts in the static/charts folder ..')
    output_dir = 'divergence_scan/charts/'  # Directory for saving PNG files

    # Delete all old PNG files in the output directory
    for filename in os.listdir(output_dir):
        if filename.endswith('.png'):
            file_path = os.path.join(output_dir, filename)
            try:
                os.remove(file_path)
                print(f'Deleted old file: {filename}')
            except Exception as e:
                print(f'Error deleting file {filename}: {e}')

    print('Reading dataframe: ......')

    with open_workbook(file_path_model) as wb:
        with wb.get_sheet(1) as sheet:
            data = []
            for row in sheet.rows():
                data.append([item.v for item in row])

    # Row 5 (index 4) is the header
    header = data[4]  # Extract the header from row 5

    # Data starts from row 6 (index 5)
    df = pd.DataFrame(data[5:], columns=header)

    # Drop any rows that might still contain the header data
    df = df[df['Date'] != 'Date']  # Assuming 'Date' is one of the columns



    print('Dataframe loaded!')
    print(df.head())  # Print first few rows for verification
    print('setting index to date:')


    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df.set_index('Date', inplace=True)

    print(df.head())


    filtered_df_with_tickers_signal_long_last_3_peaks = df[df['Signal_3p'].str.contains("long last 3 peaks", na=False)].copy()

    tickers_with_signal_last_3_peaks_list = filtered_df_with_tickers_signal_long_last_3_peaks['Ticker'].unique().tolist()
    print(tickers_with_signal_last_3_peaks_list)


    numeric_columns = ['Open', 'High', 'Low', 'Close', 'Volume', 'Avg_Volume_10', 'RSI', 'SMA_20', 'SMA_50', 'SMA_200', 'resistance_high']

    # Ensure columns exist in DataFrame
    for column in numeric_columns:
        if column in df.columns:
            df.loc[:, column] = pd.to_numeric(df[column], errors='coerce')
        else:
            print(f"Warning: {column} not found in DataFrame")

    print('Tickers with signals list:')
    print(tickers_with_signal_last_3_peaks_list)

    for ticker in tickers_with_signal_last_3_peaks_list:
        ticker_data = df[df['Ticker'] == ticker].copy()

        if 'Date' in ticker_data.columns:
            ticker_data['Date'] = pd.to_datetime(ticker_data['Date'], errors='coerce')
            ticker_data.set_index('Date', inplace=True)

        ticker_data[['Open', 'High', 'Low', 'Close', 'Volume','resistance_high']] = ticker_data[['Open', 'High', 'Low', 'Close', 'Volume','resistance_high']].apply(pd.to_numeric, errors='coerce')

        resistance_high_value = ticker_data['resistance_high'].iloc[-1]  # Get the last known value
        resistance_line = mpf.make_addplot([resistance_high_value] * len(ticker_data), color='green', linestyle='--', width=1, label='Resistance High')

        avg_volume_line = mpf.make_addplot(ticker_data['Avg_Volume_10'], panel=1, color='black', width=1, label='Avg Volume')
        rsi_line = mpf.make_addplot(ticker_data['RSI'], panel=2, color='blue', width=1, label='RSI')
        sma_20_line = mpf.make_addplot(ticker_data['SMA_20'], color='green', width=1, label='SMA 20')
        sma_50_line = mpf.make_addplot(ticker_data['SMA_50'], color='orange', width=1, label='SMA 50')
        sma_200_line = mpf.make_addplot(ticker_data['SMA_200'], color='red', width=1, label='SMA 200')

        addplots = [resistance_line, sma_20_line, sma_50_line, sma_200_line, avg_volume_line, rsi_line]

        filename = f'static/charts/{ticker}_candlestick_chart.png'
        filenames.append(filename)

        print(f'Ploting for ticker:- {ticker}')

        mpf.plot(ticker_data, type='candle', volume=True,
                 title=f'{ticker} Candlestick Chart',
                 ylabel='Price', ylabel_lower='Volume',
                 style='charles',
                 addplot=addplots,
                 savefig=filename,
                 figratio=(12, 8),
                 figscale=1.2,
                 tight_layout=True)
