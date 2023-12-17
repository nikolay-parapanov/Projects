from flask import Flask, render_template, request
from patterns import patterns
from data_collection_daily import data_collection_daily

app = Flask(__name__)

@app.route('/')
def index():
    pattern = request.args.get('pattern', None)
    return render_template('index.html', patterns=patterns)


@app.route('/snapshot')
def snapshot():

   data_collection_daily()

   return 'snapshot executed'