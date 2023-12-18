from flask import Flask, render_template, request
import adding_preselected_patterns_from_talib
from patterns import patterns
from data_collection_daily import data_collection_daily
import last_day_data


app = Flask(__name__)

@app.route('/')
def index():

    # pattern = request.args.get('pattern', None)

    return render_template('index.html', patterns=patterns)


@app.route('/collect_data')
def snapshot():

   collected = data_collection_daily()
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