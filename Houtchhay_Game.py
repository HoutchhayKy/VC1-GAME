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
# DEFINE VARIABLES
playerImage = PhotoImage(file="imge/player1.gif")
playerId = canvas.create_image(600, 650, image = playerImage)
colors = ["red", "orange", "yellow", "green", "purple", "brown", "blue", "indigo", "violet"]
color=random.choice(colors)
ennemy=[]
ennemyImage=PhotoImage(file="imge/ennemy2.gif")
#POSITION  ENEMY LEVEL1
margian=50
for index in range (1,11):
    X=50
    Y=50
    size=50
    ennemyId=canvas.create_image(index*(X+size),Y,image=ennemyImage)
# DEFINE FUNCTIONS
    # ACTION PLAYER
def moveRight(event):
    if canvas.coords(playerId)[0]<=1160:
        canvas.move(playerId,20,0)
    # screen_heigt = canvas.winfo_height()
def moveLeft(event):
    if canvas.coords(playerId)[0]>20:
        canvas.move(playerId,-20,0)
    # ENEMY

# BIND KEYS
root.bind("<Left>", moveLeft)
root.bind("<Right>", moveRight)

#CALL FUNCTION

root.mainloop()