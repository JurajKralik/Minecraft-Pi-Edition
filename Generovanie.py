from mcpi.minecraft import Minecraft
from perlin_noise import PerlinNoise
from tkinter import *
import tkinter as tk

## GUI seed setting

def button_click() :
    global seed
    seed = E1.get()
    seedgui.withdraw()
    seedgui.destroy()
    
seedgui = tk.Tk()
seedgui.title("Seed selection")
win_width = 270
win_height = 100
screen_width = seedgui.winfo_screenwidth()
screen_height = seedgui.winfo_screenheight()
center_x = int(screen_width/2 - (win_width/2))
center_y = int(screen_height/2 - (win_height/2))
seedgui.geometry(f'{win_width}x{win_height}+{center_x}+{center_y}')
seedgui.resizable(False,False)

L1 = Label(seedgui, text="World seed:")
L1.pack(side = TOP)
seed = tk.StringVar()
E1 = ttk.Entry(seedgui, textvariable=seed)
E1.focus()
E1.pack(side=TOP)
B1 = ttk.Button(seedgui, text="GO", command= button_click)
B1.pack(side=TOP)
seedgui.mainloop()


def intify(i) : # 32-bit value limiter
  return (i % 4294967296) - 2147483648

def hashCode(s) : # Replicates Java's string.hashCode function
  counter = 0
  for i in range(len(s)):
    counter += intify(ord(s[-i-1]) * (pow(31,i)))
  return intify(counter)

intseed = hashCode(seed)

print("seed: "+ str(seed))
print("numerical seed: "+ str(intseed))
intseed=int(intseed)

mc = Minecraft.create()

## MC find start

startX, startZ = 0, 0

finderBlock = mc.getBlock(startX, 0, startZ)
while not (finderBlock == 95) : #find X start
    startX -= 1
    finderBlock = mc.getBlock(startX, 0, startZ)
startX += 1
mc.postToChat("Start block X= "+ str(startX))

finderBlock = mc.getBlock(startX, 0, startZ)
while not (finderBlock == 95) : #find Z start
    startZ -= 1
    finderBlock = mc.getBlock(startX, 0, startZ)
startZ += 1
mc.postToChat("Start block Z= "+ str(startZ))

## MC delete everything

mc.postToChat("Deleting world")
mc.player.setPos(0.5,55,0.5)
mc.setBlocks(startX, -64, startZ, startX + 255, 63, startZ + 255, 0)
mc.postToChat("World deleted")

## MC terrain generation setup

density = 3 #nature density
curvature = 6 #higher = smoother transitions
perlScale = 50 #perlin noise value -> block scale
offset = 3.5 #up/down (water level = -15, top level = 50)
noise = PerlinNoise(octaves=0.1, seed=intseed) #0.1 oct = {-0,57 , 0,57}

chunkAmount = 0
chunkList = []
for undefined in range(256) :
    chunkList.append(256)#256 = not created yet

def chunkGet(pos) : #coordinates -> chunk number
    chunkNum = int((int((int(pos.x) - startX) / 16)) + int((int((int(pos.z) - startZ) / 16))*16))
    return (chunkNum)
    
def chunkSetX(pos) : 
    x = int(pos%16)*16+startX
    return x

def chunkSetZ(pos) :
    z = (int(pos/16)*16)+startZ
    return z

