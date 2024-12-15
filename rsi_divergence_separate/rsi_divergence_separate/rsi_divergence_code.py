import os
import mplfinance as mpf
import pandas as pd
import openpyxl
import matplotlib
from matplotlib import pyplot as plt
from matplotlib.pyplot import axes
import matplotlib.dates as mdates


matplotlib.use('Agg')  # Use the non-interactive backend to avoid GUI issues

filenames = []
file_path_model = r'C:\Users\npara\coding\np-github\Projects\rsi_divergence_separate\rsi_divergence_separate\excel_model\excel_model.xlsx'

# Delete old PNG files in the output directory
print('Deleting all previous charts in the static/charts folder ..')

# Directory for saving PNG files
output_dir = r'C:\Users\npara\coding\np-github\Projects\rsi_divergence_separate\rsi_divergence_separate\charts'

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Delete all old PNG files in the output directory
for filename in os.listdir(output_dir):
    if filename.endswith('.png'):
        file_path = os.path.join(output_dir, filename)
        try:
            os.remove(file_path)
            print(f'Deleted old file: {filename}')
        except Exception as e:
            print(f'Error deleting file {filename}: {e}')

print('Reading dataframe: ......')

# Read Excel file directly
df = pd.read_excel(file_path_model)

print('Dataframe loaded!')
print(df.head())  # Print first few rows for verification

# Convert 'Datetime' to a datetime format, removing timezone if not needed
df['Datetime'] = pd.to_datetime(df['Datetime'], errors='coerce').dt.tz_localize(None)

# Set 'Datetime' as the index
df.set_index('Datetime', inplace=True)

print(df.head())

# Filter DataFrame for signals
filtered_df_with_tickers_signal_buy = df[df['last'].str.contains("Buy", na=False, case=False)].copy()
filtered_df_with_tickers_signal_sell = df[df['last'].str.contains("Sell", na=False, case=False)].copy()

tickers_with_signal_buy_list = filtered_df_with_tickers_signal_buy['ticker'].unique().tolist()
tickers_with_signal_sell_list = filtered_df_with_tickers_signal_sell['ticker'].unique().tolist()

print('Buy list: ')
print(tickers_with_signal_buy_list)

print('Sell list: ')
print(tickers_with_signal_sell_list)

numeric_columns = ['Open', 'High', 'Low', 'Close', 'Volume', 'avg_volume_10', 'rsi', 'sma_20', 'sma_50', 'sma_200',
                   'desc_number', 'previous_day_max', 'previous_day_min', 'rsi_peak_rsi_value', 'rsi_peak_high_value',
                   'rsi_bottom_rsi_value', 'rsi_bottom_low_value', 'be_current_rsi_less_than_peak',
                   'be_current_price_close_above_rsi_peak', 'be_pre_signal_1', 'be_pre_signal_last_10',
                   'be_pre_signal_2', 'bu_current_rsi_more_than_bottom', 'bu_current_price_close_above_rsi_peak',
                   'bu_pre_signal_1', 'bu_pre_signal_last_10', 'bu_pre_signal_2', 'price_above_65_sma']

# Ensure columns exist in DataFrame
for column in numeric_columns:
    if column in df.columns:
        df.loc[:, column] = pd.to_numeric(df[column], errors='coerce')
    else:
        print(f"Warning: {column} not found in DataFrame")

for ticker in tickers_with_signal_buy_list:
    ticker_data = df[df['ticker'] == ticker].copy()

    if 'Datetime' in ticker_data.columns:
        ticker_data['Datetime'] = pd.to_datetime(ticker_data['Datetime'], errors='coerce')
        ticker_data.set_index('Datetime', inplace=True)

    ticker_data[numeric_columns] = ticker_data[numeric_columns].apply(pd.to_numeric, errors='coerce')

    # Identify buy signal indices based on the 'last' column
    buy_signal_data = ticker_data[ticker_data['last'] == "Buy"]  # Filter rows where last is "Buy"

    # Ensure 'last' column contains string values and check for unique values
    print(f"Unique values in 'last' for {ticker}: {ticker_data['last'].unique()}")

    # Get the closing prices for those indices
    buy_signal_prices = buy_signal_data['Close']

    # Debug: Print buy signal prices
    print(f'Ticker: {ticker}, Buy signal prices: {buy_signal_prices}')

    addplots = []

    previous_day_max_value = ticker_data['previous_day_max'].iloc[-1]
    previous_day_max_line = mpf.make_addplot([previous_day_max_value] * len(ticker_data), color='green',
                                                 linestyle='--', width=1, label='previous_day_max')

    avg_volume_line = mpf.make_addplot(ticker_data['avg_volume_10'], panel=1, color='black', width=1,
                                       label='Avg Volume')
    rsi_line = mpf.make_addplot(ticker_data['rsi'], panel=2, color='blue', width=1, label='RSI')
    sma_20_line = mpf.make_addplot(ticker_data['sma_20'], color='green', width=1, label='sma_20')
    sma_50_line = mpf.make_addplot(ticker_data['sma_50'], color='orange', width=1, label='sma_50')
    sma_200_line = mpf.make_addplot(ticker_data['sma_200'], color='red', width=1, label='sma_200')
    sma_65_line = mpf.make_addplot(ticker_data['sma_65'], color='black', width=2, label='sma_65')

    # Add previous day max and other indicators to addplots
    addplots.extend([previous_day_max_line, avg_volume_line, rsi_line, sma_20_line, sma_50_line, sma_200_line, sma_65_line])

    # Create filename for saving chart
    filename = os.path.join(output_dir, f'{ticker}_candlestick_chart.png')
    filenames.append(filename)

    print(f'Plotting for ticker: {ticker}')

    # Plot the candlestick chart
    try:
        # Use returnfig=True to capture the figure and axes
        fig, axes = mpf.plot(ticker_data, type='candle', volume=True,
                             title=f'{ticker} Candlestick Chart',
                             ylabel='Price', ylabel_lower='Volume',
                             style='charles',
                             addplot=addplots,
                             savefig=filename,
                             figratio=(12, 8),
                             figscale=1.2,
                             tight_layout=True,
                             returnfig=True)  # Ensure to return the figure and axes

        # Customize x-axis
        ax = axes[0]  # Get the main axes for the candlestick chart
        ax.xaxis.set_major_locator(mdates.DayLocator(interval=1))  # Set interval for ticks (every 5 days)
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))  # Format the date

        plt.setp(ax.xaxis.get_majorticklabels(), rotation=90, ha='right')  # Rotate x-axis labels for better readability

        # Optional: Set minor ticks for better granularity (e.g., every day)
        ax.xaxis.set_minor_locator(mdates.DayLocator())

        # Show grid for better readability (optional)
        ax.grid(True)

        plt.show()  # Optionally show the plot if running interactively
        print("Charts are generated")
    except ValueError as e:
        print(f"Error plotting for {ticker}: {e}")

    print("Charts are generated")
