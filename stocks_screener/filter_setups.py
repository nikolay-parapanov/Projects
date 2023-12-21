import pandas as pd


def filter_setups_for_summary():
    df = pd.read_csv('database/daily/all_symbols_daily_patterns_added.csv')

    df['filtered'] = 0

    for i, row in df.iterrows():
        if row['bull_pattern_count'] != 0 or row['bear_pattern_count'] != 0:
            print('yes')
            df.at[i, 'filtered'] = 1

    df_filtered = df[df['filtered'] == 1]

    df_filtered.to_csv('database/daily/all_symbols_daily_patterns_added_and_filtered.csv')

    return
