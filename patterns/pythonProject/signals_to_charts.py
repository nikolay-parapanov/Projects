import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf
from PIL import Image


def combine_images(filenames):
    images = [Image.open(filename) for filename in filenames]

    # Get the maximum width and total height of the images
    max_width = max(image.width for image in images)
    total_height = sum(image.height for image in images)

    # Create a new image with the maximum width and total height
    combined_image = Image.new('RGB', (max_width, total_height))

    # Paste each image into the new image
    y_offset = 0
    for image in images:
        combined_image.paste(image, (0, y_offset))  # Paste at (0, y_offset)
        y_offset += image.height  # Increment y_offset by the height of the current image

    # Save the combined image
    combined_image.save('combined_candlestick_charts.png')


def visualize_signals(combined_df_signals):

    df = combined_df_signals

    # Check if 'Date' is the index
    df.reset_index(inplace=True)  # This will convert the index back to a column

    # List to hold filenames for combining later
    filenames = []

    # Iterate through each unique ticker
    unique_tickers = df['Ticker'].unique()

    for ticker in unique_tickers:
        # Filter the DataFrame for the current ticker
        ticker_data = df[df['Ticker'] == ticker]

        # Set 'Date' as the index for mplfinance
        ticker_data.set_index('Date', inplace=True)

        # Create the candlestick chart with volume
        apds = [mpf.make_addplot(ticker_data['Avg_Volume_10'], panel=1, color='black', width=1, label='Avg Volume')]


        # File name for the candlestick chart
        filename = f'{ticker}_candlestick_chart.png'
        filenames.append(filename)

        # Plot the candlestick chart with custom volume colors
        mpf.plot(ticker_data, type='candle', volume=True,
                 title=f'{ticker} Candlestick Chart',
                 ylabel='Price', ylabel_lower='Volume',
                 style='charles',
                 addplot=apds,  # Add the average volume line
                 savefig=f'{ticker}_candlestick_chart.png',
                 figratio=(12, 8),
                 figscale=1.2,
                 tight_layout=True)

        # Combine all images into one
        combine_images(filenames)

        # Plot the 'Close' price
        # plt.plot(ticker_data['Date'], ticker_data['Close'], label='Close Price', color='blue')
        #
        # # Optional: You can plot other lines, such as SMA or volume
        # if 'SMA_20' in ticker_data.columns:
        #     plt.plot(ticker_data['Date'], ticker_data['SMA_20'], label='SMA 20', color='orange')
        # if 'SMA_50' in ticker_data.columns:
        #     plt.plot(ticker_data['Date'], ticker_data['SMA_50'], label='SMA 50', color='green')
        #
        # # Customize the plot
        # plt.title(f'{ticker} Price Chart')
        # plt.xlabel('Date')
        # plt.ylabel('Price')
        # plt.legend()
        # plt.xticks(rotation=45)  # Rotate x-axis labels for better visibility
        # plt.grid()

