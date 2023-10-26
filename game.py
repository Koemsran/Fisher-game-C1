import tkinter as tk
from tkinter import *
import winsound
from random import randrange
import time

# CREATE WIDTH AND HEIGHT ON WINDOW
SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 740

# CREATE THE MAIN WINDOW
window = tk.Tk()
window.geometry(str(SCREEN_WIDTH)+"x"+str(SCREEN_HEIGHT))

# THE TITTLE NAME OF GAME 
window.title('Group-C1 - Game Fish')
window.attributes('-fullscreen', True)
canvas = tk.Canvas(window)

#  .................................................. IMAGE ...............................................
# CREATE IMAGE DISPLAY BACKGROUND
game_start = tk.PhotoImage(file='images/bg/background.png')
bg_start = tk.PhotoImage(file='images/bg/bg.png')

# IMAGE DISPLAY CONDITION OF GAME
game_win = tk.PhotoImage(file='images/bg/game_win.png')
game_over = tk.PhotoImage(file='images/bg/game_over.png')
bg_level = tk.PhotoImage(file= 'images/bg/bg_level.png')

# IMAGE OF GAME LEVELS
game_level = tk.PhotoImage(file ='images/menus/level.png')
level_up = tk.PhotoImage(file= 'images/menus/level_up.png')
level1= tk.PhotoImage(file='images/menus/level1.png')
level2= tk.PhotoImage(file='images/menus/level2.png')
level3= tk.PhotoImage(file='images/menus/level3.png')

# IMAGE DISPLAY PLAYERS
actor = tk.PhotoImage(file='images/player1.png')
actor1 = tk.PhotoImage(file='images/player2.png')

# IMAGE DISPLAY FISH
enemy1 = tk.PhotoImage(file='images/enemies/enemy1.png')
enemy2 = tk.PhotoImage(file='images/enemies/enemy2.png')
enemy6 = tk.PhotoImage(file='images/enemies/enemy6.png')
small_fish = tk.PhotoImage(file='images/enemies/small_fish.png')
right1 = tk.PhotoImage(file='images/enemies/right1.png')

# IMAGE BUBBLE WATER FOR DISPLAY ANEMIES 
bubble1 = tk.PhotoImage(file='images/bubble1.png')
bubble2 = tk.PhotoImage(file='images/bubble2.png')
bubble3 = tk.PhotoImage(file='images/bubble3.png')

# CREATE IMAGE COIN LEVEL1 AND 2
coin1 = tk.PhotoImage(file='images/coin1.png')
coin2 = tk.PhotoImage(file='images/coin2.png')

# CREATE IMAGE DIAMONDS AND HEART 
diamond1 = tk.PhotoImage(file='images/diamond1.png')
diamond2 = tk.PhotoImage(file='images/diamond2.png')
heard1 = tk.PhotoImage(file='images/heard1.png')
heard2 = tk.PhotoImage(file='images/heard2.png')

# CREATE IMAGE DISPLAY MENU
menu = tk.PhotoImage(file='images/menus/menus 1.png')
btn_play = tk.PhotoImage(file='images/menus/play.png')
btn_restart = tk.PhotoImage(file='images/menus/restart.png')
btn_exit = tk.PhotoImage(file='images/menus/exit_menu.png')
btn_back = tk.PhotoImage(file='images/menus/back_menu.png')

# CREATE NAMES
player_x =700
player_y = 450
listOfLife = []
totalScore = 0
totalDiamond = 0
getCoin = 0
numberOfDiamond = 0
life = 6
isStart = True

# ---------------FUNCTION GAME-------------

#--------------PROCESS GAME------------------
def processGame():
    if numberOfDiamond == 3 and life != 0:
        gameWin()
    if life == 0:
        gameOver()
    canvas.after(100,processGame)


#===============================================>SHOW LEVEL GAME<==============================================
#---------BACKGROUND SHOWING----------
def levelGame(event):
    canvas.delete('all')
    
    canvas.create_image(680,372, image=bg_level)
    canvas.create_image(650,150, image=level_up)
    canvas.create_image(250,400, image=level1, tags='level1')
    canvas.create_image(670,400, image=level2, tags='level2')
    canvas.create_image(1100,400, image=level3, tags ='level3')
    canvas.create_image(100,70, image = btn_back, tags= 'back')

#-----------LEVEL1------------

