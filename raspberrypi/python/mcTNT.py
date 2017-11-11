from mcpi.minecraft import Minecraft


mc  = Minecraft.create()

TNT = 46

x, y, z = mc.player.getPos()  # player position (x, y, z)
mc.setBlocks(x+1, y+1, z+1, x+11, y+11, z+11, TNT, 1)
