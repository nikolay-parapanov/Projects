from flask import Flask, render_template, url_for, send_file, redirect
from shortable_stocks import ss_options_scan_NOV, ss_options_scan_NOA, ss_options_scan_OVL, ss_options_scan_HIV

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