import pandas as pd


def check_for_setups_in_last_days():
    df = pd.read_csv('database/daily/last_days_data_enriched19_daily.csv')

    # First index from the enrichment is 'CDLMARUBOZU', therefore this is the start index for the columns loop

    column_names = df.columns.values.tolist()
    start_index = column_names.index('CDLMARUBOZU')

    total_rows = df.shape[0]
    total_cols = df.shape[1]

    # print(start_index)
    # print(column_names)
    #

    for row in range(0, total_rows):
        bull_pattern_count = 0
        bear_pattern_count = 0
        bull_pattern_names = []
        bear_pattern_names = []

        for col in range(start_index, len(column_names)):
            if df[row, col] == 100:
                bull_pattern_count += 1
                bull_pattern_names.append(column_names[col])
            if df[row, col] == -100:
                bear_pattern_count -= 1
                bear_pattern_names.append(column_names[col])
        df[row, 'bull_pattern_count'] = bull_pattern_count
        df[row, 'bull_pattern_names'] = ','.join(bull_pattern_names)
        df[row, 'bear_pattern_count'] = bear_pattern_count
        df[row, 'bear_pattern_names'] = ','.join(bear_pattern_names)

    print(df)

    return
