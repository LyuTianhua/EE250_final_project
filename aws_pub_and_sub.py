import time
import json
import pandas as pd
import paho.mqtt.client as mqtt
from alpha_vantage.timeseries import TimeSeries

def on_connect(client, userdata, flags, rc):
	print("Connected to server (i.e., broker) with result code "+str(rc))

#Default message callback. Please use custom callbacks.
def on_message(client, userdata, msg):
	print("on_message: " + msg.topic + " " + str(msg.payload, "utf-8"))

if __name__ == '__main__':
	
	#this section is covered in publisher_and_subscriber_example.py
	client = mqtt.Client()
	client.on_message = on_message
	client.on_connect = on_connect
	client.connect(host="eclipse.usc.edu", port=11000, keepalive=60)
	client.loop_start()

	while True:
		# gather data here
		ts = TimeSeries(key='70CGDRRQ9MGZSXAV')
		dataSPY, meta_dataSPY = ts.get_intraday(symbol='SPY', interval='60min', outputsize='compact')
		time.sleep(15)   
		dataWCHN, meta_dataWCHN = ts.get_intraday(symbol='WCHN', interval='60min', outputsize='compact')
		time.sleep(15)   
		dataINDA, meta_dataINDA = ts.get_intraday(symbol='INDA', interval='60min', outputsize='compact')
		jsonStr = json.dumps(dataSPY)
		client.publish("ubuntu/SPY_index", jsonStr)
		jsonStr = json.dumps(dataWCHN)
		client.publish("ubuntu/WCHN_index", jsonStr)
		jsonStr = json.dumps(dataINDA)
		client.publish("ubuntu/INDA_index", jsonStr)
		time.sleep(15)    

