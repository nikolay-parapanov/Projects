import pandas as pd
from flask import Flask, render_template, url_for, send_file, redirect

from general.filter_noa_calls import filter_noa_calls_details
from shortable_stocks import ss_options_scan_NOV, ss_options_scan_NOA, ss_options_scan_OVL, ss_options_scan_HIV
from general import pivot_generation_noa_calls, filter_noa_calls
from individual_stock_analysis_code import generate_strike_prices_data, generate_strike_prices_individual_ticker, generate_strike_prices_data_pivot_for_current_date_by_hour_individual_ticker

app = Flask(__name__)


@app.route('/')
@app.route('/home')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/ss_notable_options_volume')
def shortable_stocks_ss_options_NOV():
    ss_options_scan_NOV.ss_login_and_options_scan()
    return render_template('index.html')


@app.route('/ss_notable_options_activity')
def shortable_stocks_ss_options_NOA():
    ss_options_scan_NOA.ss_login_and_options_scan()
    return render_template('index.html')


@app.route('/ss_options_volume_leaders')
def shortable_stocks_ss_options_OVL():
    ss_options_scan_OVL.ss_login_and_options_scan()
    return render_template('index.html')


@app.route('/ss_highest_implied_volatility')
def shortable_stocks_ss_options_HIV():
    ss_options_scan_HIV.ss_login_and_options_scan()
    return render_template('index.html')


@app.route('/generate_noa_pivot')
def general_function_generate_noa_pivot():
    pivot_generation_noa_calls.generate_pivot()
    filter_noa_calls.filter_noa_calls_details()

    return render_template('index.html')


@app.route('/render_noa_pivot_filtered')
def generate_noa_pivot_filtered():
    unique_tickers, filtered_df_01 = filter_noa_calls_details()

    # Convert DataFrame to HTML table
    table_html = filtered_df_01.to_html(classes='table table-striped', index=False)

    # Get unique tickers
    print(unique_tickers)
    print(type(unique_tickers))

    return render_template('index.html', tickers=unique_tickers, table=table_html)


@app.route('/individual_analysis')
def individual_analysis_all_tickers_main():
    generate_strike_prices_data.generate_strike_prices_data_pivot_for_all_tickers()

    raw_file_df = 'individual_analysis_results/strike_prices_for_all_tickers.csv'
    tickers_df_strike_prices = pd.read_csv(raw_file_df)

    unique_tickers_file = 'individual_analysis_results/result_tickers_sorted_filtered_calls_all_tickers.csv'
    # Read unique tickers from the unique_tickers_file
    unique_tickers_df = pd.read_csv(unique_tickers_file, header=None)

    # Convert the first (and only) column to a list skipping first value as it is zero (probably index from previous iterations)
    unique_tickers_list = unique_tickers_df.iloc[:, 0].tolist()

    # Convert DataFrame to HTML table
    table_html = tickers_df_strike_prices.to_html(classes='table table-striped', index=False)



    return render_template('individual_analysis.html', tickers=unique_tickers_list, table=table_html)


@app.route('/individual_analysis/<individual_ticker>')
def individual_analysis_individual_ticker_main(individual_ticker):
    df, individual_ticker = generate_strike_prices_individual_ticker.generate_strike_prices_data_pivot_for_individual_ticker(
        individual_ticker)

    unique_tickers_file = 'individual_analysis_results/result_tickers_sorted_filtered_calls_all_tickers.csv'

    # Read unique tickers from the unique_tickers_file
    unique_tickers_df = pd.read_csv(unique_tickers_file, header=None)

    # Convert the first (and only) column to a list skipping first value as it is zero (probably index from previous iterations)
    unique_tickers_list = unique_tickers_df.iloc[:, 0].tolist()

    # Convert DataFrame to HTML table
    table_html = df.to_html(classes='table table-striped', index=False)

    time_table_df = generate_strike_prices_data_pivot_for_current_date_by_hour_individual_ticker.generate_strike_prices_data_pivot_for_individual_ticker_current_date_by_hour(individual_ticker)

    table_time_html = time_table_df.to_html(classes='table table-striped', index=False)

    return render_template('individual_analysis.html', tickers=unique_tickers_list, table=table_html, table_time=table_time_html,
                           individual_ticker=individual_ticker)
