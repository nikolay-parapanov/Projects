import pandas as pd
import pandas_ta as ta
import general_functions.save_list_to_csv_file


def rsi_indicator_code():
    df_initial = pd.read_csv('database/daily/rsi/step_1_-_all_symbols_daily_initial_finviz_2200.csv')
    # # # Drop unnecessary columns ("Adj. Close")
    # df_initial = df_initial.drop(df_initial.columns[[6]], axis=1)
    print("DF INITIAL: .......................................................")
    print(df_initial)

    # Calculate RSI
    df_initial = df_initial.assign(RSI='')
    unique_tickers = df_initial["Ticker"].unique()
    print("LEN UNIQUE TICKERS: ....................................................")
    print(len(unique_tickers))

    for ticker in unique_tickers:
        subdf = df_initial.loc[df_initial.Ticker == ticker]
        rsi_values = ta.rsi(subdf.Close, length=14)
        df_initial.loc[df_initial.Ticker == ticker, 'RSI'] = rsi_values


    df_initial = df_initial.assign(rsi_flag1='', rsi_flag2='', rsi_result='')

    df = df_initial.groupby('Ticker').tail(8)
    df = df.reset_index(drop=True)

    print(df)
    for _, group in df.groupby('Ticker').head(5).groupby('Ticker'):
        # Check if any of the first 5 elements in the 'RSI' column are less than 29
        if (group['RSI'] < 29).any():
            # Set 'rsi_flag1' to 1 for all 5 items for this ticker
            df.loc[df['Ticker'] == group['Ticker'].iloc[0], 'rsi_flag1'] = 1

    # Check the last 3 elements in the 'RSI' column for each unique ticker
    for _, group in df.groupby('Ticker').tail(3).groupby('Ticker'):
        if (group['RSI'].between(30, 35)).any():
            # Set 'rsi_flag2' to 2 for all 3 items for this ticker
            df.loc[df['Ticker'] == group['Ticker'].iloc[0], 'rsi_flag2'] = 2

    # Replace empty strings with zeros in 'rsi_flag1' and 'rsi_flag2'
    df['rsi_flag1'] = df['rsi_flag1'].replace('', 0)
    df['rsi_flag2'] = df['rsi_flag2'].replace('', 0)

    # Sum 'rsi_flag1' and 'rsi_flag2' for each row and store the result in 'rsi_result'
    df['rsi_result'] = df[['rsi_flag1', 'rsi_flag2']].astype(int).sum(axis=1)

    filtered_df = df[df['rsi_result'] == 3]
    print("FILTERED DF WHERE RSI_RESULT = 3: .......................................")
    print(filtered_df)
    filtered_df.to_csv('database/daily/rsi/step_2.1_-_all_symbols_daily_finviz_2200_rsi_added_last_8_rows.csv')

    result_tickers = filtered_df["Ticker"].unique()

    print("DF BEFORE SAVE IN STEP 2 FILE: ..........................................")
    print(df)
    df.to_csv(
        'database/daily/rsi/step_2_-_all_symbols_daily_finviz_2200_rsi_added_last_8_rows.csv')

    pd.DataFrame(result_tickers, columns=['Ticker']).to_csv('database/daily/rsi/step_3_-_rsi_final_filter_as_list.csv',
                                                            index=False)
    print("RESULT TICKERS AS LIST: ...........................................")
    print(result_tickers)
    return result_tickers

