"""#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tkinter import *
from random import *
import time
fen = Tk()
can=Canvas(fen,width=500,height=500,background='white')
can.pack()
balle=can.create_oval(10,250,30,270,fill="red")
randx = randint(-10,10)
randy = randint(-10,10)
x=20
y=260
while True:
    if (x<5 or x>495):
        randx=-randx
    if (y<5 or y>495):
        randy=-randy
    can.move(balle,randx,randy)
    x=x+randx
    y=y+randy
    fen.update_idletasks()
    fen.update()
    time.sleep(0.01)

fen.mainloop()"""


#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tkinter import *
import time
import random
fen = Tk()
canvas=Canvas(fen,width=500,height=500,background='white')
canvas.pack()
class Balle:
    def __init__(self,posX_ini,posY_ini,vitX_ini,vitY_ini,ray):
        self.objet=canvas.create_oval(posX_ini-ray,posY_ini-ray,posX_ini+ray,posY_ini+ray,fill="red")
        self.posX=posX_ini
        self.posY=posY_ini
        self.vitX=vitX_ini
        self.vitY=vitY_ini
    def deplacement(self):
        if (self.posX<5 or self.posX>495):
            self.vitX=-self.vitX
        if (self.posY<5 or self.posY>495):
            self.vitY=-self.vitY
        canvas.move(self.objet,self.vitX,self.vitY)
        self.posX=self.posX+self.vitX
        self.posY=self.posY+self.vitY
x=[]
for i in range(50):
    balle = Balle(250,250,random.randint(-50,50),random.randint(-50,50),5)
    x.append(balle)
print(x)
while True:
    for i in x:
        i.deplacement()
    fen.update_idletasks()
    fen.update()
    time.sleep(0.01)
fen.mainloop()