import pandas as pd


def check_for_setups_in_last_days():
    df = pd.read_csv('database/daily/step_3_-_all_symbols_daily_enriched_19_ta_lib_patterns_last_days_extracted.csv')

    # First index from the enrichment is 'CDLMARUBOZU', therefore this is the start index for the columns nested loop

    column_names = df.columns.values.tolist()
    start_index = column_names.index('CDLMARUBOZU')

    total_rows = df.shape[0]
    total_cols = df.shape[1]

    # print(start_index)
    # print(column_names)

    df['bull_pattern_count'] = 0
    df['bull_pattern_names'] = ''
    df['bear_pattern_count'] = 0
    df['bear_pattern_names'] = ''

    for row in range(0, total_rows):
        bull_pattern_count = 0
        bear_pattern_count = 0
        bull_pattern_names = []
        bear_pattern_names = []

        for col in range(start_index, len(column_names)):
            if df.iloc[row, col] == 100:
                bull_pattern_count += 1
                # print(column_names[col])
                bull_pattern_names.append(column_names[col])
            if df.iloc[row, col] == -100:
                bear_pattern_count += 1
                bear_pattern_names.append(column_names[col])
            #
        df.iloc[row, len(column_names)] = bull_pattern_count
        df.iloc[row, len(column_names)+1] = ','.join(bull_pattern_names)
        df.iloc[row, len(column_names)+2] = bear_pattern_count
        df.iloc[row, len(column_names)+3] = ','.join(bear_pattern_names)


    print(df)
    df.to_csv('database/daily/step_4_-_all_symbols_daily_enriched_19_ta_lib_patterns_last_days_extracted_signals_added.csv')

    return
