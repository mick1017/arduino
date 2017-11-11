import RPi.GPIO as GPIO
import time

YELLOW = 17
WHITE = 27
RED = 6
GREEN = 22

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)

GPIO.output(22,GPIO.HIGH)
time.sleep(1)
GPIO.output(22,GPIO.LOW)



