from mcpi.minecraft import Minecraft
import time
 
mc  = Minecraft.create()
#mc.postToChat("Hello World")
x,y,z = mc.player.getPos()


#mc.setBlock(x+1, y, z, 1 )
size=5
speed=.25
from mcpi.minecraft import Minecraft
import time

mc  = Minecraft.create()
#mc.postToChat("Hello World")
x,y,z = mc.player.getPos()
for z1 in range ( 1, size):
	for y1 in range ( 1, size ):
	 	print("here")
		time.sleep(speed)
	   	mc.setBlock(x, y + y1, z+z1, 14)

for x2 in range ( 1,size):
	for y2 in range ( 1, size ):
		time.sleep(speed)
		mc.setBlock( x + x2,y+ y2, z+size,15)

for z2 in range ( size,1):
	for y2 in range ( 1, size ):
		time.sleep(speed)
		mc.setBlock( x + size,y+y2, z+z2,16)

  
print ("outside of loop")

	
