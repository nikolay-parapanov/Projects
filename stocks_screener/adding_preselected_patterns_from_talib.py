import talib
import pandas as pd


# Data enrichment with few patterns from TA-lib

def adding_preselected_patterns_to_df_from_ta_lib():
    df = pd.read_csv('database/daily/all_symbols_initial_daily.csv')

    op = df['Open']
    hi = df['High']
    lo = df['Low']
    cl = df['Adj Close']

    preselected_patterns = ['CDLMARUBOZU', 'CDL3STARSINSOUTH', 'CDL3OUTSIDE', 'CDL3WHITESOLDIERS', 'CDLBREAKAWAY',
                            'CDLEVENINGSTAR', 'CDLHAMMER', 'CDLHARAMICROSS', 'CDLINVERTEDHAMMER', 'CDLMATCHINGLOW',
                            'CDLMORNINGDOJISTAR', 'CDLPIERCING', 'CDLRICKSHAWMAN', 'CDLRISEFALL3METHODS',
                            'CDLSEPARATINGLINES', 'CDLSTICKSANDWICH', 'CDLUNIQUE3RIVER', 'CDLTHRUSTING',
                            'CDLXSIDEGAP3METHODS']

    for pattern in preselected_patterns:
        pattern_function = getattr(talib, pattern)
        col_name = str(pattern)

        try:
            result = pattern_function(op, hi, lo, cl)
            df[col_name] = result;
        except:
            pass

    # print(df)
    df.to_csv('database/daily/all_symbols_daily_enriched_19.csv')

    return
