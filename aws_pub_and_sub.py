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
	client.subscribe("ubuntu/location_callback")
	client.message_callback_add("ubuntu/location_callback", ultrasonic_callback)

#Default message callback. Please use custom callbacks.
def on_message(client, userdata, msg):
	print("on_message: " + msg.topic + " " + str(msg.payload, "utf-8"))


#		client.publish("rpi-tianhual/lcd", "w")


if __name__ == '__main__':
	#setup the keyboard event listener
#	lis = keyboard.Listener(on_press=on_press)
#	lis.start() # start to listen on a separate thread

	#this section is covered in publisher_and_subscriber_example.py
	client = mqtt.Client()
	client.on_message = on_message
	client.on_connect = on_connect
	client.connect(host="eclipse.usc.edu", port=11000, keepalive=60)
	client.loop_start()
	location_callback

	while True:
		#on_press(lis)
		location_callback
		time.sleep(1)    

