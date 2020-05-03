import paho.mqtt.client as mqtt
import sys
import time

#-------------------------- Grovepi stuffs --------------------------
# By appending the folder of all the GrovePi libraries to the system path here,
# we are successfully `import grovepi`
sys.path.append('../../Software/Python/')
# This append is to support importing the LCD library.
sys.path.append('../../Software/Python/grove_rgb_lcd')

import grovepi
from grove_rgb_lcd import *

# SIG,NC,VCC,GND
# Connect the Grove Rotary Angle Sensor to analog port A0
potentiometer = 0

grovepi.pinMode(potentiometer,"INPUT")
time.sleep(1)

# Reference voltage of ADC is 5v
adc_ref = 5

# Vcc of the grove interface is normally 5v
grove_vcc = 5

#-------------------------- Grovepi stuffs --------------------------

#Custom callbacks 
def led_callback(client, userdata, message):
	print("led_callback: " + message.topic + " " + "\"" + 
		str(message.payload, "utf-8") + "\"")
	print("led_callback: message.payload is of type " + 
		str(type(message.payload)))
	if str(message.payload, "utf-8") == "LED_ON":
		grovepi.digitalWrite(3, 1)
	elif str(message.payload, "utf-8") == "LED_OFF":
		grovepi.digitalWrite(3, 0)

def lcd_callback(client, userdata, message):
	#the third argument is 'message' here unlike 'msg' in on_message 
	print("lcd_callback: " + message.topic + " " + "\"" + 
		str(message.payload, "utf-8") + "\"")
	print("lcd_callback: message.payload is of type " + 
		  str(type(message.payload)))
	setText_norefresh(str(message.payload, "utf-8"))
	setRGB(20,80,20)

# Subscribe the led and lcd topics when connected
def on_connect(client, userdata, flags, rc):
	print("Connected to server (i.e., broker) with result code "+str(rc))

	#subscribe to topics of interest here
	client.subscribe("rpi-tianhual/led")
	client.message_callback_add("rpi-tianhual/led", led_callback)

	client.subscribe("rpi-tianhual/lcd")
	client.message_callback_add("rpi-tianhual/lcd", lcd_callback)

#Default message callback.
def on_message(client, userdata, msg):
	print("on_message: " + msg.topic + " " + str(msg.payload, "utf-8"))

if __name__ == '__main__':
	PORT = 4    # D4
	button = 2	#D2

	#this section is covered in publisher_and_subscriber_example.py
	client = mqtt.Client()
	client.on_message = on_message
	client.on_connect = on_connect
	client.connect(host="eclipse.usc.edu", port=11000, keepalive=60)
	client.loop_start()

	grovepi.pinMode(button,"INPUT")

	while True:
		# 2 callback functions for receiving the messages
		lcd_callback
		led_callback
		# publish data at the same time
		client.publish("ee250@ee250-VirtualBox/ultrasonic", str(grovepi.ultrasonicRead(PORT)))
		if grovepi.digitalRead(button) == 1:
			client.publish("ee250@ee250-VirtualBox/button", "Button pressed")
		time.sleep(1)
			

