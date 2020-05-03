import paho.mqtt.client as mqtt
import time

#Custom callbacks
def ultrasonic_callback(client, userdata, message):
	print("ultrasonic_callback: " + message.topic + " " + "\"" + 
		str(message.payload, "utf-8") + "\"")
	print("ultrasonic_callback: message.payload is of type " + 
		str(type(message.payload)))

def button_callback(client, userdata, message):
	print("button_callback: " + message.topic + " " + "\"" + 
		str(message.payload, "utf-8") + "\"")
	print("button_callback: message.payload is of type " + 
		str(type(message.payload)))

def on_connect(client, userdata, flags, rc):
	print("Connected to server (i.e., broker) with result code "+str(rc))

	#subscribe to the ultrasonic ranger and click button
	client.subscribe("ee250@ee250-VirtualBox/ultrasonic")
	client.message_callback_add("ee250@ee250-VirtualBox/ultrasonic", ultrasonic_callback)
	client.subscribe("ee250@ee250-VirtualBox/button")
	client.message_callback_add("ee250@ee250-VirtualBox/button", button_callback)

#Default message callback. Please use custom callbacks.
def on_message(client, userdata, msg):
	print("on_message: " + msg.topic + " " + str(msg.payload, "utf-8"))

if __name__ == '__main__':
	client = mqtt.Client()
	client.on_message = on_message
	client.on_connect = on_connect
	client.connect(host="eclipse.usc.edu", port=11000, keepalive=60)
	client.loop_start()

	while True:
		# 2 callback functions for receiving the messages
		ultrasonic_callback
		button_callback
		time.sleep(1)
			

