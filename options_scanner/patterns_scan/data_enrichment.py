import pandas as pd
import os


def rsi_divergence_signals_cut_by_day(input_file, output_file):
    input_file = input_file
    output_file = output_file

    df = pd.read_csv(input_file)

    df = df.drop(columns=['Unnamed: 0'])

    if 'Date' in df.columns:
        df.rename(columns={'Date': 'Datetime'}, inplace=True)
        print("Column 'Date' renamed to 'Datetime'.")
    else:
        print("Column 'Date' does not exist.")

    # Remove ":00-05:00" from the 'Datetime' column
    df['Datetime'] = df['Datetime'].astype(str).str.replace(r':00-05:00$', '', regex=True)

    # Move 'Combined Signals' to be right after 'Ticker'
    columns = list(df.columns)  # Get the list of columns
    columns.remove('Combined_Signals_65')  # Remove 'Combined Signals' from the list
    columns.remove('bu_signal')  # Remove 'Combined Signals' from the list
    columns.remove('be_signal')  # Remove 'Combined Signals' from the list
    columns.remove('vol_vs_avrg_vol')  # Remove 'Combined Signals' from the list
    columns.remove('RSI')  # Remove 'Combined Signals' from the list
    ticker_index = columns.index('Ticker')  # Find the index of 'Ticker'
    # Insert 'Combined Signals' right after 'Ticker'

    # Add a new column for the % difference between Close and SMA_65
    df['Close_SMA65_Diff_Percent'] = ((df['Close'] - df['SMA_65']) / df['SMA_65']) * 100

    columns.insert(ticker_index + 1, 'Combined_Signals_65')
    columns.insert(ticker_index + 2, 'bu_signal')
    columns.insert(ticker_index + 3, 'be_signal')
    columns.insert(ticker_index + 4, 'Close_SMA65_Diff_Percent')
    columns.insert(ticker_index + 5, 'vol_vs_avrg_vol')
    columns.insert(ticker_index + 6, 'RSI')

    # Reorder the DataFrame
    df = df[columns]

    # Convert back to datetime object if needed
    df['Datetime'] = pd.to_datetime(df['Datetime'])

    # Sort the data by date to ensure chronological order
    df = df.sort_values(by='Datetime')

    # Extract the unique dates from the 'Datetime' column
    unique_days = sorted(df['Datetime'].dt.date.unique())

    # Get the last 3 unique dates (or fewer if the dataset has less than 3 unique dates)
    last_3_days = unique_days[-3:]

    # Filter the DataFrame for rows belonging to these last 3 days
    last_3_days_signals = df[df['Datetime'].dt.date.isin(last_3_days)]

    # Add a column for just the date (no time)
    last_3_days_signals['Date'] = last_3_days_signals['Datetime'].dt.date

    # Sort by 'Date' (newest to oldest) and then by 'Ticker' (alphabetically)
    last_3_days_signals = last_3_days_signals.sort_values(by=['Date', 'Ticker'], ascending=[False, True])
    last_3_days_signals = last_3_days_signals.drop(columns=['Date'])

    # Convert to datetime and format
    last_3_days_signals['Datetime'] = pd.to_datetime(last_3_days_signals['Datetime']).dt.strftime('%d/%H:%M')

    # Convert columns to numeric
    columns_to_format = ['Open', 'High', 'Low', 'Close', 'RSI', 'ATR', 'SMA_20', 'SMA_50', 'SMA_200', 'SMA_65',
                         'rsi_peak_rsi_value', 'rsi_peak_high_value', 'rsi_bottom_rsi_value', 'rsi_bottom_low_value','vol_vs_avrg_vol','Close_SMA65_Diff_Percent']
    last_3_days_signals[columns_to_format] = last_3_days_signals[columns_to_format].apply(pd.to_numeric)

    # Round to 2 decimals
    last_3_days_signals[columns_to_format] = last_3_days_signals[columns_to_format].round(2)

    folder_path_general = r'C:\Users\npara\coding\np-github\Projects\options_scanner\rsi_divergence_files'
    file_name_last_day_data = output_file

    full_path_single_use = os.path.join(folder_path_general, file_name_last_day_data)
    last_3_days_signals.to_csv(full_path_single_use, index=True)


    print('File saved after data enrichment')

    return