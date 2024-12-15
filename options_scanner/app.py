import os

import pandas as pd
from flask import Flask, render_template, url_for, send_file, redirect

import patterns_scan.rsi_divergence_formulas
from general.filter_noa_calls import filter_noa_calls_details
from general.filter_noa_puts import filter_noa_puts_details
from shortable_stocks import ss_options_scan_NOV, ss_options_scan_NOA, ss_options_scan_OVL, ss_options_scan_HIV
from general import pivot_generation_noa_calls, filter_noa_calls, pivot_generation_ovl
from individual_stock_analysis_code import generate_strike_prices_data, generate_strike_prices_individual_ticker, generate_strike_prices_data_pivot_for_current_date_by_hour_individual_ticker
from current_day_scan_code import current_day_scan_live
from patterns_scan import yf_retrieve_period_60_daily, signals_scan, yf_retrieve_period_custom_last_cut_custom, data_enrichment, rsi_divergence_formulas_pre_signal


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


@app.route('/generate_ss_pivots')
def general_function_generate_ss_pivots():
    pivot_generation_noa_calls.generate_pivot()
    filter_noa_calls.filter_noa_calls_details()
    pivot_generation_ovl.generate_pivot()

    return render_template('index.html')


@app.route('/render_noa_pivot_filtered_calls')
def generate_noa_pivot_filtered_calls():
    unique_tickers_calls, filtered_df_calls = filter_noa_calls_details()
    unique_tickers_puts, filtered_df_puts = filter_noa_puts_details()

    # Convert DataFrame to HTML table
    table_calls_html = filtered_df_calls.to_html(classes='table table-striped', index=False)
    table_puts_html = filtered_df_puts.to_html(classes='table table-striped', index=False)

    # Get unique tickers
    print(unique_tickers_calls)
    print(unique_tickers_puts)

    return render_template('index.html', tickers_calls=unique_tickers_calls, table_calls=table_calls_html, tickers_puts=unique_tickers_puts, table_puts=table_puts_html )
