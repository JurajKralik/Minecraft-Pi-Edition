from mcpi.minecraft import Minecraft
mc = Minecraft.create()
X, Y, Z = mc.player.getPos()
mc.setBlock (X, Y, Z + 2, 67)
mc.setBlocks (X + 1, Y, Z, X + 5, Y, Z + 4, 4)#floor
mc.setBlocks (X + 1, Y + 1, Z, X + 1, Y + 3, Z, 4)
mc.setBlocks (X + 5, Y + 1, Z, X + 5, Y + 3, Z, 4)
mc.setBlocks (X + 1, Y + 1, Z + 4, X + 1, Y + 3, Z + 4, 4)
mc.setBlocks (X + 5, Y + 1, Z + 4, X + 5, Y + 3, Z + 4, 4)#pillars
mc.setBlocks (X + 2, Y + 1, Z, X + 4, Y + 3, Z, 5)
mc.setBlocks (X + 2, Y + 1, Z + 4, X + 4, Y + 3, Z + 4, 5)
mc.setBlocks (X + 5, Y + 1, Z + 1, X + 5, Y + 3, Z + 3, 5)
mc.setBlocks (X + 1, Y + 1, Z + 1, X + 1, Y + 3, Z + 3, 5)#walls
mc.setBlocks (X + 1, Y + 1, Z + 2, X + 1, Y + 2, Z + 2, 0)
mc.setBlock (X + 3, Y + 2, Z, 20)
mc.setBlock (X + 3, Y + 2, Z + 4, 20)
mc.setBlock (X + 5, Y + 2, Z + 2, 20)#windows
mc.setBlocks (X + 1, Y + 4, Z, X + 5, Y + 4, Z + 4, 17)
mc.setBlocks (X + 2, Y + 4, Z + 1, X + 4, Y + 4, Z + 3, 5)
mc.setBlocks (X + 1, Y + 5, Z, X + 5, Y + 5, Z + 4, 85)
mc.setBlocks (X + 2, Y + 5, Z + 1, X + 4, Y + 5, Z + 3, 0)#roof
quit()
