from mcpi.minecraft import Minecraft
import time

mc  = Minecraft.create()
#mc.postToChat("Hello World")
x,y,z = mc.player.getPos()
bStr = str(x) + " " + str(y) + " "
while True:
	mc.postToChat(bStr)	
	time.sleep(1)


#tnt = 51
#mc.setBlocks(x+1, y+1, z+1, x+11, y+11, z+11, tnt, 1)
