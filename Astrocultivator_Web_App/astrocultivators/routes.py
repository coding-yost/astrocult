from flask import render_template, url_for, flash, redirect
# import pandas as pd
from astrocultivators import app

# df = pd.read_csv('csv/test_seconds.csv')

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

# @app.route("/csv")
# def csv():
#     df_html = df.to_html()
#     return render_template('csv.html', data=df_html)