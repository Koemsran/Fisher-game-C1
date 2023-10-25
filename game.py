import tkinter as tk
from tkinter import *
import winsound
from random import randrange
import time


SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 740
window = tk.Tk()
window.geometry(str(SCREEN_WIDTH)+"x"+str(SCREEN_HEIGHT))
window.title('Group-C1 - Game Fish')
window.attributes('-fullscreen', True)
canvas = tk.Canvas(window)


game_start = tk.PhotoImage(file='images/bg/background.png')
bg_start = tk.PhotoImage(file='images/bg/bg.png')
game_win = tk.PhotoImage(file='images/bg/game_win.png')
game_over = tk.PhotoImage(file='images/bg/game_over.png')


actor = tk.PhotoImage(file='images/player1.png')
actor1 = tk.PhotoImage(file='images/player2.png')
enemy1 = tk.PhotoImage(file='images/enemies/enemy1.png')
enemy2 = tk.PhotoImage(file='images/enemies/enemy2.png')
enemy6 = tk.PhotoImage(file='images/enemies/enemy6.png')
small_fish = tk.PhotoImage(file='images/enemies/small_fish.png')
right1 = tk.PhotoImage(file='images/enemies/right1.png')
bubble1 = tk.PhotoImage(file='images/bubble1.png')
bubble2 = tk.PhotoImage(file='images/bubble2.png')
bubble3 = tk.PhotoImage(file='images/bubble3.png')

coin1 = tk.PhotoImage(file='images/coin1.png')
coin2 = tk.PhotoImage(file='images/coin2.png')
diamond1 = tk.PhotoImage(file='images/diamond1.png')
diamond2 = tk.PhotoImage(file='images/diamond2.png')
heard1 = tk.PhotoImage(file='images/heard1.png')
heard2 = tk.PhotoImage(file='images/heard2.png')

menu = tk.PhotoImage(file='images/menus/menus 1.png')
btn_start = tk.PhotoImage(file='images/menus/start_menu.png')
btn_continue = tk.PhotoImage(file='images/menus/continue_menu.png')
btn_exit = tk.PhotoImage(file='images/menus/exit_menu.png')
btn_back = tk.PhotoImage(file='images/menus/back_menu.png')



player_x =700
player_y = 450
enemyX= 1400
listOfDiamond=[]
listOfCoin=[]
listOfEnemy=[]
listOfLife=[]
totalScore = 0
totalDiamond = 0
getCoin=0
numberOfDiamond =0
life=6
isStart = True

# -------------function game------------
# -----------------------------------------

#--------------Process game------------------
def processGame():
    if numberOfDiamond==3 and life !=0:
        gameWin()
    if life==0:
        gameOver()
    canvas.after(100,processGame)

#--------------game show--------------
def gameShow(event):
    
    canvas.delete('all')
    canvas.create_image(680,372, image= bg_start)
    canvas.create_image(680, 100, image=menu, tags= 'menu')
    canvas.create_image(680,280, image=btn_start, tags="startgame")
    canvas.create_image(680,410,image=btn_continue, tags="continue")
    canvas.create_image(680,540,image=btn_exit, tags="exit")
    
