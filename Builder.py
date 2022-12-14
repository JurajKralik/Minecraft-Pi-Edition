from mcpi.minecraft import Minecraft
from tkinter import *
import tkinter as tk

mc = Minecraft.create()

def bt1():
    mc.events.clearAll()
    print("Building Hut")
    mc.postToChat("Building Hut")
    while True:
        blockEvents = mc.events.pollBlockHits()
        if blockEvents :
            for blockEvent in blockEvents :
                X, Y, Z = blockEvent.pos
                Y += 1
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
                break
            break
    
def bt2():
    mc.events.clearAll()
    print("Building Tavern")
    mc.postToChat("Building Tavern")
    while True:
        blockEvents = mc.events.pollBlockHits()
        if blockEvents :
            for blockEvent in blockEvents :
                X, Y, Z = blockEvent.pos
                Y += 1
                mc.setBlocks (X + 2, Y, Z, X + 8, Y, Z + 3, 85)
                mc.setBlocks (X + 3, Y, Z + 1, X + 7, Y, Z + 3, 0)
                mc.setBlock (X + 6, Y, Z + 3, 67, 2)
                mc.setBlock (X + 2, Y, Z + 10, 67, 3)
                mc.setBlocks (X, Y, Z + 4, X + 8, Y, Z + 9, 4)
                mc.setBlocks (X + 1, Y, Z + 5, X + 7, Y, Z + 8, 5)
                mc.setBlocks (X + 5, Y, Z + 6, X + 7, Y, Z + 8, 43) #floor
                mc.setBlocks (X, Y + 1, Z + 4, X, Y + 1, Z + 9, 4)
                mc.setBlocks (X, Y + 1, Z + 4, X + 5, Y + 1, Z + 4, 4)
                mc.setBlock (X + 1, Y + 1, Z + 9, 4)
                mc.setBlock (X + 7, Y + 1, Z + 4, 4)
                mc.setBlocks (X + 8, Y + 1, Z + 4, X + 8, Y + 1, Z + 9, 4)
                mc.setBlocks (X + 8, Y + 1, Z + 9, X + 3, Y + 1, Z + 9, 4)
                mc.setBlocks (X + 6, Y + 1, Z + 7, X + 6, Y + 1, Z + 8, 43)
                mc.setBlock (X + 1, Y + 1, Z + 5, 5)
                mc.setBlock (X + 2, Y + 1, Z + 5, 53, 3)
                mc.setBlock (X + 1, Y + 1, Z + 6, 53, 1)
                mc.setBlock (X + 2, Y + 1, Z + 6, 85)#1fl wall
                mc.setBlock (X, Y + 2, Z + 4, 4)
                mc.setBlock (X + 8, Y + 2, Z + 4, 4)
                mc.setBlock (X + 8, Y + 2, Z + 9, 4)
                mc.setBlock (X, Y + 2, Z + 9, 4)
                mc.setBlocks (X + 1, Y + 2, Z + 4, X + 5, Y + 2, Z + 4, 5)
                mc.setBlocks (X + 2, Y + 2, Z + 4, X + 3, Y + 2, Z + 4, 20)
                mc.setBlock (X + 7, Y + 2, Z + 4, 5)
                mc.setBlocks (X, Y + 2, Z + 5, X, Y + 2, Z + 8, 17)
                mc.setBlocks (X, Y + 2, Z + 6, X, Y + 2, Z + 7, 20)
                mc.setBlock (X + 1, Y + 2, Z + 9, 5)
                mc.setBlocks (X + 3, Y + 2, Z + 9, X + 7, Y + 2, Z + 9, 5)
                mc.setBlocks (X + 5, Y + 2, Z + 9, X + 6, Y + 2, Z + 9, 20)
                mc.setBlocks (X + 8, Y + 2, Z + 5, X + 8, Y + 2, Z + 8, 17)
                mc.setBlocks (X + 8, Y + 2, Z + 6, X + 8, Y + 2, Z + 7, 20)
                mc.setBlock (X + 2, Y + 2, Z + 6, 96)#2fl wall
                mc.setBlocks (X, Y + 3, Z + 4, X, Y + 3, Z + 9, 4)
                mc.setBlocks (X + 8, Y + 3, Z + 4, X + 8, Y + 3, Z + 9, 4)
                mc.setBlocks (X + 1, Y + 3, Z + 4, X + 7, Y + 3, Z + 4, 5)
                mc.setBlocks (X + 1, Y + 3, Z + 9, X + 7, Y + 3, Z + 9, 5)
                mc.setBlocks (X, Y + 3, Z + 3, X + 8, Y + 3, Z + 3, 53, 2)
                mc.setBlocks (X, Y + 3, Z + 10, X + 8, Y + 3, Z + 10, 53, 3)#3fl
                mc.setBlocks (X, Y + 4, Z + 4, X + 8, Y + 4, Z + 4, 53, 2)
                mc.setBlocks (X, Y + 4, Z + 9, X + 8, Y + 4, Z + 9, 53, 3)
                mc.setBlocks (X, Y + 4, Z + 5, X + 8, Y + 4, Z + 8, 5)
                mc.setBlocks (X + 1, Y + 4, Z + 6, X + 7, Y + 4, Z + 7, 0)#4fl
                mc.setBlocks (X, Y + 5, Z + 5, X + 8, Y + 5, Z + 5, 53, 2)
                mc.setBlocks (X, Y + 5, Z + 8, X + 8, Y + 5, Z + 8, 53, 3)
                mc.setBlocks (X, Y + 5, Z + 6, X + 8, Y + 5, Z + 7, 5)#5fl
                mc.setBlocks (X, Y + 6, Z + 6, X + 8, Y + 6, Z + 6, 53, 2)
                mc.setBlocks (X, Y + 6, Z + 7, X + 8, Y + 6, Z + 7, 53, 3)#6fl
                break
            break
    
