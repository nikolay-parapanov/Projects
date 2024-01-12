import pandas as pd


def filter_setups_for_summary():
    df = pd.read_csv('database/daily/step_4_-_all_symbols_daily_enriched_19_ta_lib_patterns_last_days_extracted_signals_added.csv')

    df['filtered'] = 0

    for i, row in df.iterrows():
        if row['bull_pattern_count'] != 0 or row['bear_pattern_count'] != 0:
            # print('yes')
            df.at[i, 'filtered'] = 1

    df_filtered = df[df['filtered'] == 1]

    df_filtered.to_csv('database/daily/step_5_-_all_symbols_daily_enriched_19_ta_lib_patterns_last_days_extracted_signals_added_filtered_for_visualization.csv')

    return
