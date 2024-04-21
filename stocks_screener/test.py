import pandas as pd


def test_code():
    data = [{'a': 1, 'b': 10, 'c': 100, 'd': 1000},
            {'a': 2, 'b': 20, 'c': 800, 'd': 2000},
            {'a': 3, 'b': 30, 'c': 300, 'd': 3000}]

    df = pd.DataFrame(data)

    total_rows = df.shape[0]
    total_cols = df.shape[1]
    for row in range(0, total_rows):
        for col in range(0, total_cols):
            if df.iloc[row, col] == 800:
                row['pattern'] = 'pattern'


            # b_1_1 = df.iloc[1, 1]
    # print(b_1_1)

    print(df)

    return



'''
Code snippets: 
# Calculate volatility as the difference between High and Low prices
df['Volatility'] = df['High'] - df['Low']

# Shift the volatility by 1 to compare with the previous period
previous_volatility = df['Volatility'].shift(1)

# Check if the current volatility is less than the volatility of the previous period
df['volatility_transition'] = (df['Volatility'] < previous_volatility).astype(int)

# Count consecutive occurrences of 1 in volatility_transition
consecutive_count = df['volatility_transition'].groupby(
    (df['volatility_transition'] != df['volatility_transition'].shift()).cumsum()).cumcount() + 1

# Add a new column 'volatility_result'
df['volatility_result'] = 'Not Tightening'

# Check for 6 consecutive rows where volatility_transition is equal to 1
if (consecutive_count >= 10).any():
    df.loc[consecutive_count >= 10, 'volatility_result'] = 'Tightening'

# Print the DataFrame with the new columns
print(df[['Date', 'Ticker', 'Volatility', 'volatility_transition', 'volatility_result']])
'''