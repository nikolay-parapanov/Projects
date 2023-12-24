from flask import Flask, render_template, url_for
import step_1_data_collection , step_2_adding_preselected_patterns_from_talib, step_4_check_for_setups, step_1_data_collection, step_3_last_data, patterns, test, \
    step_5_filter_setups, step_6_visualization

app = Flask(__name__)


@app.route('/')
@app.route('/home')
@app.route('/index')
def index():

    return render_template('index.html')

@app.route('/general_daily_scanner')
def general_daily_scanner_route():

    # This procedure is to perform all of the daily scanning activities at one page (incl. visualization at the end):

    step_1_data_collection.data_collection_daily()
    step_2_adding_preselected_patterns_from_talib.adding_preselected_patterns_to_df_from_ta_lib()
    step_3_last_data.last_day_data()
    step_4_check_for_setups.check_for_setups_in_last_days()
    step_5_filter_setups.filter_setups_for_summary()
    details = step_6_visualization.visualize_predefined_dataframe()

    return render_template('general_daily_scanner.html', details=details)


@app.route('/symbol/')
def scanner_for_specific_symbol():


    return

@app.route('/collect_data')
def snapshot():
    collected = step_1_data_collection.data_collection_daily()
    print('data collected')
    return collected


@app.route('/enrich_data')
def enrich_data():
    step_2_adding_preselected_patterns_from_talib.adding_preselected_patterns_to_df_from_ta_lib()

    return 'data enriched'


@app.route('/last_day_data')
def last_day():
    step_3_last_data.last_day_data()

    return 'last day data filtered'


@app.route('/check_for_setups')
def check():
    step_4_check_for_setups.check_for_setups_in_last_days()

    return 'check for setups has been done'


@app.route('/filter')
def filter_setups1():
    step_5_filter_setups.filter_setups_for_summary()

    return 'filtered setups'


@app.route('/visualize')
def visualize1():

    details = step_6_visualization.visualize_predefined_dataframe()

    # return 'viz'
    return render_template('general_daily_scanner.html', details=details)




@app.route('/test')
def test1():
    test.test_code()

    return 'test code'
