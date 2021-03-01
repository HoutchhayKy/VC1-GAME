# IMPORTS
from tkinter import *
import random

# CREATE WINDOW
root = Tk() 

# CONSTANT
canvas = Canvas(root,width=1200,height=700)
bg=PhotoImage(file="imge/background4.gif")
canvas.create_image( 0, 0, image = bg,anchor = "nw")
playerImage = PhotoImage(file="imge/player2.gif")
ennemyImage=PhotoImage(file="imge/ennemy2.gif") 
imageLaser1=PhotoImage(file="imge/redLaser.gif")
imageLaser2=PhotoImage(file="imge/redLaser.gif")
canvas.pack(expand=True, fill='both')
root.resizable(False,False)

# DEFINE VARIABLES
playerId = canvas.create_image(600, 650, image = playerImage)

ennemy1=canvas.create_image(50,80,image=ennemyImage)
ennemy2=canvas.create_image(150,80,image=ennemyImage)
ennemy3=canvas.create_image(250,80,image=ennemyImage)
ennemy4=canvas.create_image(350,80,image=ennemyImage)
ennemy5=canvas.create_image(450,80,image=ennemyImage)
ennemy6=canvas.create_image(550,80,image=ennemyImage)
ennemy7=canvas.create_image(650,80,image=ennemyImage)
ennemy8=canvas.create_image(750,80,image=ennemyImage)
ennemies = [[ennemy1,10,0], [ennemy2,10,0], [ennemy3,10,0], [ennemy4,10,0],[ennemy5,10,0],[ennemy6,10,0],[ennemy7,10,0],[ennemy8,10,0]]

#POSITION  ENEMY LEVEL1
def ennemyposition():
    global ennemies
    for index in range (len(ennemies)):
        position=canvas.coords(ennemies[index][0])
        if position[0]<40 or position[0]>1160:
            ennemies[index][1]=-ennemies[index][1]
        canvas.move(ennemies[index][0],ennemies[index][1],ennemies[index][2])
    canvas.after(90,ennemyposition)

# ACTION PLAYER
def moveRight(event):
    if canvas.coords(playerId)[0]<=1160:
        canvas.move(playerId,20,0)
def moveLeft(event):
    if canvas.coords(playerId)[0]>20:
        canvas.move(playerId,-20,0)

#CREATE BULLET
def lasershooting():
    global firstLaser,secondLaser
    canvas.move(firstLaser,0,-20)
    canvas.move(secondLaser,0,-20)
    dy1=canvas.coords(firstLaser)[1]
    dy2=canvas.coords(secondLaser)[1]
    if dy1>0 and dy2>0:
        canvas.after(10,lambda:lasershooting())
    else:    
        canvas.delete(firstLaser)
        canvas.delete(secondLaser)
        laserPlayer()
def laserPlayer():
    global firstLaser,secondLaser
    x=canvas.coords(playerId)[0]
    y=canvas.coords(playerId)[1]
    firstLaser=canvas.create_image(x-20,y-20,image=imageLaser1)
    secondLaser=canvas.create_image(x+20,y-20,image=imageLaser2)
    lasershooting()

# BIND KEYS
root.bind("<Left>", moveLeft)
root.bind("<Right>", moveRight)

#CALL FUNCTION
ennemyposition()
laserPlayer()

root.mainloop()