def levelOne(event):
    global player, NumberDiamond, TotalCoin
    canvas.delete('all')
    canvas.create_image(680, 372,  image=game_start)
    player = canvas.create_image(player_x, player_y, image=actor)
    Level1 = canvas.create_text(400, 70, text="Level: 1", font=("serif", 20 ,'bold'), fill="black")
    Numberdiamond = canvas.create_text(560, 70, text=": "+str(totalDiamond), font=("serif", 20 ,'bold'), fill="black")
    TotalCoin = canvas.create_text(760, 70, text=': '+str(totalScore), font=("serif", 20 ,'bold'), fill="black")

    canvas.create_image(100,70, image = btn_back, tags= 'back')

    # DISPLAY SOUND IN TO GAME
    winsound.PlaySound("sounds/playing.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)

    canvas.create_image(520, 65, image = diamond1)
    id=canvas.create_image(720, 65, image = coin2)
    for i in range(5):
        life_actor = canvas.create_image(1150 + i * 37, 60, image=heard1)
        listOfLife.append(life_actor)


# ===================CALL FUNCTION HERE<=================
#---START THE SIMULATION----
    createEnemy()
    createDiamond()
    move_buuble()
    createCion()
    pickUpDiamond()
    delete_item()


#-------------------LEVEL2--------------------
def levelTwo(event):
    global player, NumberDiamond, TotalCoin
    canvas.delete('all')
    canvas.create_image(680, 372,  image=game_start)
    player = canvas.create_image(player_x, player_y, image=actor, tags = 'player')
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
#---START THE SIMULATION----
    createEnemy()
    createDiamond()
    # small_fishes()
    move_buuble()
    createCion()
    pickUpDiamond()
    delete_item()
    anemyLevelTwo()


#-------------------LEVEL3------------------
def levelThree(event):
    global player, NumberDiamond, TotalCoin
    canvas.delete('all')
    canvas.create_image(680, 372,  image=game_start)
    player = canvas.create_image(player_x, player_y, image=actor, tags = 'player')
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
#---START THE SIMULATION----
    createEnemy()
    createDiamond()
    move_buuble()
    createCion()
    pickUpDiamond()
    delete_item()
    anemyLevelThree()



#--------------GAME SHOW--------------
def gameShow(event):
    canvas.delete('all')
    canvas.create_image(680,372, image= bg_start)
    canvas.create_image(680, 100, image=menu, tags= 'menu')
    canvas.create_image(680,280, image=btn_play, tags="playgame")
    canvas.create_image(680,410,image=btn_restart, tags="restart")
    canvas.create_image(680,540,image=btn_exit, tags="exit")
    winsound.PlaySound("sounds/start.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)

#---------------GAME RESTART--------------   
def reStart(event):
    global player, NumberDiamond, TotalCoin
    canvas.delete('all')
    canvas.create_image(680, 372,  image=game_start)
    player = canvas.create_image(player_x, player_y, image=actor, tags = 'player')
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
#---START THE SIMULATION----
    createEnemy()
    createDiamond()
    move_buuble()
    createCion()
    pickUpDiamond()
    delete_item()

#-----------CREATE FUNCTION TO UPDATE THE OBJECT ENEMY DISPLAY ON BACKGROUND--------------
def createEnemy():
    enemies1= canvas.create_image(900,150, image = enemy1, tags ='FISH')
    enemies2= canvas.create_image(900,400, image = enemy1, tags ='FISH')
    enemies3= canvas.create_image(900,650, image = enemy1, tags ='FISH')
    enemies4= canvas.create_image(1250,300, image = enemy6, tags ='FISH')
    enemies5= canvas.create_image(1250,570, image = enemy6, tags ='FISH')
    enemies6= canvas.create_image(1250,790, image = enemy6, tags ='FISH')
   
#----------------------------GO RIGHT FUNCTION-------------------------------------------------
# FUNCTION TO UPDATE THE OBJECT POSITION
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

# FUNCTION TO UPDATE THE OBJECT POSITION
#--------------------------------------GO LEFT FUNCTION------------------------------------------      
    def update_position_left():
        fish_coods = canvas.coords('FISH')
        if fish_coods[0] > -500:
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


#--------------------------------------FUNCTION SPEED OF SMALL FISH----------------------------------

def small_fishes():
    x3 = 100
    y3 = 50
    for i in range(1,10):
        fish_small= canvas.create_image(x3,y3, image = small_fish, tags= 'SMALLFISH')
        x3 += 50
        y3 += (i+1)*30
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


#----------------CREATE DIAMOND DISPLAY ON BACKGROUND---------------
# FUNCTION TO CREATE THE OBJECT DIAMOND
def createDiamond():
    DM1 = canvas.create_image(1000,250, image = diamond1, tags= 'DM')
    DM2 = canvas.create_image(1500,400, image = diamond1, tags = 'DM')
    DM3 = canvas.create_image(1200,550, image = diamond1, tags = 'DM')
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


#------------------CREATE ICONS FOR CHECK CONDITION-----------------------
# FUNCTION TO CREATE THE OBJECT CIONS
def createCion():
    x = 100
    y = 200
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

# ------------------MOVE BUBBLE---------------------
# FUNCTION TO MOVE THE OBJECT BUBBLEP
def move_buuble():
    x = 100
    y = 900
    for i in range(1,6):
        canvas.create_image(x+900,y+150, image = bubble1, tags = 'BUBBLE')
        canvas.create_image(x,y, image = bubble2, tags = 'BUBBLE')
        canvas.create_image(x+500,y+100*(i), image = bubble3, tags = 'BUBBLE')
        x += 100
        y += 200
    def update_position_up():
        fish_coods = canvas.coords("BUBBLE")
        if fish_coods[1] < 300:
            canvas.move("BUBBLE", 0, 2)
            window.after(20, update_position_up)
        else:
            update_position_down()
        
    def update_position_down():
        fish_coods = canvas.coords("BUBBLE")
        if fish_coods[1] > 100 :
            canvas.move("BUBBLE", 0, -2)
            window.after(20, update_position_down)
        else:
            update_position_up()
        
    window.after(20, update_position_up)

#------------ENEMY LEVEL 2-------------------
def anemyLevelTwo():
    enemies1=canvas.create_image(100,100, image = enemy1, tags= 'ENEMY')
    enemies2=canvas.create_image(100,400, image = enemy1, tags= 'ENEMY')
    enemies3=canvas.create_image(100,700, image = enemy1, tags= 'ENEMY')

    def update_position_right():
        
        fish_coods = canvas.coords('ENEMY')
        if fish_coods[0] < 2000:
            canvas.itemconfigure(enemies1, image = enemy2)
            canvas.itemconfigure(enemies2, image = enemy2)
            canvas.itemconfigure(enemies3, image = enemy2)
            canvas.move('ENEMY', 2, 0)
            window.after(20, update_position_right)
        else:
            update_position_left()

#--------------------------------------GO LEFT FUNCTION------------------------------------------      
    def update_position_left():
        fish_coods = canvas.coords('ENEMY')
        if fish_coods[0] > -100 :
            canvas.itemconfigure(enemies1, image = enemy1)
            canvas.itemconfigure(enemies2, image = enemy1)
            canvas.itemconfigure(enemies3, image = enemy1)
            canvas.move('ENEMY', -2, 0)
            window.after(20, update_position_left)
        else:
            update_position_right()
        
    window.after(20, update_position_left)

#------------ENEMY LEVEL 3-------------------
def anemyLevelThree():
    enemies1=canvas.create_image(100,100, image = enemy1, tags= 'ENEMY')
    enemies2=canvas.create_image(100,400, image = enemy1, tags= 'ENEMY')
    enemies3=canvas.create_image(100,700, image = enemy1, tags= 'ENEMY')

    def update_position_right():
        
        fish_coods = canvas.coords('ENEMY')
        if fish_coods[0] < 1500:
            canvas.itemconfigure(enemies1, image = enemy2)
            canvas.itemconfigure(enemies2, image = enemy2)
            canvas.itemconfigure(enemies3, image = enemy2)
            canvas.move('ENEMY', 7, 0)
            window.after(20, update_position_right)
        else:
            update_position_left()

#--------------------------------------GO LEFE FUNCTION------------------------------------------      
    def update_position_left():
        fish_coods = canvas.coords('ENEMY')
        if fish_coods[0] > -100 :
            canvas.itemconfigure(enemies1, image = enemy1)
            canvas.itemconfigure(enemies2, image = enemy1)
            canvas.itemconfigure(enemies3, image = enemy1)
            canvas.move('ENEMY', -7, 0)
            window.after(20, update_position_left)
        else:
            update_position_right()
        
    window.after(20, update_position_left)

#======================>PICK UP DIAMOND FUNCTION<========================
# FUNCTION TO PICK UP THE OBJECT DIAMOND
def pickUpDiamond():
    global player
    coord= canvas.coords(player)
    foods = canvas.find_withtag('DM')
    print(foods)
    overlap = canvas.find_overlapping(coord[0], coord[1], coord[0]+actor.width(), coord[1]+actor.height())
    print(overlap)
    for food in foods:
        if food in overlap:
            return food
    return 0
score = 0
def delete_item():
    shape = pickUpDiamond()
    if shape > 0:
        canvas.delete(shape)
        score += 1
        canvas.itemconfigure(totalDiamond, Text =': '+str(score))
        
#======================>PICK UP COIN<========================

# def pickUpCoin():
#     global player
#     coord= canvas.coords(player)
#     print(coord[0])
#     foods = canvas.find_withtag('COIN')
#     print(foods)
#     overlap = canvas.find_overlapping(coord[0], coord[1], coord[0]+actor.width(), coord[1]+actor.height())
#     print(overlap)
#     for food in foods:
#         if food in overlap:
#             return food
#     return 0
# scoreCion
# def delete_item():
#     shape = pickUpCoin()
#     if shape>0:
#         canvas.delete(shape)
#         scoreCoin+=1
#         canvas.itemconfigure(TotalCoin, Text =Text =': '+str(scoreCion))

#======================>TOUCH ENEMY<========================

# def touchEnemy():
#     global player
#     coord= canvas.coords(player)
#     print(coord[0])
#     foods = canvas.find_withtag('FISH')
#     print(foods)
#     overlap = canvas.find_overlapping(coord[0], coord[1], coord[0]+actor.width(), coord[1]+actor.height())
#     print(overlap)
#     for food in foods:
#         if food in overlap:
#             return food
#     return 0

# def delete_item():
#     global life
#     shape = touchEnemy()
#     if shape>0:
#         life-=1
#         canvas.itemconfigure

        
#------------------------------------ GMAE WIN FUNCTION--------------------------------------------
def gameWin():
    global isStart
    isStart = False
    canvas.delete('all')
    canvas.create_image(680,372, image=game_win)
    canvas.create_text(1200, 143, text=totalScore, font=("serif", 34 ,'bold'), fill="black")
    canvas.create_text(1200, 218, text=totalDiamond, font=("serif", 34 ,'bold'), fill="black")
    canvas.create_image(680,420, image=btn_restart, tags="continue")
    canvas.create_image(680,550,image=btn_exit, tags="exit")
    winsound.PlaySound("sounds/winner.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)


#--------------------------------- GAME OVER FUNCTION ---------------------------------------------
def gameOver():
    global isStart
    isStart = False
    canvas.create_image(680, 372, image=game_over)
    canvas.create_text(1200, 143, text=getCoin, font=("serif", 34 ,'bold'), fill="black")
    canvas.create_text(1200, 218, text=totalScore, font=("serif", 34 ,'bold'), fill="black")
    canvas.create_image(680,570,image=btn_exit, tags="exit")
    winsound.PlaySound("sounds/over.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)


#------------ ----------------------GAME EXIT-------------------------------------
def gameExit(event):
    window.destroy()

#-----------------------------------------GAME RESTART FUNCTION---------------------------------
def gameRestart(event):
    global player_x, player_y,totalScore, totalDiamond, getCoin
    isStart = False
    player_x = 150
    player_y = 450
    listOfDiamond = []
    listOfCoin = []
    listOfEnemy = []
    listOfLife = []
    totalScore = 0
    totalDiamond = 0
    getCoin = 0
    canlive = 6
    toConfig = 0
    countCreateEnemy = 0
    createEnemysSize = 0
    isStart = True
    reStart(event)

#---------------------------------PLAYER UP FUNCTION ------------------------------------------
def movePlayerUp(event):
    global player_y
    if player_y>130:
        player_y -= 20
        canvas.moveto(player, player_x-80, player_y-70)

#---------------------------PLAYER DOWN FUNCTION--------------------------------------------
def movePlayerDown(event):
    global player_y
    if player_y<650:
        player_y += 20
        canvas.moveto(player, player_x-80, player_y-70)

# ----------------------------MOVE PLAYER LET FUNCTION------------------------------------------
def movePlayerleft(event):
    canvas.itemconfigure(player, image = actor1)

def movePlayerRight(event):
    canvas.itemconfigure(player, image = actor)


#========================> CREATE GAME SHOW ON WINDOW<===============================

canvas.create_image(680, 372, image=bg_start)
canvas.create_image(680, 150, image=menu)
canvas.create_image(680,330, image=btn_play, tags="playgame")
canvas.create_image(680,460,image=btn_restart, tags="restart")
canvas.create_image(680,590,image=btn_exit, tags="exit")
winsound.PlaySound("sounds/start.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)

# Start the simulation
processGame()

window.bind("<Up>", movePlayerUp)
window.bind("<Down>", movePlayerDown)
window.bind("<Left>", movePlayerleft)
window.bind("<Right>", movePlayerRight)
canvas.tag_bind("back","<Button-1>", gameShow)
canvas.tag_bind("exit","<Button-1>", gameExit)
canvas.tag_bind("playgame","<Button-1>", levelGame)
canvas.tag_bind("level1","<Button-1>", levelOne)
canvas.tag_bind("level2","<Button-1>", levelTwo)
canvas.tag_bind("level3","<Button-1>", levelThree)
canvas.tag_bind("restart","<Button-1>", reStart)
# ---------------------------------------------------------------------------
#=> MAIN WINDOW
# ---------------------------------------------------------------------------
canvas.pack(expand=True, fill='both')


# RUN THE TKINTER MAIN LOOP
window.mainloop()
