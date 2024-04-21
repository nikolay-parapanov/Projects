from flask import Flask, render_template, url_for, send_file, redirect
import daily_step_2_adding_preselected_patterns_from_talib, daily_step_4_check_for_setups, \
    daily_step_3_last_data, test, \
    daily_step_5_filter_setups, daily_step_6_visualization
import general_functions.get_last_modified_date_and_time_of_file as gf_date_time
import general_functions.import_data_as_list_from_csv_file as gf_import_list
import rsi_indicator.rsi_indicator_data_retrieve as rsi_dr
import rsi_indicator.rsi_indicator_main as rsi_main
import shortable_stocks.shortable_stocks_fisher_heikin
import symbol_analysis
from shortable_stocks import shortable_stocks_data_retrieve as ss

app = Flask(__name__)

@app.route('/')
@app.route('/home')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/shortable_stocks')
def shortable_stocks_home_page_main():
    file_path = 'database/shortable_stocks/shortable_stocks_initial_screener_db.csv'
    formatted_modification_time = gf_date_time.get_last_modified_date_and_time_of_file_code(file_path)
    fisher_list, heikin_ashi_uptrends, heikin_ashi_downtrends, len_fl, len_hau, len_had, len_cfh, cross_fisher_heikin = shortable_stocks.shortable_stocks_fisher_heikin.shortable_data_fisher_heikin_code()

    return render_template('shortable_stocks.html',
                           date_of_shortable_stocks_last_retrieve = formatted_modification_time,
                           fl = fisher_list,
                           hau= heikin_ashi_uptrends,
                           had = heikin_ashi_downtrends,
                           len_fl= len_fl, len_hau = len_hau, len_had= len_had, len_cfh= len_cfh,
                           cross_fisher_heikin = cross_fisher_heikin )

@app.route('/shortable_stocks/data_retrieve')
def shortable_stocks_data_retrieve_main():
    ss.ss_data_retrieve_code()

    return redirect(url_for('shortable_stocks_home_page_main'))


@app.route('/rsi_indicator')
def rsi_indicator_main():
    file_path1 = 'database/daily/rsi/step_1_-_all_symbols_daily_initial_finviz_2200.csv'
    file_path2 = 'database/daily/rsi/step_2_-_all_symbols_daily_finviz_2200_rsi_added_last_8_rows.csv'
    file_path3 = 'database/daily/rsi/step_3_-_rsi_final_filter_as_list.csv'

    formatted_modification_time_market_data = gf_date_time.get_last_modified_date_and_time_of_file_code(file_path1)
    formatted_modification_time_rsi_calcs = gf_date_time.get_last_modified_date_and_time_of_file_code(file_path2)
    formatted_modification_rsi_results = gf_date_time.get_last_modified_date_and_time_of_file_code(
        file_path3)
    result_list = []
    try:
        result_list = gf_import_list.import_data_as_list_from_csv_file_code(file_path3)
        if not result_list:
            print("The imported list is empty.")
        else:
            # Process the non-empty list
            print("Successfully imported data:", result_list)
    except Exception as e:
            print("An error occurred:", e)
            # Handle the exception as needed

    return render_template('rsi_indicator.html',
                           rsi_indicator_last_retrieved_market_data=formatted_modification_time_market_data,
                           rsi_calcs_last_data = formatted_modification_time_rsi_calcs,
                           resi_results_last_data = formatted_modification_rsi_results,
                           result_list = result_list)

@app.route('/rsi_indicator/data_retrieve')
def rsi_indicator_data_retrieve_main():

    rsi_dr.rsi_indicator_data_retrieve_code()
    return redirect(url_for('rsi_indicator_main'))

@app.route('/rsi_indicator/recalculate_rsi_data')
def rsi_indicator_recalculation_main():

    rsi_main.rsi_indicator_code()
    return redirect(url_for('rsi_indicator_main'))

@app.route('/ticker/<ticker>')
def scanner_for_specific_symbol(ticker):

    img_candlestick = symbol_analysis.individual_symbol_analysis(ticker)

    return send_file(img_candlestick, mimetype='image/png')

@app.route('/spy_scanner')
def general_daily_scanner_route_main():
    # This procedure is to perform all of the daily scanning activities at one page (incl. visualization at the end):

    daily_step_1_data_collection.data_collection_daily()
    # daily_step_2_adding_preselected_patterns_from_talib.adding_preselected_patterns_to_df_from_ta_lib()
    # daily_step_3_last_data.last_day_data()
    # daily_step_4_check_for_setups.check_for_setups_in_last_days()
    # daily_step_5_filter_setups.filter_setups_for_summary()
    details = daily_step_6_visualization.visualize_predefined_dataframe()

    return render_template('general_daily_scanner.html', details=details)

@app.route('/ticker_general/')
def individual_scanner_general():

    return render_template('single_ticker_scanner_general.html')

@app.route('/collect_data')
def snapshot():
    collected = daily_step_1_data_collection.data_collection_daily()
    print('data collected')
    return collected


@app.route('/enrich_data')
def enrich_data():
    daily_step_2_adding_preselected_patterns_from_talib.adding_preselected_patterns_to_df_from_ta_lib()

    return 'data enriched'


@app.route('/last_day_data')
def last_day():
    daily_step_3_last_data.last_day_data()

    return 'last day data filtered'


@app.route('/check_for_setups')
def check():
    daily_step_4_check_for_setups.check_for_setups_in_last_days()

    return 'check for setups has been done'


@app.route('/filter')
def filter_setups1():
    daily_step_5_filter_setups.filter_setups_for_summary()

    return 'filtered setups'


@app.route('/visualize')
def visualize1():
    details = daily_step_6_visualization.visualize_predefined_dataframe()

    # return 'viz'
    return render_template('general_daily_scanner.html', details=details)


@app.route('/test')
def test1():
    test.test_code()

    return 'test code'
