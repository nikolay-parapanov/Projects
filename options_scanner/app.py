from flask import Flask, render_template, url_for, send_file, redirect
from shortable_stocks import ss_options_scan
app = Flask(__name__)



@app.route('/ss_options')
def shortable_stocks_ss_options():
    ss_options_scan.ss_login_and_options_scan()
    return render_template('shortable_stocks_options.html')