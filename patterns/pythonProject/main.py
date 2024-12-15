import signals_extraction
import signals_to_charts
import yfinance_retrieve_for_signals

if __name__ == '__main__':

    # tickers_with_signals_list = signals_extraction.signals_extraction()
    tickers_with_signals_list = ['a', 'aapl', 'roku', 'm', 'aal']
    signals_combined_df = yfinance_retrieve_for_signals.retrieves_for_signals(tickers_with_signals_list)
    signals_combined_df.to_csv('test_signals_combined_df.csv', index=True)
    print("signals combined df:")
    print(signals_combined_df)

    signals_to_charts.visualize_signals(signals_combined_df)
    # print(signals_combined_df)

    print('the end :)')
