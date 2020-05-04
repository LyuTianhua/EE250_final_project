import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
	print("Connected to server (i.e., broker) with result code "+str(rc))

#Default message callback. Please use custom callbacks.
def on_message(client, userdata, msg):
	print("on_message: " + msg.topic + " " + str(msg.payload, "utf-8"))


#		client.publish("ubuntu/lcd", "w")


if __name__ == '__main__':

	#this section is covered in publisher_and_subscriber_example.py
	client = mqtt.Client()
	client.on_message = on_message
	client.on_connect = on_connect
	client.connect(host="eclipse.usc.edu", port=11000, keepalive=60)
	client.loop_start()
	location_callback

	while True:
		# debug
		client.publish("ubuntu/dow_index", "100")
		client.publish("ubuntu/nasdaq_index", "100")
		client.publish("ubuntu/sp_index", "100")
		time.sleep(3)    