def buildTerrain(buildChunk) :
    buildX = chunkSetX(buildChunk)
    for undefined in range(16) : #X
        buildZ = chunkSetZ(buildChunk)
        for undefined in range(16) : #Z
            buildY = noise([buildX/curvature, buildZ/curvature]) * perlScale + offset
            mc.setBlocks(buildX, -64, buildZ, buildX, -61, buildZ, 7)
            if buildY > 2 : #Grass
                mc.setBlocks (buildX, buildY, buildZ, buildX, buildY-2, buildZ, 3)
                mc.setBlock (buildX, buildY, buildZ, 2)
                mc.setBlocks(buildX, -60, buildZ, buildX, buildY-3, buildZ, 1)
            elif buildY > -1 : #Beach
                mc.setBlocks (buildX, buildY, buildZ, buildX, buildY-2, buildZ, 12)
                mc.setBlocks (buildX, buildY-3, buildZ, buildX, buildY-4, buildZ, 24)
                mc.setBlocks(buildX, -60, buildZ, buildX, buildY-5, buildZ, 1)
            else: #Water
                mc.setBlocks (buildX, buildY, buildZ, buildX, buildY-2, buildZ, 12)
                mc.setBlocks (buildX, buildY-3, buildZ, buildX, buildY-4, buildZ, 24)
                mc.setBlocks (buildX, -1, buildZ, buildX, buildY+1, buildZ, 9)
                mc.setBlocks(buildX, -60, buildZ, buildX, buildY-5, buildZ, 1)
            buildZ += 1
        buildX += 1

def buildNature(buildChunk) :
    buildX = chunkSetX(buildChunk)
    for undefined in range(16) : #X
        buildZ = chunkSetZ(buildChunk)
        for undefined in range(16) : #Z
            plant = abs(noise([buildX*density, buildZ*density]))*175 #perlin value to {0, 100}
            buildY = noise([buildX/curvature, buildZ/curvature]) * perlScale + offset
            if plant > 80 : #Tree
                woodType = 17
                leafType = 18
                if plant > 95 :
                    treeHeight = 4
                elif plant > 92 :
                    treeHeight = 3
                elif plant > 89 :
                    treeHeight = 2
                elif plant > 86 :
                    treeHeight = 1
                elif plant > 82 :
                    treeHeight = 0
                else :
                    treeHeight = 1
                    woodType = 17, 2
                    leafType = 18, 2
                if buildY > 2 and buildY < 45: #tree
                    if mc.getBlock(buildX +1, buildY+2, buildZ) != 17 and mc.getBlock(buildX +1, buildY+2, buildZ+1) != 17 and mc.getBlock(buildX, buildY+2, buildZ+1) != 17 and mc.getBlock(buildX-1, buildY+2, buildZ+1) != 17 and mc.getBlock(buildX-1, buildY+2, buildZ) != 17 and mc.getBlock(buildX-1, buildY+2, buildZ-1) != 17 and mc.getBlock(buildX, buildY+2, buildZ-1) != 17 and mc.getBlock(buildX+1, buildY+2, buildZ-1) != 17 :
                        buildY = buildY + 1
                        mc.setBlocks(buildX-2, buildY+2+treeHeight, buildZ-2, buildX+2, buildY+3+treeHeight, buildZ+2, leafType)
                        mc.setBlocks(buildX-1, buildY+4+treeHeight, buildZ-1, buildX+1, buildY+4+treeHeight, buildZ+1, leafType)
                        mc.setBlocks(buildX-1, buildY+5+treeHeight, buildZ, buildX+1, buildY+5+treeHeight, buildZ, leafType)
                        mc.setBlocks(buildX, buildY+5+treeHeight, buildZ-1, buildX, buildY+5+treeHeight, buildZ+1, leafType)
                        mc.setBlocks(buildX, buildY, buildZ, buildX, buildY+4+treeHeight, buildZ, woodType)
            elif plant > 70 : #yelow flower
                if buildY > 2 and buildY < 45:
                    buildY += 1
                    mc.setBlock (buildX, buildY, buildZ, 37)
            elif plant > 65 : #cyan flower
                if buildY > 2 and buildY < 45:
                    buildY += 1
                    mc.setBlock (buildX, buildY, buildZ, 38)
            elif plant > 50 : #tall grass, desert grass, sugar cane
                if buildY > 2 and buildY < 45:
                    mc.setBlock (buildX, buildY+1, buildZ, 31, 1) #grass
                elif buildY < 3 and buildY > -1 and plant < 53 :
                    mc.setBlock (buildX, buildY+1, buildZ, 31) #desert
                elif int(buildY) == 0:
                    if mc.getBlock(buildX +1, -1, buildZ) == 9 or mc.getBlock(buildX -1, -1, buildZ) == 9 or mc.getBlock(buildX, -1, buildZ+1) == 9 or mc.getBlock(buildX, -1, buildZ-1) == 9:
                        mc.setBlock(buildX, 0, buildZ, 83) #sugar
            buildZ += 1
        buildX += 1

