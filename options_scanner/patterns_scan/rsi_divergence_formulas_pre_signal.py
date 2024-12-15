import pandas as pd
import os


def rsi_divergence_formulas_calcs_pre_signal(input_file):
    input_file = input_file
    if input_file == 'custom':
        df = pd.read_csv(
            r'C:\Users\npara\coding\np-github\Projects\options_scanner\rsi_divergence_files\step1_retrieve_finviz_beta.csv')
        print("Opening the step1 retrieve custom file ....")
        file_to_be_saved_single_use = 'step2_result_finviz_beta_pre-signal.csv'
        file_to_be_saved_filtered = 'step3_result_filtered_finviz_beta_pre-signal.csv'

    elif input_file == 'options_favourites':
        df = pd.read_csv(
            r'C:\Users\npara\coding\np-github\Projects\options_scanner\rsi_divergence_files\step1_retrieve_options_favourites.csv')
        print("Opening the step1 retrieve options favourites file ....")
        file_to_be_saved_single_use = 'step2_result_options_favourites_pre-signal.csv'
        file_to_be_saved_filtered = 'step3_result_filtered_options_favourites_pre-signal.csv'

    if 'Capital Gains' in df.columns:
        df.drop(columns='Capital Gains', inplace=True)
    else:
        print("Column 'Capital Gains' does not exist.")

    df['rsi_peak_rsi_value'] = 0 # (equivalent to column P)
    df['rsi_peak_high_value'] = 0 # (equivalent to column Q)
    df['rsi_bottom_rsi_value'] = 0 # (equivalent to column R)
    df['rsi_bottom_low_value'] = 0 # (equivalent to column S)

    for i in range(len(df)):
        if df.at[i, 'desc_number'] > 116:  # Check threshold condition
            df.at[i, 'rsi_peak_rsi_value'] = 0
            df.at[i, 'rsi_peak_high_value'] = 0
        else:
            # Ensure we are within bounds to check 4 rows above and below
            if (i >= 4 and i < len(df) - 4):  # Avoid out-of-bounds errors
                # Check if RSI is a peak compared to surrounding values
                if (df.at[i, 'RSI'] >= df.at[i-1, 'RSI'] and
                    df.at[i, 'RSI'] >= df.at[i-2, 'RSI'] and
                    df.at[i, 'RSI'] >= df.at[i-3, 'RSI'] and
                    df.at[i, 'RSI'] >= df.at[i-4, 'RSI'] and
                    df.at[i, 'RSI'] >= df.at[i+1, 'RSI'] and
                    df.at[i, 'RSI'] >= df.at[i+2, 'RSI'] and
                    df.at[i, 'RSI'] >= df.at[i+3, 'RSI'] and
                    df.at[i, 'RSI'] >= df.at[i+4, 'RSI']):
                    df.at[i, 'rsi_peak_rsi_value'] = df.at[i, 'RSI']  # Assign RSI value
                    df.at[i, 'rsi_peak_high_value'] = df.at[i, 'High']  # Assign High value as the peak
                else:
                    # Copy previous values if current row is not a peak
                    df.at[i, 'rsi_peak_rsi_value'] = df.at[i-1, 'rsi_peak_rsi_value']
                    df.at[i, 'rsi_peak_high_value'] = df.at[i-1, 'rsi_peak_high_value']
            else:
                # Copy previous values for out-of-bound rows
                if i >= 1:  # Only if there's a valid previous row
                    df.at[i, 'rsi_peak_rsi_value'] = df.at[i-1, 'rsi_peak_rsi_value']
                    df.at[i, 'rsi_peak_high_value'] = df.at[i-1, 'rsi_peak_high_value']
                else:
                    # Initialize to zero for the first row
                    df.at[i, 'rsi_peak_rsi_value'] = 0
                    df.at[i, 'rsi_peak_high_value'] = 0

    for i in range(len(df)):  # Start from row 11 to ensure sufficient surrounding rows
        if df.at[i, 'desc_number'] > 116:  # Check if desc_number is greater than 116
            df.at[i, 'rsi_bottom_rsi_value'] = 0
            df.at[i, 'rsi_bottom_low_value'] = 0
        else:
             # Ensure we are within bounds to check 4 rows above and below
            if (i >= 4 and i < len(df) - 4):  # Avoid out-of-bounds errors
                # Check if RSI is a bottom compared to surrounding rows
                if (df.at[i, 'RSI'] <= df.at[i-1, 'RSI'] and
                    df.at[i, 'RSI'] <= df.at[i-2, 'RSI'] and
                    df.at[i, 'RSI'] <= df.at[i-3, 'RSI'] and
                    df.at[i, 'RSI'] <= df.at[i-4, 'RSI'] and
                    df.at[i, 'RSI'] <= df.at[i+1, 'RSI'] and
                    df.at[i, 'RSI'] <= df.at[i+2, 'RSI'] and
                    df.at[i, 'RSI'] <= df.at[i+3, 'RSI'] and
                    df.at[i, 'RSI'] <= df.at[i+4, 'RSI']):
                    df.at[i, 'rsi_bottom_rsi_value'] = df.at[i, 'RSI']  # Assign RSI value as bottom
                    df.at[i, 'rsi_bottom_low_value'] = df.at[i, 'Low']  # Assign Low value as bottom
                else:
                    df.at[i, 'rsi_bottom_rsi_value'] = df.at[i-1, 'rsi_bottom_rsi_value']  # Copy previous rsi_bottom_rsi_value
                    df.at[i, 'rsi_bottom_low_value'] = df.at[i-1, 'rsi_bottom_low_value']  # Copy previous rsi_bottom_low_value
            else:
                # Copy previous values for out-of-bound rows
                if i >= 1:  # Only if there's a valid previous row
                    df.at[i, 'rsi_bottom_rsi_value'] = df.at[i-1, 'rsi_bottom_rsi_value']
                    df.at[i, 'rsi_bottom_low_value'] = df.at[i-1, 'rsi_bottom_low_value']
                else:
                    # Initialize to zero for the first row
                    df.at[i, 'rsi_bottom_rsi_value'] = 0
                    df.at[i, 'rsi_bottom_low_value'] = 0

    df['be_current_rsi_less_than_peak'] = 0

    print("Peaks and bottoms RSI & Values are calculated .... ")

    for i in range(len(df)):
        if df.at[i, 'desc_number'] > 105:  # Check if desc_number is greater than 105
            df.at[i, 'be_current_rsi_less_than_peak'] = 0
        else:
            # Compare RSI with rsi_peak_rsi_value
            if df.at[i, 'RSI'] < df.at[i, 'rsi_peak_rsi_value']:
                df.at[i, 'be_current_rsi_less_than_peak'] = 1
            else:
                df.at[i, 'be_current_rsi_less_than_peak'] = 0

    df['be_current_price_close_above_rsi_peak'] = 0

    for i in range(len(df)):
        if df.at[i, 'desc_number'] > 105:  # Check if desc_number is greater than 105
            df.at[i, 'be_current_price_close_above_rsi_peak'] = 0
        else:
            # Compare Close with rsi_peak_high_value
            if df.at[i, 'Close'] >= df.at[i, 'rsi_peak_high_value']:
                df.at[i, 'be_current_price_close_above_rsi_peak'] = 1
            else:
                df.at[i, 'be_current_price_close_above_rsi_peak'] = 0

    df['be_pre_signal_1'] = 0

    for i in range(len(df)):
        if df.at[i, 'be_current_rsi_less_than_peak'] + df.at[i, 'be_current_price_close_above_rsi_peak'] == 2:
            df.at[i, 'be_pre_signal_1'] = 1
        else:
            df.at[i, 'be_pre_signal_1'] = 0

    df['be_pre_signal_last_10'] = 0

    for i in range(13, len(df)):  # Start at index 13 (i.e., row 14 in Excel terms)
        if df.at[i, 'desc_number'] >= 112:  # Check if desc_number is greater than or equal to 112
            df.at[i, 'be_pre_signal_last_10'] = 0
        else:
            # Sum the values in column V from row i-9 to i (previous 10 rows)
            if df.loc[i - 9:i, 'be_pre_signal_1'].sum() > 0:
                df.at[i, 'be_pre_signal_last_10'] = 2
            else:
                df.at[i, 'be_pre_signal_last_10'] = 0

    df['be_close_below_SMA65'] = 0

    for i in range(len(df)):
        if df.at[i, 'Close'] < df.at[i, 'SMA_65']:  # Compare Close with SMA_65
            df.at[i, 'be_close_below_SMA65'] = 1
        else:
            df.at[i, 'be_close_below_SMA65'] = 0

    df['be_signal'] = 0

    for i in range(len(df)):
        # Sum the values in columns W (be_pre_signal_last_10) and X (be_close_below_SMA65) for the current row
        if df.at[i, 'be_pre_signal_last_10'] + df.at[i, 'be_close_below_SMA65'] == 2:  # Check if sum equals 3
            df.at[i, 'be_signal'] = "Sell"
        else:
            df.at[i, 'be_signal'] = 0

    df['bu_current_rsi_more_than_bottom'] = 0

    for i in range(len(df)):
        if df.at[i, 'desc_number'] > 105:  # Check if desc_number is greater than 105
            df.at[i, 'bu_current_rsi_more_than_bottom'] = 0
        else:
            # Compare rsi (J) with rsi_bottom_rsi_value (R)
            if df.at[i, 'RSI'] > df.at[i, 'rsi_bottom_rsi_value']:
                df.at[i, 'bu_current_rsi_more_than_bottom'] = 1
            else:
                df.at[i, 'bu_current_rsi_more_than_bottom'] = 0

    df['bu_current_price_close_below_rsi_bottom'] = 0

    for i in range(len(df)):
        if df.at[i, 'desc_number'] > 105:  # Check if desc_number is greater than 105
            df.at[i, 'bu_current_price_close_below_rsi_bottom'] = 0
        else:
            # Compare Close (G) with rsi_bottom_low_value (S)
            if df.at[i, 'Close'] <= df.at[i, 'rsi_bottom_low_value']:  # Check if Close <= rsi_bottom_low_value
                df.at[i, 'bu_current_price_close_below_rsi_bottom'] = 1
            else:
                df.at[i, 'bu_current_price_close_below_rsi_bottom'] = 0

    df['bu_pre_signal_1'] = 0

    for i in range(len(df)):
        # Check if the sum of 'bu_current_rsi_more_than_bottom' (Z) and 'bu_current_price_close_above_rsi_peak' (AA) equals 2
        if df.at[i, 'bu_current_rsi_more_than_bottom'] + df.at[i, 'bu_current_price_close_below_rsi_bottom'] == 2:
            df.at[i, 'bu_pre_signal_1'] = 1
        else:
            df.at[i, 'bu_pre_signal_1'] = 0

    df['bu_pre_signal_last_13'] = 0

    # Apply the formula for each row, starting from row 16 (index 15)
    for i in range(15, len(df)):  # Start from row 16 (index 15)
        if df.at[i, 'desc_number'] > 107:  # Check if desc_number is greater than 107
            df.at[i, 'bu_pre_signal_last_13'] = 0
        else:
            # Sum the values of 'bu_pre_signal_1' from AB4 to AB16 (i.e., from row 4 to row 16)
            start_idx = max(i - 12, 0)  # Ensure we don't go below index 0
            end_idx = i  # The current row (i)
            sum_bu_pre_signal_1 = df.loc[start_idx:end_idx, 'bu_pre_signal_1'].sum()  # Sum the values

            # If the sum is greater than 0, set the value to 2; otherwise, set it to 0
            if sum_bu_pre_signal_1 > 0:
                df.at[i, 'bu_pre_signal_last_13'] = 2
            else:
                df.at[i, 'bu_pre_signal_last_13'] = 0

    df['bu_close_above_SMA65'] = 0

    for i in range(len(df)):
        if df.at[i, 'Close'] > df.at[i, 'SMA_65']:  # Check if Close (G) is greater than SMA_65 (N)
            df.at[i, 'bu_close_above_SMA65'] = 1
        else:
            df.at[i, 'bu_close_above_SMA65'] = 0

    df['bu_signal'] = 0

    for i in range(len(df)):
        if df.at[i, 'bu_pre_signal_last_13'] + df.at[i, 'bu_close_above_SMA65'] == 2:
            df.at[i, 'bu_signal'] = "Buy"
        else:
            df.at[i, 'bu_signal'] = 0

    df['Combined_Signals_65'] = 0

    for i in range(len(df)):
        if df.at[i, 'be_signal'] == "Sell":
            df.at[i, 'Combined_Signals_65'] = "Sell"
        elif df.at[i, 'bu_signal'] == "Buy":
            df.at[i, 'Combined_Signals_65'] = "Buy"
        else:
            df.at[i, 'Combined_Signals_65'] = 0

    # Define a small tolerance for floating-point comparison
    tolerance = 1e-9

    # Calculate the difference and fill NaN with 0
    df['SMA_65_trend_diff'] = df['SMA_65'].diff().fillna(0)

    # Use the tolerance to handle floating-point comparisons
    df['SMA_65_trend'] = df['SMA_65_trend_diff'].apply(
        lambda x: 'Up' if x > tolerance else ('Down' if x < -tolerance else 'Neutral')
    )

    filtered_df = df[df['Combined_Signals_65'] != 0]

    print("Signals are extracted ... ")

    print(filtered_df)
    folder_path_single_use = r'C:\Users\npara\coding\np-github\Projects\options_scanner\rsi_divergence_files'

    full_path_single_use = os.path.join(folder_path_single_use, file_to_be_saved_single_use)
    df.to_csv(full_path_single_use, index=True)

    full_path_filtered = os.path.join(folder_path_single_use, file_to_be_saved_filtered)
    filtered_df.to_csv(full_path_filtered, index=True)

    print("RSI divergence scans signals have been saved (PRE-SIGNAL) ")

    return filtered_df