from flask import render_template, url_for, send_from_directory, send_file, flash, redirect
from astrocultivators import app

# imports for charts
from matplotlib.figure import Figure
import base64 
from io import BytesIO
import pandas as pd
from sensor_figure import get_figure

@app.route("/")
@app.route("/home")
def home():

    fig = get_figure()
    # save to a buffer
    buf = BytesIO()
    fig.savefig(buf, format="png")

    # Embed saved fig in html output
    data = base64.b64encode(buf.getbuffer()).decode('ascii')

    return render_template('home.html', rgb_image=url_for('static', filename='images/RGB_Images/Straight_1.png'), sensor_data_figure=f'data:image/png;base64,{data}')

@app.route("/csv")
def csv():
    # create the figure with custom script
    
    # # Generate the figure **without using pyplot**.
    # fig = Figure()
    # ax = fig.subplots()
    # ax.plot([1, 2])

    return render_template('csv.html', title='Show Data')
    
    return 