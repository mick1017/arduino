import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)

GPIO.output(17,GPIO.HIGH)
time.sleep(1)
GPIO.output(17,GPIO.LOW)


for num in range ( 1,10):
	print "we are on %d" % ( num )
	print "Light on"
	GPIO.output(6,GPIO.HIGH)
	time.sleep(.051)
	GPIO.output(17,GPIO.HIGH)
	time.sleep(.051)
	GPIO.output(22,GPIO.HIGH)
	time.sleep(.051)
	GPIO.output(27,GPIO.HIGH)
	time.sleep(.051)
	print "Light off"
	GPIO.output(17,GPIO.LOW)
	time.sleep(.051)
	GPIO.output(27,GPIO.LOW)
	time.sleep(.051)
	GPIO.output(22,GPIO.LOW)
	time.sleep(.051)
	GPIO.output(6,GPIO.LOW)
	time.sleep(.051)

	
