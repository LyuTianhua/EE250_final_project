import sys
import time
import os
import matplotlib.pyplot as plt
import paho.mqtt.client as mqtt

cmd = ""
dow = False
nasdaq = False
sp = False

#Default message callback.
def on_message(client, userdata, msg):
	print("on_message: " + msg.topic + " " + str(msg.payload, "utf-8"))

#Custom callbacks 
def dow_index_callback(client, userdata, message):
	print("dow_index_callback: " + message.topic + " " + "\"" + 
		str(message.payload, "utf-8") + "\"")
	dow_index = str(type(message.payload))
	print("dow_index_callback: message.payload is of type " + dow_index)
	plt.title('DOW index')
	plt.show()
	
def nasdaq_index_callback(client, userdata, message):
	print("nasdaq_index_callback: " + message.topic + " " + "\"" + 
		str(message.payload, "utf-8") + "\"")
	nasdaq_index = str(type(message.payload))
	print("nasdaq_index_callback: message.payload is of type " + nasdaq_index)
	plt.title('Nasdaq index')
	plt.show()

def sp_index_callback(client, userdata, message):
	print("sp_index_callback: " + message.topic + " " + "\"" + 
		str(message.payload, "utf-8") + "\"")
	sp_index = str(type(message.payload))
	print("sp_index_callback: message.payload is of type " + sp_index)
	plt.title('S&P index')
	plt.show()
	
# Subscribe the screen_brightness topics when connected
def on_connect(client, userdata, flags, rc):
	if rc == 0:
		print("Connected to server.")
	else:
		print("Unable to connect to server.")
		
	#subscribe to topics of interest here
	client.subscribe("ubuntu/dow_index")
	client.message_callback_add("ubuntu/dow_index", dow_index_callback)
	client.subscribe("ubuntu/nasdaq_index")
	client.message_callback_add("ubuntu/nasdaq_index", nasdaq_index_callback)
	client.subscribe("ubuntu/sp_index")
	client.message_callback_add("ubuntu/sp_index", sp_index_callback)

if __name__ == '__main__':

	while True:
		print("\nPlease select the stock index you want to view.\nEnter in numeric order and do not seperate with anything if there are multiple.")
		print("1-dow index, 2-nasdaq index, 3-s&p index")
		cmd = input("Enter your choice: ")
		
		if len(cmd) < 1 | len(cmd) > 3:
			print("\ninvalid input\n")
			continue
			
		valid = False
		for elem in cmd:
			if not(elem.isdigit()):
				break
			else:
				if int(elem) < 1 & int(elem) > 3:
					break
				else:
					valid = True
					if elem == 1:
						dow = True
					elif elem == 2:
						nasdaq = True
					elif elem == 3:
						sp = True
		
		if valid:
			break;
	
	#this section is covered in publisher_and_subscriber_example.py
	client = mqtt.Client()
	client.on_message = on_message
	client.on_connect = on_connect
	client.connect(host="eclipse.usc.edu", port=11000, keepalive=60)
	client.loop_start()
	
	while True:
		# callback functions for receiving the messages
		if dow:
			dow_index_callback
		if nasdaq:
			nasdaq_index_callback
		if sp:
			sp_index_callback
		time.sleep(1)
			