def bt3():
    mc.events.clearAll()
    print("Building L house")
    mc.postToChat("Building L house")
    while True:
        blockEvents = mc.events.pollBlockHits()
        if blockEvents :
            for blockEvent in blockEvents :
                X, Y, Z = blockEvent.pos
                Y += 1
                mc.setBlock (X + 1, Y, Z + 6, 67)
                mc.setBlocks (X + 2, Y, Z, X + 12, Y, Z + 6, 4)
                mc.setBlocks (X + 2, Y, Z + 7, X + 7, Y, Z + 8, 4)
                mc.setBlocks (X + 3, Y, Z + 1, X + 11, Y, Z + 5, 5)
                mc.setBlocks (X + 3, Y, Z + 6, X + 6, Y, Z + 7, 5)#floor
                mc.setBlocks (X + 2, Y + 1, Z, X + 12, Y + 1, Z, 4)
                mc.setBlocks (X + 12, Y + 1, Z, X + 12, Y + 3, Z + 6, 4)
                mc.setBlocks (X + 12, Y + 1, Z + 6, X + 7, Y + 1, Z + 6, 4)
                mc.setBlocks (X + 7, Y + 1, Z + 6, X + 7, Y + 1, Z + 8, 4)
                mc.setBlocks (X + 7, Y + 1, Z + 8, X + 2, Y + 1, Z + 8, 4)
                mc.setBlocks (X + 2, Y + 1, Z + 8, X + 2, Y + 1, Z + 7, 4)
                mc.setBlocks (X + 2, Y + 1, Z + 1, X + 2, Y + 1, Z + 5, 4)#1fl wall
                mc.setBlocks (X + 2, Y + 2, Z, X + 2, Y + 2, Z, 4)
                mc.setBlocks (X + 2, Y + 2, Z + 8, X + 2, Y + 2, Z + 8, 4)
                mc.setBlocks (X + 7, Y + 2, Z + 8, X + 7, Y + 2, Z + 8, 4)
                mc.setBlocks (X + 2, Y + 2, Z + 1, X + 2, Y + 2, Z + 5, 5)
                mc.setBlocks (X + 2, Y + 2, Z + 2, X + 2, Y + 2, Z + 4, 17)
                mc.setBlock (X + 2, Y + 2, Z + 3, 20)
                mc.setBlock (X + 2, Y + 2, Z + 7, 5)
                mc.setBlocks (X + 3, Y + 2, Z + 8, X + 6, Y + 2, Z + 8, 17)
                mc.setBlocks (X + 4, Y + 2, Z + 8, X + 5, Y + 2, Z + 8, 20)
                mc.setBlocks (X + 7, Y + 2, Z + 6, X + 7, Y + 2, Z + 7, 5)
                mc.setBlocks (X + 8, Y + 2, Z + 6, X + 11, Y + 2, Z + 6, 17)
                mc.setBlocks (X + 9, Y + 2, Z + 6, X + 10, Y + 2, Z + 6, 20)
                mc.setBlocks (X + 8, Y + 2, Z, X + 11, Y + 2, Z, 17)
                mc.setBlocks (X + 9, Y + 2, Z, X + 10, Y + 2, Z, 20)
                mc.setBlocks (X + 3, Y + 2, Z, X + 6, Y + 2, Z, 17)
                mc.setBlocks (X + 4, Y + 2, Z, X + 5, Y + 2, Z, 20)
                mc.setBlock (X + 7, Y + 2, Z, 5)#2fl wall
                mc.setBlocks (X + 2, Y + 3, Z, X + 12, Y + 3, Z, 4)
                mc.setBlocks (X + 12, Y + 3, Z + 6, X + 7, Y + 3, Z + 6, 4)
                mc.setBlocks (X + 7, Y + 3, Z + 6, X + 7, Y + 3, Z + 7, 5)
                mc.setBlocks (X + 8, Y + 3, Z + 8, X + 2, Y + 3, Z + 8, 4)
                mc.setBlocks (X + 2, Y + 3, Z + 1, X + 2, Y + 3, Z + 7, 5)
                mc.setBlocks (X + 1, Y + 3, Z, X + 1, Y + 3, Z + 8, 53)
                mc.setBlock (X + 8, Y + 3, Z + 7, 5)
                mc.setBlock (X + 8, Y + 3, Z + 8, 53, 1)
                mc.setBlocks (X + 9, Y + 3, Z + 7, X + 12, Y + 3, Z + 7, 53, 3)#3fl wall
                mc.setBlocks (X + 3, Y + 4, Z, X + 6, Y + 4, Z + 8, 5)
                mc.setBlocks (X + 4, Y + 4, Z + 2, X + 5, Y + 4, Z + 7, 0)
                mc.setBlocks (X + 4, Y + 4, Z + 1, X + 12, Y + 4, Z + 1, 5)
                mc.setBlocks (X + 7, Y + 4, Z + 5, X + 12, Y + 4, Z + 5, 5)
                mc.setBlocks (X + 2, Y + 4, Z, X + 2, Y + 4, Z + 8, 53)
                mc.setBlocks (X + 8, Y + 4, Z + 6, X + 12, Y + 4, Z + 6, 53, 3)
                mc.setBlocks (X + 7, Y + 4, Z, X + 12, Y + 4, Z, 53, 2)
                mc.setBlock (X + 7, Y + 4, Z + 6, 5)
                mc.setBlocks (X + 7, Y + 4, Z + 7, X + 7, Y + 4, Z + 8, 53, 1)
                mc.setBlocks (X + 12, Y + 4, Z + 2, X + 12, Y + 4, Z + 4, 17)
                mc.setBlock (X + 12, Y + 4, Z + 3, 20)
                mc.setBlocks (X + 5, Y + 4, Z + 2, X + 10, Y + 4, Z + 4, 0)#4fl roof
                mc.setBlocks (X + 3, Y + 5, Z, X + 3, Y + 5, Z + 8, 53)
                mc.setBlocks (X + 4, Y + 5, Z, X + 5, Y + 5, Z + 8, 5)
                mc.setBlocks (X + 6, Y + 5, Z + 1, X + 6, Y + 5, Z + 5, 5)
                mc.setBlocks (X + 7, Y + 5, Z + 2, X + 12, Y + 5, Z + 4, 5)
                mc.setBlocks (X + 6, Y + 5, Z + 3, X + 11, Y + 5, Z + 3, 0)
                mc.setBlock (X + 6, Y + 5, Z, 53, 1)
                mc.setBlocks (X + 6, Y + 5, Z + 6, X + 6, Y + 5, Z + 8, 53, 1)
                mc.setBlocks (X + 7, Y + 5, Z + 1, X + 12, Y + 5, Z + 1, 53, 2)
                mc.setBlocks (X + 7, Y + 5, Z + 5, X + 12, Y + 5, Z + 5, 53, 3)#5fl roof
                mc.setBlocks (X + 4, Y + 6, Z, X + 4, Y + 6, Z + 8, 53)
                mc.setBlocks (X + 6, Y + 6, Z + 2, X + 12, Y + 6, Z + 2, 53, 2)
                mc.setBlocks (X + 6, Y + 6, Z + 4, X + 12, Y + 6, Z + 4, 53, 3)
                mc.setBlocks (X + 5, Y + 6, Z, X + 5, Y + 6, Z + 1, 53, 1)
                mc.setBlocks (X + 5, Y + 6, Z + 5, X + 5, Y + 6, Z + 8, 53, 1)
                mc.setBlocks (X + 5, Y + 6, Z + 2, X + 5, Y + 6, Z + 4, 5)
                mc.setBlocks (X + 5, Y + 6, Z + 3, X + 12, Y + 6, Z + 3, 5)
                break
            break
    
