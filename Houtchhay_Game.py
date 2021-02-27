# IMPORTS
from tkinter import *
import random
# CREATE WINDOW
root = Tk() 
# INITIALIZE CANVAS ELEMENTS
canvas = Canvas(root,width=1200,height=700)
bg=PhotoImage(file="imge/background4.gif")
canvas.create_image( 0, 0, image = bg,anchor = "nw") 
canvas.pack(expand=True, fill='both')
root.resizable(False,False)
# DEFINE VARIABLES
playerImage = PhotoImage(file="imge/player2.gif")
playerId = canvas.create_image(600, 650, image = playerImage)
colors = ["red", "orange", "yellow", "green", "purple", "brown", "blue", "indigo", "violet"]
color=random.choice(colors)
ennemy=[]
ennemyImage=PhotoImage(file="imge/ennemy2.gif")
#POSITION  ENEMY LEVEL1
for index in range (1,6):
    x=100
    y=100
    size=100
    ennemyId=canvas.create_image(index*(x+size),y,image=ennemyImage)
    ennemy.append(ennemyId)
# DEFINE FUNCTIONS  
    # ACTION PLAYER
def moveRight(event):
    if canvas.coords(playerId)[0]<=1160:
        canvas.move(playerId,20,0)
    # screen_heigt = canvas.winfo_height()
def moveLeft(event):
    if canvas.coords(playerId)[0]>20:
        canvas.move(playerId,-20,0)
    # ACTION ENEMY
imageLaser1=PhotoImage(file="imge/redLaser.gif")
imageLaser2=PhotoImage(file="imge/redLaser.gif")
def laserPlayer():
    global firstLaser,secondLaser
    x=canvas.coords(playerId)[0]
    y=canvas.coords(playerId)[1]
    firstLaser=canvas.create_image(x-20,y-20,image=imageLaser1)
    secondLaser=canvas.create_image(x+20,y-20,image=imageLaser2)
    lasershooting()
def lasershooting():
    global firstLaser,secondLaser
    y=canvas.coords(playerId)[1]
    canvas.move(firstLaser,0,-20)
    canvas.move(secondLaser,0,-20)
    canvas.after(10,lambda:lasershooting())
# BIND KEYS
root.bind("<Left>", moveLeft)
root.bind("<Right>", moveRight)
#CALL FUNCTION
laserPlayer()

root.mainloop()