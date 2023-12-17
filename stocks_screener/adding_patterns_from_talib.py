import talib



# Data enrichment with few patterns from TA-lib

def adding_patterns_to_df_from_ta_lib(df):
    try:
        result= talib.CDL3INSIDE(df['Open'],df['High'],df['Low'],df['Close'])
        df.insert(-1, 'CDL3INSIDE', result)
    except:

    return