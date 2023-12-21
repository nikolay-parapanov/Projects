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
