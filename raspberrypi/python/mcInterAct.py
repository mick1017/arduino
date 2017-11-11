from mcpi.minecraft import Minecraft
import RPi.GPIO as GPIO
import os
import glob
import time


os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
 
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'



YELLOW = 17
WHITE = 27
GREEN = 6
RED = 22

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)


def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines
 
def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0

        return (  temp_f )


mc  = Minecraft.create()

STONE = 1
GRASS = 2
DIRT = 3
FLOWER = 38
TORCH = 50
FIRE = 51
SNOW = 78
ICE = 79
WATER = 81
TNT = 46
SAND =12



while True:
    x, y, z = mc.player.getPos()  # player position (x, y, z)
    block_beneath = mc.getBlock(x, y-1, z)  # block ID
    block_in      = mc.getBlock(x, y, z)

    print(str(block_beneath) + "," +  str(block_in))     

    if block_beneath == GRASS:
        #mc.setBlock(x, y, z, flower)
	GPIO.output(GREEN,GPIO.HIGH)
	GPIO.output(RED,GPIO.LOW)
	GPIO.output(YELLOW,GPIO.LOW)
	GPIO.output(WHITE,GPIO.LOW)
	temp = read_temp()
	print ("temp: " + str(temp) )
	if temp > 70 and temp < 80:
		mc.setBlock(x,y, z, TORCH)
	elif temp > 81 and temp < 90:
		mc.setBlock(x, y-1, z, TNT)
		print("Starting Fire!")
    elif block_beneath == FIRE or block_in == FIRE or block_beneath == DIRT:
	GPIO.output(RED,GPIO.HIGH)
	GPIO.output(YELLOW,GPIO.LOW)
	GPIO.output(GREEN,GPIO.LOW)
	GPIO.output(WHITE,GPIO.LOW)	
    elif block_beneath == SNOW or  block_beneath == ICE or block_beneath == STONE:
	GPIO.output(WHITE,GPIO.HIGH)
        GPIO.output(GREEN,GPIO.LOW)
	GPIO.output(RED,GPIO.LOW)
	GPIO.output(YELLOW,GPIO.LOW)
    elif block_beneath == SAND:
	GPIO.output(WHITE,GPIO.LOW)
        GPIO.output(GREEN,GPIO.LOW)
	GPIO.output(RED,GPIO.LOW)
	GPIO.output(YELLOW,GPIO.HIGH)
    else:
	GPIO.output(GREEN,GPIO.LOW)
	GPIO.output(RED,GPIO.LOW)
	GPIO.output(YELLOW,GPIO.LOW)
	GPIO.output(WHITE,GPIO.LOW)

    