def bt4():
    mc.events.clearAll()
    print("Building Garden")
    mc.postToChat("Building Garden")
    while True:
        blockEvents = mc.events.pollBlockHits()
        if blockEvents :
            for blockEvent in blockEvents :
                X, Y, Z = blockEvent.pos
                mc.setBlocks (X, Y, Z, X + 8, Y, Z + 6, 3)
                mc.setBlocks (X, Y + 1, Z, X + 8, Y + 1, Z + 6, 17)
                mc.setBlocks (X + 1, Y + 1, Z + 1, X + 7, Y + 1, Z + 5, 60)
                mc.setBlocks (X + 1, Y + 1, Z + 3, X + 7, Y + 1, Z + 3, 9)
                mc.setBlocks (X + 1, Y + 2, Z + 1, X + 7, Y + 2, Z + 2, 59)
                mc.setBlocks (X + 1, Y + 2, Z + 4, X + 7, Y + 2, Z + 5, 59)
                break
            break
    
def bt5():
    mc.events.clearAll()
    print("Building Forge")
    mc.postToChat("Building Forge")
    while True:
        blockEvents = mc.events.pollBlockHits()
        if blockEvents :
            for blockEvent in blockEvents :
                X, Y, Z = blockEvent.pos
                Y += 1
                mc.setBlocks (X, Y, Z, X + 9, Y, Z + 6, 4)#fl
                mc.setBlocks (X, Y + 4, Z, X + 9, Y + 4, Z + 6, 4)#rf
                mc.setBlocks (X + 6, Y + 1, Z + 6, X + 9, Y + 3, Z + 6, 4)
                mc.setBlocks (X + 6, Y + 1, Z + 4, X + 6, Y + 3, Z + 6, 4)
                mc.setBlocks (X + 6, Y + 1, Z + 4, X + 9, Y + 1, Z + 6, 4)
                mc.setBlocks (X + 7, Y + 1, Z + 5, X + 8, Y + 1, Z + 5, 35, 1)
                mc.setBlock (X + 6, Y + 1, Z + 3, 4)
                mc.setBlocks (X + 9, Y + 1, Z, X + 9, Y + 3, Z, 85)
                mc.setBlocks (X + 5, Y + 1, Z, X + 5, Y + 3, Z, 85)
                mc.setBlocks (X, Y + 1, Z, X, Y + 4, Z, 17)
                mc.setBlocks (X + 3, Y + 1, Z, X + 3, Y + 4, Z, 17)
                mc.setBlocks (X, Y + 1, Z + 6, X, Y + 4, Z + 6, 17)
                mc.setBlocks (X + 1, Y + 1, Z, X + 2, Y + 3, Z, 5)
                mc.setBlocks (X, Y + 1, Z + 1, X, Y + 3, Z + 5, 5)
                mc.setBlocks (X + 1, Y + 1, Z + 6, X + 5, Y + 3, Z + 6, 5)
                mc.setBlocks (X + 4, Y + 1, Z + 3, X + 5, Y + 3, Z + 3, 5)
                mc.setBlocks (X + 3, Y + 1, Z + 2, X + 3, Y + 3, Z + 2, 5)
                mc.setBlock (X + 5, Y + 1, Z + 5, 58)
                mc.setBlock (X + 8, Y + 1, Z + 1, 43)
                mc.setBlock (X + 1, Y + 1, Z + 4, 53, 1)
                mc.setBlock (X + 2, Y + 1, Z + 5, 53, 2)
                mc.setBlock (X + 1, Y + 1, Z + 5, 5)
                mc.setBlock (X + 2, Y + 1, Z + 4, 85)#fl
                mc.setBlocks (X + 9, Y + 2, Z + 4, X + 9, Y + 2, Z + 5, 85)
                mc.setBlocks (X + 6, Y + 2, Z + 3, X + 6, Y + 3, Z + 3, 62, 2)
                mc.setBlocks (X + 7, Y + 3, Z + 4, X + 9, Y + 3, Z + 6, 4)
                mc.setBlock (X + 3, Y + 3, Z + 1, 5)
                mc.setBlock (X, Y + 2, Z + 2, 20)
                mc.setBlock (X, Y + 2, Z + 4, 20)
                mc.setBlock (X + 2, Y + 2, Z + 6, 20)
                mc.setBlock (X + 4, Y + 2, Z + 6, 20)
                mc.setBlock (X + 2, Y + 2, Z + 4, 96)
                mc.setBlocks (X, Y + 5, Z, X + 9, Y + 5, Z + 6, 44)
                mc.setBlocks (X + 1, Y + 5, Z + 1, X + 8, Y + 5, Z + 5, 0)
                break
            break

