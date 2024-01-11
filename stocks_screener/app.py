import io
from PIL import Image
from flask import Flask, render_template, url_for, send_file
import daily_step_1_data_collection, daily_step_2_adding_preselected_patterns_from_talib, daily_step_4_check_for_setups, \
    daily_step_1_data_collection, daily_step_3_last_data, patterns, test, \
    daily_step_5_filter_setups, daily_step_6_visualization
import symbol_analysis

app = Flask(__name__)


@app.route('/')
@app.route('/home')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/spy_scanner')
def general_daily_scanner_route():
    # This procedure is to perform all of the daily scanning activities at one page (incl. visualization at the end):

    daily_step_1_data_collection.data_collection_daily()
    # daily_step_2_adding_preselected_patterns_from_talib.adding_preselected_patterns_to_df_from_ta_lib()
    # daily_step_3_last_data.last_day_data()
    # daily_step_4_check_for_setups.check_for_setups_in_last_days()
    # daily_step_5_filter_setups.filter_setups_for_summary()
    details = daily_step_6_visualization.visualize_predefined_dataframe()

    return render_template('general_daily_scanner.html', details=details)


@app.route('/ticker/<ticker>')
def scanner_for_specific_symbol(ticker):

    img_candlestick = symbol_analysis.individual_symbol_analysis(ticker)

    return send_file(img_candlestick, mimetype='image/png')

@app.route('/ss')
def short():
    soup = shortablestocks.connect_to_site()

    return render_template('ss.html', details = soup)

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
