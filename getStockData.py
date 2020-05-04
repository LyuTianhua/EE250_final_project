from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
ts = TimeSeries(key='70CGDRRQ9MGZSXAV',output_format='pandas')
data, meta_data = ts.get_intraday(symbol='TSLA', interval='1min', outputsize='compact')
#print(data)
#print("Now just the important")
print(data['4. close'])
data['4. close'].plot()
plt.title('TSLA Price')
plt.show()
	