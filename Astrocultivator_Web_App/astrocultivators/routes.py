from flask import render_template, url_for, send_from_directory, send_file, flash, redirect
from astrocultivators import app

# imports for charts
from matplotlib.figure import Figure
import base64 
from io import BytesIO
import pandas as pd
from sensor_figure import Sensor_Figure

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', rgb_image=url_for('static', filename='images/RGB_Images/Straight_1.png'))

@app.route("/csv")
def csv():
    # create the figure with custom script
    fig = Sensor_Figure.get_figure()
    # # Generate the figure **without using pyplot**.
    # fig = Figure()
    # ax = fig.subplots()
    # ax.plot([1, 2])

    # save to a buffer
    buf = BytesIO()
    fig.savefig(buf, format="png")

    # Embed saved fig in html output
    data = base64.b64encode(buf.getbuffer()).decode('ascii')
    return f"<img src='data:image/png;base64,{data}'/>"

# def get_figure():
#     '''
#     data[0] = Date
#     data[1] = Temperature
#     data[2] = Humidity
#     data[3] = Pressure
#     '''

#     format = '-'
#     # date_format = mpl_dates.DateFormatter('%H:%M:%S')

#     # read in .csv data
#     data = pd.read_csv('C:/Users/codiy/Desktop/astrocult-py-flask/astrocult/Astrocultivator_Web_App/astrocultivators/test_seconds.csv', header=None)

#     timestamp = pd.to_datetime(data[0])
#     temp = data[1]
#     humid = data[2]
#     pres = data[3]

#     # create the figure
#     fig = Figure()
#     fig.suptitle('Sensor Data')

#     # create axes using add_suplot([# rows in fig], [# columns in fig], AxesNum)
#     temperature = fig.add_subplot(311)
#     temperature.set_ylabel('\N{DEGREE SIGN}C')
#     temperature.plot_date(x=timestamp, y=temp, fmt=format)

#     humidity = fig.add_subplot(312)
#     humidity.set_ylabel('Humidity')
#     humidity.plot_date(x=timestamp, y=humid, fmt=format)

#     pressure = fig.add_subplot(313)
#     pressure.set_ylabel('Pressure')
#     pressure.plot_date(x=timestamp, y=pres, fmt=format)

#     # style layout margins, labels, and axies
#     fig.tight_layout()
#     fig.align_ylabels()
#     fig.autofmt_xdate()

#     return fig