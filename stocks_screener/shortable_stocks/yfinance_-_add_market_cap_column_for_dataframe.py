import yfinance as yf

def add_market_cap_column_for_dataframe_code(df):
    tickers = df['ticker'].tolist()
    try:
        # Fetch stock information for all tickers
        stock_info = yf.download(tickers, period="1d", group_by='ticker', auto_adjust=True)

        # Reset index of the original DataFrame to ensure proper alignment
        df = df.reset_index(drop=True)

        # Check if 'Market Cap' is present in the columns
        if 'Market Cap' in stock_info.columns:
            market_caps = stock_info['Market Cap']
            df['market_cap'] = market_caps.tolist()
        else:
            # If 'Market Cap' is not found, set a default value or handle it accordingly
            df['market_cap'] = None
            print("No 'Market Cap' data found.")

    except yf.exceptions.YFinanceError as yfe:
        print(f"Error fetching data from Yahoo Finance: {yfe}")
    except yf.exceptions.NotFoundError as nfe:
        print(f"Symbol not found or may be delisted: {nfe}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return df
