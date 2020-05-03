import paho.mqtt.client as mqtt
import time

#Custom callbacks
def location_callback(client, userdata, message):
	print("location_callback: " + message.topic + " " + "\"" + 
		str(message.payload, "utf-8") + "\"")
	print("location_callback: message.payload is of type " + 
		str(type(message.payload)))

def on_connect(client, userdata, flags, rc):
	print("Connected to server (i.e., broker) with result code "+str(rc))

	#subscribe to topics of interest here
	client.subscribe("ee250@ee250-VirtualBox/location")
	client.message_callback_add("ee250@ee250-VirtualBox/location", location_callback)

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
		client.publish("ubuntu/screen_brightness", "100")
		location_callback
		time.sleep(1)    

