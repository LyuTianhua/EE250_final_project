import paho.mqtt.client as mqtt
import time
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
	
	# gather data here
	ts = TimeSeries(key='70CGDRRQ9MGZSXAV',output_format='pandas')
	data, meta_data = ts.get_intraday(symbol='TSLA', interval='1min', outputsize='compact')

	while True:
		# debug
		client.publish("ubuntu/dow_index", "100")
		client.publish("ubuntu/nasdaq_index", "100")
		client.publish("ubuntu/sp_index", "100")
		time.sleep(3)    

