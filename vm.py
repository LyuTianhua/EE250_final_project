import sys
import time
import os
import matplotlib.pyplot as plt
import paho.mqtt.client as mqtt
import pandas as pd

#Default message callback.
def on_message(client, userdata, msg):
	print("on_message: " + msg.topic + " " + str(msg.payload, "utf-8"))

#Custom callbacks 
def SPY_index_callback(client, userdata, message):
	global dataSPYtemp, SPY
	dataSPYtemp = str(message.payload, "utf-8")
	
def WCHN_index_callback(client, userdata, message):
	global dataWCHNtemp, WCHN
	dataWCHNtemp = str(message.payload, "utf-8")

def INDA_index_callback(client, userdata, message):
	global dataINDAtemp, INDA
	dataINDAtemp = str(message.payload, "utf-8")
	
	
# Subscribe the screen_brightness topics when connected
def on_connect(client, userdata, flags, rc):
	if rc == 0:
		print("Connected to the server.")
	else:
		print("Unable to connect to the server.")
		
	#subscribe to topics of interest here
	client.subscribe("ubuntu/SPY_index")
	client.message_callback_add("ubuntu/SPY_index", SPY_index_callback)
	client.subscribe("ubuntu/WCHN_index")
	client.message_callback_add("ubuntu/WCHN_index", WCHN_index_callback)
	client.subscribe("ubuntu/sp_index")
	client.message_callback_add("ubuntu/INDA_index", INDA_index_callback)

cmd = ""
SPY = False
WCHN = False
INDA = False
dataSPYtemp = ""
dataWCHNtemp = ""
dataINDAtemp = ""

if __name__ == '__main__':
	
	client = mqtt.Client()
	client.on_message = on_message
	client.on_connect = on_connect
	client.connect(host="eclipse.usc.edu", port=11000, keepalive=60)
	client.loop_start()
	
	time.sleep(2)
	quit = False
	
	while True:

		while True:
			print("\n=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
			print("Please select the stock index you want to view.\nEnter in numeric order and do not seperate with anything if there are multiple.\nEnter \"quit\" to quit is program\n")
			print("1-SPDR S&P 500 Trust ETF, 2-WisdomTree ICBCCS S&P China 500 Fund, 3-ISHARES TR/MSCI INDIA ETF")
			cmd = ""
			cmd = input("Enter your command: ")
			
			if cmd == "quit":
				quit = True
				break
			
			if len(cmd) < 1 | len(cmd) > 3:
				print("\ninvalid input")
				print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
				continue
				
			valid = False
			for elem in cmd:
				if not(elem.isdigit()):
					print("\ninvalid input")
					break
				else:
					if int(elem) < 1 | int(elem) > 3:	
						print("\ninvalid input")
						break
					else:
						valid = True
						if elem == '1':
							SPY = True
						elif elem == '2':
							WCHN = True
						elif elem == '3':
							INDA = True
			print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
			if valid:
				break;
		
		if quit:
			print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
			break;
		
		SPY_index_callback
		WCHN_index_callback
		INDA_index_callback
		
		if SPY:
			while True:
				if len(dataSPYtemp) > 0:
					break
			dataSPY = pd.read_json(dataSPYtemp)
			dataSPY = dataSPY.T
			dataSPY['4. close'].plot()
			plt.title('SPY index')
			plt.show()
			SPY = False
			
		if WCHN:
			while True:
				if len(dataWCHNtemp) > 0:
					break
			dataWCHN = pd.read_json(dataWCHNtemp)
			dataWCHN = dataWCHN.T
			dataWCHN['4. close'].plot()
			plt.title('WCHN index')
			plt.show()
			WCHN = False
			

		if INDA:
			while True:
				if len(dataINDAtemp) > 0:
					break
			dataINDA = pd.read_json(dataINDAtemp)
			dataINDA = dataINDA.T
			dataINDA['4. close'].plot()
			plt.title('INDA index')
			plt.show()
			INDA = False
		
		time.sleep(1)
			

