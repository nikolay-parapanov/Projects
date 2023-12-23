from flask import Flask, render_template, url_for
import step_2_adding_preselected_patterns_from_talib, check_for_setups, step_1_data_collection, step_3_last_data, patterns, test, \
    filter_setups, visualization

app = Flask(__name__)


@app.route('/')
@app.route('/home')
@app.route('/index')
def index():

    return render_template('index.html')


@app.route('/general_daily_scanner')
def general_daily_scanner_route():

    # This procedure is to perform all of the daily scanning activities at one page (incl. visualization at the end):

    data_collection.data_collection_daily()
    adding_preselected_patterns_from_talib.adding_preselected_patterns_to_df_from_ta_lib()
    last_data.last_day_data()
    check_for_setups.check_for_setups_in_last_days()
    filter_setups.filter_setups_for_summary()
    details = visualization.visualize_predefined_dataframe()

    return render_template('general_daily_scanner.html', details=details)




@app.route('/collect_data')
def snapshot():
    collected = data_collection_daily.data_collection_daily()
    print('data collected')
    return collected


@app.route('/enrich_data')
def enrich_data():
    adding_preselected_patterns_from_talib.adding_preselected_patterns_to_df_from_ta_lib()

    return 'data enriched'


@app.route('/last_day_data')
def last_day():
    last_day_data.last_day_data()

    return 'last day data filtered'


@app.route('/check_for_setups')
def check():
    check_for_setups.check_for_setups_in_last_days()

    return 'check for setups has been done'


@app.route('/test')
def test1():
    test.test_code()

    return 'test code'


@app.route('/filter')
def filter_setups1():
    filter_setups.filter_setups_for_summary()

    return 'filtered setups'


@app.route('/visualize')
def visualize1():

    details = visualization.visualize_predefined_dataframe()

    # return 'viz'
    return render_template('general_daily_scanner.html', details=details)