@app.route('/render_noa_pivot_filtered_puts')
def generate_noa_pivot_filtered_puts():
    unique_tickers_puts, filtered_df_puts = filter_noa_puts_details()

    # Convert DataFrame to HTML table
    table_puts_html = filtered_df_puts.to_html(classes='table table-striped', index=False)

    # Get unique tickers
    print(unique_tickers_puts)

    return render_template('index.html', tickers_puts=unique_tickers_puts, table_puts=table_puts_html )


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
    df = generate_strike_prices_individual_ticker.generate_strike_prices_data_pivot_for_individual_ticker(
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

@app.route('/current_day_scan')
def current_day_quick_hourly_scan_main():

    df = current_day_scan_live.current_day_scan_live()

    # Convert DataFrame to HTML table
    table_time_html = df.to_html(classes='table table-striped', index=False)

    return render_template('current_day_scan.html', table_time=table_time_html)


@app.route('/yf_retrieve_period_60_daily')
def yf_retrieve_period_60_daily_main():

    yf_retrieve_period_60_daily.data_retrieval_daily()

    return render_template('index.html')


@app.route('/yf_retrieve_custom')
def yf_retrieve_period_custom_main():
    # periods: "1y" , "1mo" ,
    # intervals: "1d", "30m" , "15m"

    csv_file_path = r'C:\Users\npara\coding\np-github\Projects\options_scanner\rsi_divergence_files\tickers_list_finviz_beta.csv'  # Replace with the path to your CSV file
    df = pd.read_csv(csv_file_path)
    tickers_list_option = df['Ticker'].tolist()
    print("Updated list for retrieve from latest finviz-beta file")
    output_file = 'step1_retrieve_finviz_beta.csv'

    period = "1mo"
    interval = "30m"
    cut_last = 120
    yf_retrieve_period_custom_last_cut_custom.data_retrieval_period_custom_last_cut_custom(period, interval, cut_last, tickers_list_option, output_file)

    return render_template('rsi_divergence_general.html')

@app.route('/yf_retrieve_options_favourites')
def yf_retrieve_period_options_favourites_main():
    # periods: "1y" , "1mo" ,
    # intervals: "1d", "30m" , "15m"

    csv_file_path = r'C:\Users\npara\coding\np-github\Projects\options_scanner\rsi_divergence_files\tickers_list_options_favourites.csv'  # Replace with the path to your CSV file
    df = pd.read_csv(csv_file_path)
    tickers_list_option = df['Ticker'].tolist()
    print("Updated list for retrieve from options favourites file")
    output_file = 'step1_retrieve_options_favourites.csv'
    period = "3mo"
    interval = "1h"
    cut_last = 120
    yf_retrieve_period_custom_last_cut_custom.data_retrieval_period_custom_last_cut_custom(period, interval, cut_last, tickers_list_option, output_file)

    return render_template('rsi_divergence_general.html')

@app.route('/rsi_divergence_calculate_custom_table')
def rsi_divergence_calculate_custom_table():

    # calculation of table based on custom retrieve
    input_file = 'custom'
    patterns_scan.rsi_divergence_formulas.rsi_divergence_formulas_calcs(input_file)
    patterns_scan.rsi_divergence_formulas_pre_signal.rsi_divergence_formulas_calcs_pre_signal(input_file)

    return render_template('rsi_divergence_general.html')

@app.route('/rsi_divergence_calculate_options_favourites_table')
def rsi_divergence_calculate_options_favourites_table():

    # calculation of table based on options_favourites retrieve
    input_file = 'options_favourites'
    patterns_scan.rsi_divergence_formulas.rsi_divergence_formulas_calcs(input_file)
    patterns_scan.rsi_divergence_formulas_pre_signal.rsi_divergence_formulas_calcs_pre_signal(input_file)
    return render_template('rsi_divergence_general.html')

@app.route('/rsi_divergence_enrich_split_tables_custom')
def rsi_enrichment_and_days_split_custom():
    input_file = r'C:\Users\npara\coding\np-github\Projects\options_scanner\rsi_divergence_files\step3_result_filtered_finviz_beta.csv'
    output_file = r'C:\Users\npara\coding\np-github\Projects\options_scanner\rsi_divergence_files\step4_result_filtered_finviz_beta.csv'

    patterns_scan.data_enrichment.rsi_divergence_signals_cut_by_day(input_file, output_file)

    return render_template('rsi_divergence_general.html')

@app.route('/rsi_divergence_enrich_split_tables_custom_pre_signal')
def rsi_enrichment_and_days_split_custom_pre_signal():
    input_file = r'C:\Users\npara\coding\np-github\Projects\options_scanner\rsi_divergence_files\step3_result_filtered_finviz_beta_pre-signal.csv'
    output_file = r'C:\Users\npara\coding\np-github\Projects\options_scanner\rsi_divergence_files\step4_result_filtered_finviz_beta_pre-signal.csv'

    patterns_scan.data_enrichment.rsi_divergence_signals_cut_by_day(input_file, output_file)

    return render_template('rsi_divergence_general.html')

@app.route('/rsi_divergence_enrich_split_tables_options_favourites')
def rsi_enrichment_and_days_split_options_favourites():
    input_file = r'C:\Users\npara\coding\np-github\Projects\options_scanner\rsi_divergence_files\step3_result_filtered_options_favourites.csv'
    output_file = r'C:\Users\npara\coding\np-github\Projects\options_scanner\rsi_divergence_files\step4_result_filtered_options_favourites.csv'

    patterns_scan.data_enrichment.rsi_divergence_signals_cut_by_day(input_file, output_file)

    return render_template('rsi_divergence_general.html')
@app.route('/rsi_divergence_enrich_split_tables_options_favourites_pre_signal')
def rsi_enrichment_and_days_split_options_favourites_pre_signal():
    input_file = r'C:\Users\npara\coding\np-github\Projects\options_scanner\rsi_divergence_files\step3_result_filtered_options_favourites_pre-signal.csv'
    output_file = r'C:\Users\npara\coding\np-github\Projects\options_scanner\rsi_divergence_files\step4_result_filtered_options_favourites_pre-signal.csv'

    patterns_scan.data_enrichment.rsi_divergence_signals_cut_by_day(input_file, output_file)

    return render_template('rsi_divergence_general.html')

@app.route('/generate_tables_from_rsi_divergence_scan_custom')
def rsi_divergence_table_rendering_custom():
    df_last_day_regular = pd.read_csv(r'C:\Users\npara\coding\np-github\Projects\options_scanner\rsi_divergence_files\step4_result_filtered_finviz_beta.csv')
    print("OPening step4_result_filtered_finviz_beta file ..")

    df_last_day_regular = df_last_day_regular.drop(columns=['Unnamed: 0'])

    table_rsi_divergence_last_day_regular_html = df_last_day_regular.to_html(classes='table table-striped', index=False)

    df_last_day_pre_signal = pd.read_csv(r'C:\Users\npara\coding\np-github\Projects\options_scanner\rsi_divergence_files\step4_result_filtered_finviz_beta_pre-signal.csv')
    print("OPening step4_result_filtered_options_favourites_pre-signal file ..")

    df_last_day_pre_signal = df_last_day_pre_signal.drop(columns=['Unnamed: 0'])

    table_rsi_divergence_last_day_pre_signal_html = df_last_day_pre_signal.to_html(classes='table table-striped', index=False)


    return render_template('rsi_divergence_general.html', table_rsi_divergence_last_day_regular_html=table_rsi_divergence_last_day_regular_html,table_rsi_divergence_last_day_pre_signal_html=table_rsi_divergence_last_day_pre_signal_html)


@app.route('/generate_tables_from_rsi_divergence_scan_options_favourites')
def rsi_divergence_table_rendering_options_favourites():
    df_last_day_regular = pd.read_csv(r'C:\Users\npara\coding\np-github\Projects\options_scanner\rsi_divergence_files\step4_result_filtered_options_favourites.csv')
    print("OPening step4_result_filtered_options_favourites file ..")

    df_last_day_regular = df_last_day_regular.drop(columns=['Unnamed: 0'])

    table_rsi_divergence_last_day_regular_html = df_last_day_regular.to_html(classes='table table-striped', index=False)

    df_last_day_pre_signal = pd.read_csv(r'C:\Users\npara\coding\np-github\Projects\options_scanner\rsi_divergence_files\step4_result_filtered_options_favourites_pre-signal.csv')
    print("OPening step4_result_filtered_options_favourites_pre-signal file ..")

    df_last_day_pre_signal = df_last_day_pre_signal.drop(columns=['Unnamed: 0'])

    table_rsi_divergence_last_day_pre_signal_html = df_last_day_pre_signal.to_html(classes='table table-striped', index=False)


    return render_template('rsi_divergence_general.html', table_rsi_divergence_last_day_regular_html=table_rsi_divergence_last_day_regular_html,table_rsi_divergence_last_day_pre_signal_html=table_rsi_divergence_last_day_pre_signal_html)


@app.route('/generate_charts')
def signals_scan_main():
    signals_scan.signals_extraction()
    # Get a list of chart images from the static/charts folder
    charts_folder = os.path.join('static', 'charts')
    charts = [f for f in os.listdir(charts_folder) if f.endswith('.png')]

    # Render the charts in the index.html template
    return render_template('generate_charts.html', charts=charts)