def bt6():
    mc.events.clearAll()
    print("Building Gravel")
    mc.postToChat("Building road")
    while True :
        blockEvents = mc.events.pollBlockHits()
        if blockEvents :
            break
        X, Y, Z = mc.player.getPos()
        block = mc.getHeight(X, Z)
        mc.setBlock(X, block - 1, Z, 13)
    
builderGui = tk.Tk()
surf = IntVar()
builderGui.title("Builder")
win_width = 230
win_height = 250
screen_width = builderGui.winfo_screenwidth()
screen_height = builderGui.winfo_screenheight()
center_x = int(screen_width/2 - (win_width/2))
center_y = int(screen_height/2 - (win_height/2))
builderGui.geometry(f'{win_width}x{win_height}+{center_x}+{center_y}')
builderGui.resizable(False,False)
 
L1 = Label(builderGui, text="Choose building:")
L1.pack(side = TOP)
seed = tk.StringVar()
L2 = Label(builderGui, text=" ")
L2.pack(side = TOP)
B1 = ttk.Button(builderGui, text="Hut", command = bt1)
B1.pack(side=TOP)
B2 = ttk.Button(builderGui, text="Tavern", command = bt2)
B2.pack(side=TOP)
B3 = ttk.Button(builderGui, text="L house", command = bt3)
B3.pack(side=TOP)
B4 = ttk.Button(builderGui, text="Garden", command = bt4)
B4.pack(side=TOP)
B5 = ttk.Button(builderGui, text="Forge", command = bt5)
B5.pack(side=TOP)
B6 = ttk.Button(builderGui, text="Roads", command = bt6)
B6.pack(side=TOP)
builderGui.mainloop()

mc.postToChat("End of script")
print("End of script")
quit()
