#!/usr/bin/python
#coding:utf-8
import RPi.GPIO as GPIO
import time



GPIO_OUT = 14

def setup_GPIO():
	GPIO.setmode(GPIO.BCM)
  	GPIO.setwarnings(False)   
	GPIO.setup(GPIO_OUT, GPIO.OUT) 

def start_fan():
	GPIO.output(GPIO_OUT,GPIO.HIGH)

def stop_fan():
	GPIO.output(GPIO_OUT,GPIO.LOW)

def cpu_temp():
	tempFile=open("/sys/class/thermal/thermal_zone0/temp")
 	cpu_temp=tempFile.read()
 	tempFile.close()
	temp_c=(int(cpu_temp)/1000)
 	return int(temp_c)


def fen():
 	if cpu_temp()>=55:
 		start_fan()
 		

 	elif cpu_temp()<=45:
 		stop_fan()
 		
 	else:
 		pass

 	

if __name__ == '__main__':
	setup_GPIO()
	while True:
		fen()
		time.sleep(5)