def gameStart(event):
    global player, NumberDiamond, TotalCoin
    canvas.delete('all')
    canvas.create_image(680, 372,  image=game_start)
    player = canvas.create_image(player_x, player_y, image=actor)
    Numberdiamond = canvas.create_text(560, 70, text=": "+str(totalDiamond), font=("serif", 20 ,'bold'), fill="black")
    TotalCoin = canvas.create_text(760, 70, text=': '+str(totalScore), font=("serif", 20 ,'bold'), fill="black")

    canvas.create_image(100,70, image = btn_back, tags= 'back')
    winsound.PlaySound("sounds/playing.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)

    canvas.create_image(520, 65, image = diamond1)
    canvas.create_image(720, 65, image = coin2)

    for i in range(5):
        life_actor = canvas.create_image(1150 + i * 37, 60, image=heard1)
        listOfLife.append(life_actor)

# ===================CALL FUNCTION HERE<=================
    createEnemy()
    createDiamond()
    small_fishes()
    move_buuble()
    createCion()
    pickUpDiamond()
    delete_item()

#-----------CREATE ENEMY--------------
def createEnemy():
    enemies1= canvas.create_image(900,150, image = enemy1, tags ='FISH')
    enemies2= canvas.create_image(900,400, image = enemy1, tags ='FISH')
    enemies3= canvas.create_image(900,650, image = enemy1, tags ='FISH')
    enemies4= canvas.create_image(1250,300, image = enemy6, tags ='FISH')
    enemies5= canvas.create_image(1250,570, image = enemy6, tags ='FISH')
    enemies6= canvas.create_image(1250,790, image = enemy6, tags ='FISH')
   
    def update_position_right():
        
        fish_coods = canvas.coords('FISH')
        if fish_coods[0]< 2000:
            canvas.itemconfigure(enemies1, image = enemy2)
            canvas.itemconfigure(enemies2, image = enemy2)
            canvas.itemconfigure(enemies3, image = enemy2)
            canvas.itemconfigure(enemies4, image = right1)
            canvas.itemconfigure(enemies5, image = right1)
            canvas.itemconfigure(enemies6, image = right1)
            canvas.move('FISH', 3, 0)
            window.after(20, update_position_right)
        else:
            update_position_left()
        
    def update_position_left():
        fish_coods = canvas.coords('FISH')
        if fish_coods[0]> -500 :
            canvas.itemconfigure(enemies1, image = enemy1)
            canvas.itemconfigure(enemies2, image = enemy1)
            canvas.itemconfigure(enemies3, image = enemy1)
            canvas.itemconfigure(enemies4, image = enemy6)
            canvas.itemconfigure(enemies5, image = enemy6)
            canvas.itemconfigure(enemies6, image = enemy6)
            canvas.move('FISH', -4, 0)
            window.after(20, update_position_left)
        else:
            update_position_right()
        
    window.after(20, update_position_right)


#------------SMALL FISH------------

def small_fishes():
    x3=100
    y3=50
    for i in range(1,10):
        fish_small= canvas.create_image(x3,y3, image = small_fish, tags= 'SMALLFISH')
        x3+=50
        y3+=(i+1)*30
    def update_position_right():
        fish_coods = canvas.coords("SMALLFISH")
        if fish_coods[0]< 2000:
            canvas.move("SMALLFISH", 5, 0)
            window.after(20, update_position_right)
        else:
            update_position_left()
        
    def update_position_left():
        fish_coods = canvas.coords("SMALLFISH")
        if fish_coods[0]> -500 :
            canvas.move("SMALLFISH", -6, 0)
            window.after(20, update_position_left)
        else:
            update_position_right()
        
    window.after(20, update_position_left)

#----------------create Diamond---------------
def createDiamond():
    DM1= canvas.create_image(1000,250, image = diamond1, tags= 'DM')
    DM2= canvas.create_image(1500,400, image = diamond1, tags = 'DM')
    DM3= canvas.create_image(1200,550, image = diamond1, tags = 'DM')
    def update_position_right():
        fish_coods = canvas.coords('DM')
        if fish_coods[0]< 2000:
            canvas.move('DM', 3, 0)
            window.after(20, update_position_right)
        else:
            update_position_left()
        
    def update_position_left():
        fish_coods = canvas.coords('DM')
        if fish_coods[0]> -500 :
            canvas.move('DM', -4, 0)
            window.after(20, update_position_left)
        else:
            update_position_right()
        
    window.after(20, update_position_right)

#-----------create cion--------------
def createCion():
    x=100
    y=200
    for i in range(1,10):
        COIN1= canvas.create_image(x,y, image = coin1, tags= 'COIN')
        COIN1= canvas.create_image(x+200,y+400, image = coin2, tags= 'COIN')
        x+=25
    def update_position_right():
        fish_coods = canvas.coords('COIN')
        if fish_coods[0]< 1500:
            canvas.move('COIN', 5, 0)
            window.after(20, update_position_right)
        else:
            update_position_left()
        
    def update_position_left():
        fish_coods = canvas.coords('COIN')
        if fish_coods[0]> -400 :
            canvas.move('COIN', -5, 0)
            window.after(20, update_position_left)
        else:
            update_position_right()
        
    window.after(20, update_position_left)

# -----------move bubble------------

def move_buuble():
    x=100
    y=900
    for i in range(1,6):
        canvas.create_image(x+900,y+150, image = bubble1, tags = 'BUBBLE')
        canvas.create_image(x,y, image = bubble2, tags = 'BUBBLE')
        canvas.create_image(x+500,y+100*(i), image = bubble3, tags = 'BUBBLE')
        x+=100
        y+=200
    def update_position_up():
        fish_coods = canvas.coords("BUBBLE")
        if fish_coods[1]< 300:
            canvas.move("BUBBLE", 0, 2)
            window.after(20, update_position_up)
        else:
            update_position_down()
        
    def update_position_down():
        fish_coods = canvas.coords("BUBBLE")
        if fish_coods[1]> 100 :
            canvas.move("BUBBLE", 0, -2)
            window.after(20, update_position_down)
        else:
            update_position_up()
        
    window.after(20, update_position_up)


#======================>PICK UP DIAMOND<========================

def pickUpDiamond():
    coord= canvas.coords(player)
    foods = canvas.find_withtag('DM')
    overlap = canvas.find_overlapping(coord[0], coord[1], coord[0]+actor.width(), coord[1]+actor.height())
    print(overlap)
    for food in foods:
        if food in overlap:
            return food
    return 0

def delete_item():
    shape = pickUpDiamond()
    if shape>0:
        canvas.delete(shape)
        canvas.itemconfigure(TotalCoin, Text =totalScore)
        totalScore+=1



#----------- Game Win ----------------
def gameWin():
    global isStart
    isStart = False
    canvas.delete('all')
    canvas.create_image(680,372, image=game_win)
    canvas.create_text(1200, 143, text=totalScore, font=("serif", 34 ,'bold'), fill="black")
    canvas.create_text(1200, 218, text=totalDiamond, font=("serif", 34 ,'bold'), fill="black")
    canvas.create_image(680,420, image=btn_continue, tags="continue")
    canvas.create_image(680,550,image=btn_exit, tags="exit")
    winsound.PlaySound("sounds/winner.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)


#--------------- Game over ---------------

def gameOver():
    global isStart
    isStart = False
    canvas.create_image(680, 372, image=game_over)
    canvas.create_text(1200, 143, text=getCoin, font=("serif", 34 ,'bold'), fill="black")
    canvas.create_text(1200, 218, text=totalScore, font=("serif", 34 ,'bold'), fill="black")
    canvas.create_image(680,570,image=btn_exit, tags="exit")
    winsound.PlaySound("sounds/over.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)


def gameContinue(event):
    canvas.delete("all")
    canvas.create_image(680, 372, image=btn_continue)
    canvas.create_image(140, 200, image=btn_back, tags="back")

#------------ Game Exit--------------
def gameExit(event):
    window.destroy()

#---------------Game Restart-----------
def gameRestart(event):
    global player_x, player_y,totalScore, totalDiamond, getCoin
    isStart = False
    player_x =150
    player_y = 450
    listOfDiamond=[]
    listOfCoin=[]
    listOfEnemy=[]
    listOfLife=[]
    totalScore = 0
    totalDiamond = 0
    getCoin=0
    canlive=6
    toConfig=0
    countCreateEnemy=0
    createEnemysSize = 0
    isStart = True
    gameStart(event)

#-----------Player Up-------------
def movePlayerUp(event):
    global player_y
    if player_y>130:
        player_y -=20
        canvas.moveto(player, player_x-80, player_y-70)

#------------Player Down------------
def movePlayerDown(event):
    global player_y
    if player_y<650:
        player_y+=20
        canvas.moveto(player, player_x-80, player_y-70)

# -----------move player left---------
def movePlayerleft(event):
    canvas.itemconfigure(player, image =actor1)

def movePlayerRight(event):
    canvas.itemconfigure(player, image =actor)


#========================> CREATE GAME SHOW ON WINDOW<===============================

canvas.create_image(680, 372, image=bg_start)
canvas.create_image(680, 150, image=menu)
canvas.create_image(680,330, image=btn_start, tags="startgame")
canvas.create_image(680,460,image=btn_continue, tags="continue")
canvas.create_image(680,590,image=btn_exit, tags="exit")
#--------put sound ----------
winsound.PlaySound("sounds/start.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)

processGame()

window.bind("<Up>", movePlayerUp)
window.bind("<Down>", movePlayerDown)
window.bind("<Left>", movePlayerleft)
window.bind("<Right>", movePlayerRight)
canvas.tag_bind("startgame","<Button-1>", gameStart)
canvas.tag_bind("replay","<Button-1>", gameContinue)
canvas.tag_bind("back","<Button-1>", gameShow)
canvas.tag_bind("exit","<Button-1>", gameExit)
canvas.tag_bind("back","<Button-1>", gameShow)

# ---------------------------------------------------------------------------
#=> MAIN ROOT
# ---------------------------------------------------------------------------
canvas.pack(expand=True, fill='both')
# def scroll_right():
#     canvas.xview('scroll', 1, 'units')

# def auto_scroll():
#     scroll_right()
#     window.after(100, auto_scroll)
# auto_scroll()
window.mainloop()
