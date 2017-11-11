from mcpi.minecraft import Minecraft
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




mc  = Minecraft.create()

STONE = 1
GRASS = 2
DIRT = 3
FLOWER = 38
FIRE = 51
SNOW = 78
ICE = 79

while True:
    x, y, z = mc.player.getPos()  # player position (x, y, z)
    block_beneath = mc.getBlock(x, y-1, z)  # block ID
    block_in      = mc.getBlock(x, y, z)

    print(str(block_beneath) + "," +  str(block_in))     

    if block_beneath == GRASS:
        #mc.setBlock(x, y, z, flower)
	GPIO.output(GREEN,GPIO.HIGH)
    elif block_beneath == FIRE or block_in == FIRE or block_beneath == DIRT:
	GPIO.output(RED,GPIO.HIGH)
    elif block_beneath == SNOW or  block_beneath == ICE or block_beneath == STONE:
	GPIO.output(WHITE,GPIO.HIGH)
    else:
	GPIO.output(GREEN,GPIO.LOW)
	GPIO.output(RED,GPIO.LOW)
	GPIO.output(YELLOW,GPIO.LOW)
	GPIO.output(WHITE,GPIO.LOW)

    

