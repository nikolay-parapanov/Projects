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

    # Add a new column for the % difference between Close and SMA_65
    last_3_days_signals['Close_SMA65_Diff_Percent'] = ((last_3_days_signals['Close'] - last_3_days_signals['SMA_65']) / last_3_days_signals['SMA_65']) * 100

    # Convert columns to numeric
    columns_to_format = ['Open', 'High', 'Low', 'Close', 'RSI', 'ATR', 'SMA_20', 'SMA_50', 'SMA_200', 'SMA_65',
                         'rsi_peak_rsi_value', 'rsi_peak_high_value', 'rsi_bottom_rsi_value', 'rsi_bottom_low_value','vol_vs_avrg_vol','Close_SMA65_Diff_Percent']
    last_3_days_signals[columns_to_format] = last_3_days_signals[columns_to_format].apply(pd.to_numeric)

    # Round to 2 decimals
    last_3_days_signals[columns_to_format] = last_3_days_signals[columns_to_format].round(2)

    daily_retrieve = r'C:\Users\npara\coding\np-github\Projects\options_scanner\rsi_divergence_files\step0_retrieve_daily.csv'  # Replace with the path to your CSV file
    df2 = pd.read_csv(daily_retrieve)

    # Select only the desired columns from df2
    df2_selected_columns = df2[['Ticker', 'SMA20 vs SMA50_daily', 'SMA50 vs SMA200_daily',
                                'Avg_Volume_14_daily', 'RSI_daily', 'ATR_daily']]

    # Merge the two dataframes on the 'Ticker' column using a left join (keep only tickers from df1)
    merged_df = pd.merge(last_3_days_signals, df2_selected_columns, on='Ticker', how='left')

    print("merged df: ..................")
    print(merged_df)

    # Convert columns to numeric
    columns_to_format = ['Open', 'High', 'Low', 'Close', 'RSI', 'ATR', 'SMA_20', 'SMA_50', 'SMA_200', 'SMA_65',
                         'rsi_peak_rsi_value', 'rsi_peak_high_value', 'rsi_bottom_rsi_value', 'rsi_bottom_low_value',
                         'vol_vs_avrg_vol', 'Close_SMA65_Diff_Percent', 'Avg_Volume_14_daily', 'RSI_daily', 'ATR_daily']

    merged_df[columns_to_format] = merged_df[columns_to_format].apply(pd.to_numeric)
    # Round to 2 decimals
    merged_df[columns_to_format] = merged_df[columns_to_format].round(2)

    # Move 'Combined Signals' to be right after 'Ticker' and order the columns
    columns = list(merged_df.columns)
    reorder_columns = ['Datetime', 'Interval','Ticker', 'Combined_Signals_65', 'SMA_65_trend', 'SMA20 vs SMA50_daily', 'SMA50 vs SMA200_daily',
                       'Close_SMA65_Diff_Percent',
                       'vol_vs_avrg_vol', 'RSI', 'ATR_daily', 'RSI_daily'] + [col for col in columns if
                                                                 col not in ['Ticker', 'Combined_Signals_65',
                                                                             'SMA_65_trend',
                                                                             'SMA20 vs SMA50_daily',
                                                                             'SMA50 vs SMA200_daily',
                                                                             'Close_SMA65_Diff_Percent',
                                                                             'vol_vs_avrg_vol', 'RSI', 'ATR_daily']]

    merged_df = merged_df[reorder_columns]

    folder_path_general = r'C:\Users\npara\coding\np-github\Projects\options_scanner\rsi_divergence_files'
    file_name_last_day_data = output_file

    full_path_single_use = os.path.join(folder_path_general, file_name_last_day_data)
    merged_df.to_csv(full_path_single_use, index=True)


    print('File saved after data enrichment')

    return