#!/usr/bin/env python

import cgi
import cgitb    #display CGI error on browser
import time
import RPi.GPIO as GPIO


print('Content-type: text/html; charset=UTF-8\r\n')
print('Web SERVO')

print('<form action="" method="post">')
print('<input type="number" name="deg" >')
print('<input type="ON" name="Switch" value = "ON">')
print('<input type="OFF" name="Switch2" value = "OFF">')

print('</form>')


GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.OUT)
servo = GPIO.PWM(2,50)
servo.start(0.0)0
form = cgi.FieldStorage()
value = form.getvalue("deg")

def setservo(angle):
	servo.start(0.0)
	servo.ChangeDutyCycle(((angle+90)/180+0.5)*5)
	time.sleep(1)

if Switch == "ON" :
	setservo(int(value))
	time.sleep(1)
	print('DEGREE OF THE SERVO IS:'+str(value))
elif Switch2 == "OFF":
