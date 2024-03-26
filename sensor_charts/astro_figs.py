import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates

'''
data[0] = Date
data[1] = Temperature
data[2] = Humidity
data[3] = Pressure
'''

# choose style for charts
plt.style.use('Solarize_Light2')

# read csv file. File doesn't use header
data = pd.read_csv('data.csv', header=None)

timestamp = pd.to_datetime(data[0])
temp = data[1]
humid = data[2]
pressure = data[3]
axis = {'temp' : temp, 'humidity' : humid, 'pressure' : pressure}

# used within create_figure() to make each chart
def create_axis(axis):
	if (axis == 'temp'):
		# create timeseries chart for temp
		temp_chart.plot_date(timestamp, temp, label='Temperature', 
			linestyle='solid', marker=None)
		
		# Set title as Sensor Data because it is the first to render
		# all charts will share an x-axis
		temp_chart.set_title('Sensor Data') 
		temp_chart.set_ylabel('\N{DEGREE SIGN}C')
		
	elif (axis == 'humidity'):
		# create humidity chart
		humidity_chart.plot_date(timestamp, humid, label='Humidity',
			linestyle='solid', marker=None)
		
		humidity_chart.set_ylabel('Humidity')
		
	elif (axis == 'pressure'):
		# create pressure chart
		pressure_chart.plot_date(timestamp, pressure, label='Pressure',
			linestyle='solid', marker=None)
		
		pressure_chart.set_ylabel('Pressure')
		# Add a x-label to Pressure chart because all charts share x-axis 
		pressure_chart.set_xlabel('Time')
	
	else:
		return

# used for easy creation within animation
def create_figure():
	create_axis('temp')
	create_axis('humidity')
	create_axis('pressure')
	
	# Format times on the x-axis for readability 
	# gcf = Get Current Frame
	plt.gcf().autofmt_xdate()
	
	date_format = mpl_dates.DateFormatter('%H:%M:%S')
	
	# gca = Get Current Axis
	plt.gca().xaxis.set_major_formatter(date_format)
	
	plt.tight_layout()
	
# create one figure and three axis named 
# temp_chart, humidity_chart, and pressure_chart
fig, (temp_chart, humidity_chart, pressure_chart) = \
plt.subplots(nrows=3, ncols=1, sharex=True)

create_figure()

plt.show()