## MC terrain generation main loop

while not chunkAmount == 256 :
    buildChunk = int(chunkGet(mc.player.getPos()))
    buildChunkSolid = buildChunk
    if chunkList[buildChunk] == 256: #player position
        buildTerrain(buildChunk)
        buildNature(buildChunk)
        chunkList.pop(buildChunk)
        chunkList.insert(buildChunk,buildChunk)
        chunkAmount += 1
        print("Built chunk: "+str(buildChunk))
    if buildChunkSolid%16 != 0 : #chunk left
        buildChunk = buildChunkSolid - 1
        if chunkList[buildChunk] == 256:
            buildTerrain(buildChunk)
            buildNature(buildChunk)
            chunkList.pop(buildChunk)
            chunkList.insert(buildChunk,buildChunk)
            chunkAmount += 1
            print("Built chunk: "+str(buildChunk))
    if buildChunkSolid%16 != 0 and buildChunkSolid > 15 : #chunk left top
        buildChunk = buildChunkSolid - 17
        if chunkList[buildChunk] == 256:
            buildTerrain(buildChunk)
            buildNature(buildChunk)
            chunkList.pop(buildChunk)
            chunkList.insert(buildChunk,buildChunk)
            chunkAmount += 1
            print("Built chunk: "+str(buildChunk))
    if buildChunkSolid > 15 : #chunk top
        buildChunk = buildChunkSolid - 16
        if chunkList[buildChunk] == 256:
            buildTerrain(buildChunk)
            buildNature(buildChunk)
            chunkList.pop(buildChunk)
            chunkList.insert(buildChunk,buildChunk)
            chunkAmount += 1
            print("Built chunk: "+str(buildChunk))
    if buildChunkSolid%16 != 15 and buildChunkSolid > 15 : #chunk right top
        buildChunk = buildChunkSolid - 15
        if chunkList[buildChunk] == 256:
            buildTerrain(buildChunk)
            buildNature(buildChunk)
            chunkList.pop(buildChunk)
            chunkList.insert(buildChunk,buildChunk)
            chunkAmount += 1
            print("Built chunk: "+str(buildChunk))
    if buildChunkSolid%16 != 15 : #chunk right
        buildChunk = buildChunkSolid + 1
        if chunkList[buildChunk] == 256:
            buildChunk = buildChunkSolid + 1
            buildTerrain(buildChunk)
            buildNature(buildChunk)
            chunkList.pop(buildChunk)
            chunkList.insert(buildChunk,buildChunk)
            chunkAmount += 1
            print("Built chunk: "+str(buildChunk))
    if buildChunkSolid%16 != 15 and buildChunkSolid < 240 : #chunk right bot
        buildChunk = buildChunkSolid + 17
        if chunkList[buildChunk] == 256:
            buildTerrain(buildChunk)
            buildNature(buildChunk)
            chunkList.pop(buildChunk)
            chunkList.insert(buildChunk,buildChunk)
            chunkAmount += 1
            print("Built chunk: "+str(buildChunk))
    if buildChunkSolid < 240 : #chunk bot
        buildChunk = buildChunkSolid + 16
        if chunkList[buildChunk] == 256:
            buildTerrain(buildChunk)
            buildNature(buildChunk)
            chunkList.pop(buildChunk)
            chunkList.insert(buildChunk,buildChunk)
            chunkAmount += 1
            print("Built chunk: "+str(buildChunk))
    if buildChunkSolid%16 != 0 and buildChunkSolid < 240 : #chunk left bot
        buildChunk = buildChunkSolid + 15
        if chunkList[buildChunk] == 256:
            buildTerrain(buildChunk)
            buildNature(buildChunk)
            chunkList.pop(buildChunk)
            chunkList.insert(buildChunk,buildChunk)
            chunkAmount += 1
            print("Built chunk: "+str(buildChunk))

mc.postToChat("End of script")
quit()