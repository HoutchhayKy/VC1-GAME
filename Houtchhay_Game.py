# IMPORTS
from tkinter import *
import random
#............
root = Tk() 
canvas = Canvas(root, width=1200, height=700 ,bg="black")
#CONSTANTS
# playerImage=PhotoImage(file="/home/it-admin/Desktop/VC1-GAME")
# myPlayer=canvas.create_image(100,100,image=playerImage)
rectangle=canvas.create_rectangle(0,700,100,680,fill="blue")
colors = ["red", "orange", "yellow", "green", "purple", "brown", "blue", "indigo", "violet"]
color=random.choice(colors)
enemy=canvas.create_rectangle(50,50,100,100,fill=color)
#VARIBLAES

# ACTION PLAYER
def moveRight(event):
    x1,y1,x2,y2=canvas.coords(rectangle)
    if x2<=1100 and y2<=1100:
        canvas.move(rectangle,100,0)
        canvas.after(0,lambda :moveRight())
def moveLeft(event):
    x1,y1,x2,y2=canvas.coords(rectangle)
    if x1>0 and y1>0:
        canvas.move(rectangle,-100,0)
        canvas.after(0,lambda :moveLeft())
# ENEMY
def create_enemy():
    canvas.move(enemy,2,0)
    canvas.after(20,lambda:create_enemy())
# pack means "draw what i put inside"
canvas.pack(expand=True, fill='both')
#MOVE 
root.bind("<Left>", moveLeft)
root.bind("<Right>", moveRight)
# # moveball()
create_enemy()
create_enemy()
#Display all
root.mainloop()