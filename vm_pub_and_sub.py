import paho.mqtt.client as mqtt
import sys
import time

#Custom callbacks 
def screen_brightness_callback(client, userdata, message):
	print("screen_brightness_callback: " + message.topic + " " + "\"" + 
		str(message.payload, "utf-8") + "\"")
	print("screen_brightness_callback: message.payload is of type " + 
		str(type(message.payload)))
	# Change brightness here

# Subscribe the screen_brightness topics when connected
def on_connect(client, userdata, flags, rc):
	print("Connected to server (i.e., broker) with result code "+str(rc))

	#subscribe to topics of interest here
	client.subscribe("ubuntu/screen_brightness")
	client.message_callback_add("ubuntu/screen_brightness", screen_brightness)

#Default message callback.
def on_message(client, userdata, msg):
	print("on_message: " + msg.topic + " " + str(msg.payload, "utf-8"))

if __name__ == '__main__':

	#this section is covered in publisher_and_subscriber_example.py
	client = mqtt.Client()
	client.on_message = on_message
	client.on_connect = on_connect
	client.connect(host="eclipse.usc.edu", port=11000, keepalive=60)
	client.loop_start()

	# publish current location
	client.publish("ee250@ee250-VirtualBox/location", "los angeles")

	while True:
		# debug
		client.publish("ee250@ee250-VirtualBox/location", "los angeles")
		# 1 callback functions for receiving the messages
		screen_brightness_callback
		time.sleep(1)
			

