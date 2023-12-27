import pandas as pd


def visualize_predefined_dataframe():
    df = pd.read_csv('database/daily/step_5_-_all_symbols_daily_enriched_19_ta_lib_patterns_last_days_extracted_signals_added_filtered_for_visualization.csv')

    df['signal'] = ''

    companies = []
    details = {}
    for i, row in df.iterrows():

        companies.append(df.at[i, 'Ticker'])

        if df.at[i, 'bull_pattern_count'] != 0 and df.at[i, 'bear_pattern_count'] == 0:
            df.at[i, 'signal'] = 'Buy'
        elif df.at[i, 'bull_pattern_count'] == 0 and df.at[i, 'bear_pattern_count'] != 0:
            df.at[i, 'signal'] = 'Sell'
        elif df.at[i, 'bull_pattern_count'] != 0 and df.at[i, 'bear_pattern_count'] != 0:
            df.at[i, 'signal'] = 'Mixed'

        details[df.at[i, 'Ticker']] =   []
        details[df.at[i, 'Ticker']].append(df.at[i, 'signal'])
        details[df.at[i, 'Ticker']].append(df.at[i, 'Date'])
        details[df.at[i, 'Ticker']].append(df.at[i, 'bull_pattern_names'])
        details[df.at[i, 'Ticker']].append(df.at[i, 'bear_pattern_names'])


    for key, value in details.items():
        print(key, value)


    # print(companies)
    # print(details)
    # print(df)

    # df.to_csv('database/daily/all_symbols_daily_patterns_added_and_filtered.csv')

    return details
