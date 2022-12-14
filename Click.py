from mcpi.minecraft import Minecraft
mc = Minecraft.create()

while True:
    blockEvents = mc.events.pollBlockHits()
    if blockEvents :
        for blockEvent in blockEvents :
            X, Y, Z = blockEvent.pos
            mc.setBlock (X, Y, Z, 1)