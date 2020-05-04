from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
import json
import pandas as pd
ts = TimeSeries(key='70CGDRRQ9MGZSXAV')
data, meta_data = ts.get_intraday(symbol='INDA', interval='1min', outputsize='compact')
#print(data)
#print("Now just the important")
#SPY,WCHN,INDA
print(data)
y = json.dumps(data)
print("finished dump")
print(y)

pData = pd.read_json(y);
pData = pData.T
print("read json")
print(pData)
pData['4. close'].plot()
plt.title('The graph of ')
plt.show()


	