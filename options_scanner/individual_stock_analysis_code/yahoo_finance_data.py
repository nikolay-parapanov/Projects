import pandas as pd
import yfinance as yf


def get_tickers_prices(ticker_symbols):
    data = []
    for ticker_symbol in ticker_symbols:
        try:
            ticker = yf.Ticker(ticker_symbol)
            current_price = ticker.history(period='1d')['Close'].iloc[-1]
            data.append((ticker_symbol, current_price))
        except Exception as e:
            print(f"Error fetching data for {ticker_symbol}: {e}")
            data.append((ticker_symbol, None))
    df = pd.DataFrame(data, columns=['Stock Symbol', 'Current Price'])
    return df