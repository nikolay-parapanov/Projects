from flask import Flask, render_template, request
import pandas as pd
import yfinance as yf
import datetime as dt

from patterns import patterns
from data_collection_daily import data_collection_daily



app = Flask(__name__)

@app.route('/')
def index():

    pattern = request.args.get('pattern', None)
    df = pd.read_csv('database/daily/all_symbols_daily.csv')
    print(df)

    return render_template('index.html', patterns=patterns)


@app.route('/snapshot')
def snapshot():

   data_collection_daily()

   return 'snapshot executed'