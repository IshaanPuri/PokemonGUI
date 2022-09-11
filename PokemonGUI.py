#Imports
from tkinter import *
from tkinter import messagebox
import random
import time

def snakeLogic():
    #Global Variables
    global square
    global placeholder
    global squareLabel
    global game
    global diceLabel

    #Roll is the dice roll value, randomized from 1-6
    roll = random.randint(1,6)


    diceLabel = Label(game, text = "Your rolled a:" + str(roll), fg= 'black')
    diceLabel.place(x=770,y=400)
    diceLabel.config(font=("Courier", 15))

    #Square becomes equal to old square value plus roll
    square +=roll

   #If Statements, depending on the value of square the position of the placeholder will change
    if square ==  1:
        placeholder.place(x=50, y=650)

    elif square ==  2:
        placeholder.place(x=180, y=650)

    elif square == 3:
        placeholder.place(x=290, y=220)
        square = 22

    elif square ==  4:
        placeholder.place(x=430, y=650)

    elif square ==  5:
        placeholder.place(x=550, y=540)
        square = 8

    elif square ==  6:
        placeholder.place(x=680, y=650)


    elif square ==  7:
        placeholder.place(x=680, y=540)

    elif square ==  8:
        placeholder.place(x=550, y=540)

    elif square == 9:
        placeholder.place(x=430, y=540)

    elif square ==  10:
        placeholder.place(x=290, y=540)

    elif square ==  11:
        placeholder.place(x=180, y=50)
        square = 26

    elif square ==  12:
        placeholder.place(x=50, y=540)


    elif square ==  13:
         placeholder.place(x=50, y=340)

    elif square ==  14:
        placeholder.place(x=180, y=340)

    elif square == 15:
        placeholder.place(x=290, y=340)

    elif square ==  16:
        placeholder.place(x=430, y=340)

    elif square ==  17:
        placeholder.place(x=430, y=650)
        square = 4

    elif square ==  18:
        placeholder.place(x=680, y=340)


    elif square ==  19:
        placeholder.place(x=680, y=540)
        square = 7

    elif square ==  20:
        placeholder.place(x=550, y=50)
        square = 29

    elif square == 21:
        placeholder.place(x=430, y=540)
        square = 9

    elif square ==  22:
        placeholder.place(x=290, y=220)

    elif square ==  23:
        placeholder.place(x=180, y=220)

    elif square ==  24:
        placeholder.place(x=50, y=220)
        

    elif square ==  25:
        placeholder.place(x=50, y=50)

    elif square ==  26:
        placeholder.place(x=180, y=50)

    elif square == 27:
        placeholder.place(x=50, y=650)
        square = 1

    elif square ==  28:
        placeholder.place(x=430, y=50)

    elif square ==  29:
        placeholder.place(x=550, y=50)
        
    #squareLabel is changed depending on the new  value of square
    squareLabel.config(text="Your on Square:" + str(square))

    #If square == 30 player wins
    if square ==  30:
        placeholder.place(x=680, y=50)
        messagebox.showinfo('GOOD JOB', 'YOU WON, Open the Python shell and Press yes, PLEASE Open the Application and Play Again')
        time.sleep(1)
        game.destroy()
        exit()
        

        
    #If square is equal to more than 30 the user will start back at square 1
    if square > 30:
        placeholder.place(x=50, y=650)
        square = 1




def snakeLadder():
    #Global Variables
    global square
    global placeholder
    global squareLabel
    global game
    global diceLabel


    #Snakes and Ladders game screen

    menu.destroy()
    game = Tk()
    game.title("Pokemon Snakes and Ladders")
    game.geometry('1000x750')
    game.resizable(False, False)
    game.configure(background='white')

    board = PhotoImage(file='board.png')
    snakeBoard = Label(game, image=board)
    snakeBoard.place(x=0, y=0)


    dices = PhotoImage(file='dice.png')
    
    die = Button(game, image = dices, command = snakeLogic)
    die.place(x=770, y=0)

    #Square variable
    square = 1

    playerIcon = PhotoImage(file='pika.png')

    placeholder = Label(game, image=playerIcon)
    placeholder.place(x=50, y=650)
    
    #squareLabel tells the user what square they are on, they label changes everytime a dice is rolled
    squareLabel = Label(game, text = "Your on Square:" + str(square), fg= 'black')
    squareLabel.place(x=770,y=300)
    squareLabel.config(font=("Courier", 15))

    diceLabel = Label(game, text = "Your rolled a:", fg= 'black')
    diceLabel.place(x=770,y=400)
    diceLabel.config(font=("Courier", 15))


    pokemooon=PhotoImage(file='groudon.png')
    pokeDude = Label(game, image=pokemooon)
    pokeDude.place(x=860, y=645)



    game.mainloop()

    
    

#Functon that triggers new screen to
def moves1():
    #Globas
    global oppRealhp
    global hp
    global hpLabel2
    global hpLabel
    global stadium

    #The damage variable is randomized from 1-45
    #Opponent hp is decreased based on the value of the damage variable

    damage1 = random.randint(1,45)
    oppRealhp -= damage1
    hpLabel2.config(text = "Opponent HP:" + str(oppRealhp))

    #The opponent  damage variable is randomized from 1-45
    #the user's hp is decreased based on the value of the opponent damage variable

    oppDamage1 = random.randint(1,45)
    hp -= oppDamage1
    #label is changed when either  hp value changes
    hpLabel.config(text = "Your HP:" + str(hp))

    #If opponent hp is below 0 you win
    if oppRealhp <= 0:
        stadium.destroy()
        messagebox.showinfo('GOOD JOB', 'YOU WON, Please Open the Application and Play Again')

    
    #If the user's hp is below 0 you lose
    if hp <= 0:
        stadium.destroy()
        messagebox.showinfo('HAHA LOSER', 'YOU LOST, Please Open the Application and Play Again')

    #***THESE COMMENTS APPLY TO ALL 4 MOVES FUNCTIONS***
    

        
    

def moves2():
    #Globals
    global oppRealhp
    global hp
    global hpLabel2
    global hpLabel
    global stadium

    damage2 = random.randint(1,45)
    oppRealhp -= damage2
    hpLabel2.config(text = "Opponent HP:" + str(oppRealhp))

    oppDamage2 = random.randint(1,45)
    hp -= oppDamage2
    hpLabel.config(text = "Your HP:" + str(hp))


    if oppRealhp <= 0:
        stadium.destroy()
        messagebox.showinfo('GOOD JOB', 'YOU WON, Please Open the Application and Play Again')

    if hp <= 0:
        stadium.destroy()
        messagebox.showinfo('HAHA LOSER', 'YOU LOST, Please Open the Application and Play Again')

        

def moves3():
    #Globals
    global oppRealhp
    global hp
    global hpLabel2
    global hpLabel
    global stadium

    damage3 = random.randint(1,45)
    oppRealhp -= damage3
    hpLabel2.config(text = "Opponent HP:" + str(oppRealhp))

    oppDamage3 = random.randint(1,45)
    hp -= oppDamage3
    hpLabel.config(text = "Your HP:" + str(hp))


    if oppRealhp <= 0:
        stadium.destroy()
        messagebox.showinfo('GOOD JOB', 'YOU WON, Please Open the Application and Play Again')

    if hp <= 0:
        stadium.destroy()
        messagebox.showinfo('HAHA LOSER', 'YOU LOST, Please Open the Application and Play Again')


                                
        
def moves4():
    #Globals
    global oppRealhp
    global hp
    global hpLabel2
    global hpLabel
    global stadium

    damage4 = random.randint(1,45)
    oppRealhp -= damage4
    hpLabel2.config(text = "Opponent HP:" + str(oppRealhp))


    oppDamage4 = random.randint(1,45)
    hp -= oppDamage4
    hpLabel.config(text = "Your HP:" + str(hp))



    if oppRealhp <= 0:
        stadium.destroy()
        messagebox.showinfo('GOOD JOB', 'YOU WON, Please Open the Application and Play Again')

    elif hp <= 0:
        stadium.destroy()
        messagebox.showinfo('HAHA LOSER', 'YOU LOST, Please Open the Application and Play Again')

    
def game1():
    #Global Variables
    global choose
    global oppRealhp
    global hpLabel2
    global hpLabel
    global stadium
    global hp

    #Game Screen
    choose.destroy()
    stadium = Tk()
    stadium.title("Pokemon Arena Battle")
    stadium.geometry('1000x750')
    stadium.resizable(False, False)
    stadium.configure(background='black')

    #Hp variable is player remaining help
    hp = 100


    backarena = PhotoImage(file='arena2.png')
    background_label4 = Label(stadium, image=backarena)
    background_label4.place(x=227, y=0)

    box = PhotoImage(file='dialoguebox.png')
    textBox = Label(stadium, image=box)
    textBox.place(x=20, y=570)

    #hpLabel tells the player their remaining their remaining hp, will be updated in the moves functions
    hpLabel = Label(stadium, text = "Your HP:" + str(hp), fg= 'black', borderwidth=0, highlightthickness=0)
    hpLabel.place(x=150,y=620)
    hpLabel.config(font=("Courier", 20))

    yourPlayer = PhotoImage(file='player.png')
    player = Label(stadium, image=yourPlayer)
    player.place(x=595, y=490)

    waterStats = PhotoImage(file='kyogstats.png')
    waterStatistics = Label(stadium, image=waterStats)
    waterStatistics.place(x=550, y=570)

    otherPlayer = PhotoImage(file='opponent.png')
    player2 = Label(stadium, image=otherPlayer)
    player2.place(x=834, y=495)
                           
    character = PhotoImage(file='player1.png')
    maper = Label(stadium, image=character)
    maper.place(x=234, y=312)

    titleMoves = PhotoImage(file='moves.png')
    moves = Label(stadium, image=titleMoves)
    moves.place(x=5, y=0)

    #The players opponent pokemon will be decided by a 1-3 number randomizer
    opponent = random.randint(1,3)
    #Opphp is declared to be 0
    oppHp = 0
    if opponent == 1:
        #If opponent is 1 then the player will play the water Pokemon
        #The oppRealhp variable is created
        oppStats = PhotoImage(file='kyogstats.png')
        oppRealhp = oppHp + 100
        oppPic = PhotoImage(file='opp1.png')
        opp = Label(stadium, image=oppPic)
        opp.place(x=700, y=150)
        


    if opponent == 2:
        #If opponent is 2 player plays against charizard
        oppStats = PhotoImage(file='charstats.png')
        oppRealhp = oppHp + 78
        oppPic = PhotoImage(file='opp2.png')
        opp = Label(stadium, image=oppPic)
        opp.place(x=755, y=75)

    if opponent == 3:
        #If opponent is 3 player plays grass Pokemon
        oppStats = PhotoImage(file='rayqstats.png')
        oppRealhp = oppHp + 105
        oppPic = PhotoImage(file='opp3.png')
        opp = Label(stadium, image=oppPic)
        opp.place(x=755, y=75)


    oppStatistics = Label(stadium, image=oppStats)
    oppStatistics.place(x=810, y=570)

    hpLabel2 = Label(stadium, text = "Opponent HP:" + str(oppRealhp), fg= 'black')
    hpLabel2.place(x=125,y=650)
    hpLabel2.config(font=("Courier", 20))
        
        
    #Moves buttons
    move1 = Button(stadium, text="Aqua Tail", command = moves1)
    move1.place(x=82, y=150)

    move2 = Button(stadium, text="Hydro Pump", command = moves2)
    move2.place(x=82, y=200)

    move3 = Button(stadium, text="Scary Face", command = moves3)
    move3.place(x=82, y=250)

    move4 = Button(stadium, text="Muddy Water", command = moves4)
    move4.place(x=82, y=300)




    stadium.mainloop()

def game2():
    #Global Variables
    global choose
    global oppRealhp
    global hpLabel2
    global hpLabel
    global stadium
    global hp

    
    choose.destroy()
    stadium = Tk()
    stadium.title("Pokemon Arena Battle")
    stadium.geometry('1000x750')
    stadium.resizable(False, False)
    stadium.configure(background='black')
    #hp variable is the health for the variable
    hp = 78

    backarena2 = PhotoImage(file='arena2.png')
    background_label5 = Label(stadium, image=backarena2)
    background_label5.place(x=227, y=0)

    box2 = PhotoImage(file='dialoguebox.png')
    textBox2 = Label(stadium, image=box2)
    textBox2.place(x=20, y=570)

    #hpLabel indicates the hp of the player
    hpLabel = Label(stadium, text = "Your HP:" + str(hp), fg= 'black', borderwidth=0, highlightthickness=0)
    hpLabel.place(x=150,y=620)
    hpLabel.config(font=("Courier", 20))

    yourPlayer = PhotoImage(file='player.png')
    player = Label(stadium, image=yourPlayer)
    player.place(x=595, y=490)

    firePic = PhotoImage(file='charstats.png')
    fireImage = Label(stadium, image=firePic)
    fireImage.place(x=550, y=570)

    otherPlayer = PhotoImage(file='opponent.png')
    player2 = Label(stadium, image=otherPlayer)
    player2.place(x=834, y=495)
                           
    character = PhotoImage(file='player2.png')
    maper = Label(stadium, image=character)
    maper.place(x=250, y=130)

    titleMoves = PhotoImage(file='moves.png')
    moves = Label(stadium, image=titleMoves)
    moves.place(x=5, y=0)

    #Opponent determines who the player plays
    opponent = random.randint(1,3)

    #Temporary opponent hp variable
    oppHp = 0
    if opponent == 1:
        #If opponent is 1 then the player will play the water Pokemon
        oppStats = PhotoImage(file='kyogstats.png')
        oppRealhp = oppHp + 100
        oppPic = PhotoImage(file='opp1.png')
        opp = Label(stadium, image=oppPic)
        opp.place(x=700, y=150)
        


    if opponent == 2:
        #If opponent is 2 player plays against charizard
        oppStats = PhotoImage(file='charstats.png')
        oppRealhp = oppHp + 78
        oppPic = PhotoImage(file='opp2.png')
        opp = Label(stadium, image=oppPic)
        opp.place(x=755, y=75)

    if opponent == 3:
        #If opponent is 3 player plays grass Pokemon
        oppStats = PhotoImage(file='rayqstats.png')
        oppRealhp = oppHp + 105
        oppPic = PhotoImage(file='opp3.png')
        opp = Label(stadium, image=oppPic)
        opp.place(x=755, y=75)


    oppStatistics = Label(stadium, image=oppStats)
    oppStatistics.place(x=810, y=570)

    hpLabel2 = Label(stadium, text = "Opponent HP:" + str(oppRealhp), fg= 'black')
    hpLabel2.place(x=125,y=650)
    hpLabel2.config(font=("Courier", 20))
        
        
    #Moves buttons
    move1 = Button(stadium, text="Fire Blast", command = moves1)
    move1.place(x=82, y=150)

    move2 = Button(stadium, text="Dragon Claw", command = moves2)
    move2.place(x=82, y=200)

    move3 = Button(stadium, text="Overheat", command = moves3)
    move3.place(x=82, y=250)

    move4 = Button(stadium, text="Flamethrower", command = moves4)
    move4.place(x=82, y=300)

    stadium.mainloop()


def game3():
    #Global Variables
    global choose
    global oppRealhp
    global hpLabel2
    global hpLabel
    global stadium
    global hp

    choose.destroy()
    stadium = Tk()
    stadium.title("Pokemon Arena Battle")
    stadium.geometry('1000x750')
    stadium.resizable(False, False)
    stadium.configure(background='black')
    #Hp variable indicates the health of the player
    hp = 105


    backarena = PhotoImage(file='arena2.png')
    background_label4 = Label(stadium, image=backarena)
    background_label4.place(x=227, y=0)

    box = PhotoImage(file='dialoguebox.png')
    textBox = Label(stadium, image=box)
    textBox.place(x=20, y=570)

    hpLabel = Label(stadium, text = "Your HP:" + str(hp), fg= 'black', borderwidth=0, highlightthickness=0)
    hpLabel.place(x=150,y=620)
    hpLabel.config(font=("Courier", 20))

    yourPlayer = PhotoImage(file='player.png')
    player = Label(stadium, image=yourPlayer)
    player.place(x=595, y=490)

    grassStats = PhotoImage(file='rayqstats.png')
    grassStatistics = Label(stadium, image=grassStats)
    grassStatistics.place(x=550, y=570)

    otherPlayer = PhotoImage(file='opponent.png')
    player2 = Label(stadium, image=otherPlayer)
    player2.place(x=834, y=495)
                           
    character = PhotoImage(file='player3.png')
    maper = Label(stadium, image=character)
    maper.place(x=280, y=50)

    titleMoves = PhotoImage(file='moves.png')
    moves = Label(stadium, image=titleMoves)
    moves.place(x=5, y=0)

    #Opponent will determine who the player plays against
    opponent = random.randint(1,3)
    
    oppHp = 0
    if opponent == 1:
        #If the variable 1 on the player plays against the water pokemon
        oppStats = PhotoImage(file='kyogstats.png')
        oppRealhp = oppHp + 100
        oppPic = PhotoImage(file='opp1.png')
        opp = Label(stadium, image=oppPic)
        opp.place(x=700, y=150)
        


    if opponent == 2:
        #If the variable 2 on the player plays against the fire pokemon
        oppStats = PhotoImage(file='charstats.png')
        oppRealhp = oppHp + 78
        oppPic = PhotoImage(file='opp2.png')
        opp = Label(stadium, image=oppPic)
        opp.place(x=755, y=75)

    if opponent == 3:
        #If the variable 3 on the player plays against the grass pokemon

        oppStats = PhotoImage(file='rayqstats.png')
        oppRealhp = oppHp + 105
        oppPic = PhotoImage(file='opp3.png')
        opp = Label(stadium, image=oppPic)
        opp.place(x=755, y=75)


    oppStatistics = Label(stadium, image=oppStats)
    oppStatistics.place(x=810, y=570)

    hpLabel2 = Label(stadium, text = "Opponent HP:" + str(oppRealhp), fg= 'black')
    hpLabel2.place(x=125,y=650)
    hpLabel2.config(font=("Courier", 20))
        
        
    #Moves buttons
    move1 = Button(stadium, text="Hyper Voice", command = moves1)
    move1.place(x=82, y=150)

    move2 = Button(stadium, text="Air Slash", command = moves2)
    move2.place(x=82, y=200)

    move3 = Button(stadium, text="Hyper Beam", command = moves3)
    move3.place(x=82, y=250)

    move4 = Button(stadium, text="Extreme Speed", command = moves4)
    move4.place(x=82, y=300)


    stadium.mainloop()

     
def start():
    #Global Variables
    global choose

    menu.destroy()

#Character selection screen
    choose = Tk()
    choose.title("Choose Your Character")
    choose.geometry('552x500')
    choose.resizable(False, False)

    choose.configure(background='black')

    #Depending on which character is pressed the game def will be different
    poke1= PhotoImage(file='kyogchoose.png')
    water = Button(choose, image = poke1, command = game1)
    water.place(x=0, y=0)

    poke2= PhotoImage(file='charchoose.png')
    fire = Button(choose, image = poke2, command = game2)
    fire.place(x=184, y=0)

    poke3= PhotoImage(file='raquchoose.png')
    grass = Button(choose, image = poke3, command = game3)
    grass.place(x=368, y=0)

    messagebox.showinfo('CHOOSE YOUR CHARACTER', 'CHOOSE YOUR CHARACTER WISELY')


    choose.mainloop()

    
def helping():
    #Global Variables
    global back
    global instructions
    global menu
    

    menu.destroy()

    #Instructions screen
    instructions = Tk()
    instructions.title("Pokemon Instructions")
    instructions.geometry('1000x750')
    instructions.resizable(False, False)

    back = PhotoImage(file='back.png')
    
    background_image3 = PhotoImage(file='background3.png')
    background_label3 = Label(instructions, image=background_image3)
    background_label3.place(x=0, y=0, relwidth=1, relheight=1)


    torra = PhotoImage(file='torterra.png')
    torterra = Label(instructions, image=torra)
    torterra.place(x=520, y=500)


    back1 = Button(instructions, image = back, command = halp)
    back1.place(x=900, y=695)

    instructimage = PhotoImage(file='howto.png')
    instructtext = Label(instructions, image=instructimage)
    instructtext.place(x=0, y=0)


    titler = PhotoImage(file='instructions.png')
    titleText = Label(instructions, image = titler)
    titleText.place(x=412, y=0)


    instructions.mainloop()

def halp():
    #Global Variables
    global instructions
    #Makes the player go back to the main menu after pressing the back button
    instructions.destroy()
    play()


def pokeLists():
    #Global Variables
    global poke

    menu.destroy()

    poke = Tk()
    poke.title("POKEDEX")
    poke.geometry('1000x750')
    poke.resizable(False, False)
    #Pokedex screen
    
    #Makes the background black
    poke.configure(background='black')

    back = PhotoImage(file='back.png')

    #Below are labels that represent an image that is stats for each pokemon

    #BackButton
    backBut = Button(poke, image = back, command = back2)
    backBut.place(x=900, y=695)

    pokeTitle = PhotoImage(file='pokedex.png')
    pokeTitlee = Label(poke, image=pokeTitle)
    pokeTitlee.place(x=350, y=0)


    charzStats = PhotoImage(file='charstats.png')
    charStatistics = Label(poke, image=charzStats)
    charStatistics.place(x=100, y=100)

    firePic = PhotoImage(file='charizard.png')
    fireImage = Label(poke, image=firePic)
    fireImage.place(x=30, y=300)


    waterStats = PhotoImage(file='kyogstats.png')
    waterStatistics = Label(poke, image=waterStats)
    waterStatistics.place(x=425, y=100)

    waterPic = PhotoImage(file='kyogre.png')
    waterImage = Label(poke, image=waterPic)
    waterImage.place(x=350, y=300)

    grassStats = PhotoImage(file='rayqstats.png')
    grassStatistics = Label(poke, image=grassStats)
    grassStatistics.place(x=750, y=100)

    grassPic = PhotoImage(file='rayquaza.png')
    grassImage = Label(poke, image=grassPic)
    grassImage.place(x=670, y=300)


    poke.mainloop()


def back2():
    #Global variable
    #Back button, reloads the main menu
    global poke
    poke.destroy()
    play()


def play():
    #Global Variables
    global menu
    global login
    global off
    global login

    #If statement to make sure login destroy is only repeated once
    if off:
        login.destroy()
        off = False

    #Main menu of the program
    menu = Tk()
    menu.title("Pokemon Main Menu")
    menu.geometry('1107x683')
    menu.resizable(False, False)

    #Screen Background
    background_image2 = PhotoImage(file='background2.png')
    background_label2 = Label(menu, image=background_image2)
    background_label2.place(x=0, y=0, relwidth=1, relheight=1)

    #Below is buttons and labels, for design purposes and for the reason to switch screens
    pokeman= PhotoImage(file='pokey.png')
    head = Label(menu, image=pokeman)
    head.place(x=405, y=0,)

    playIMG = PhotoImage(file='play.png')
    playBut = Button(menu, image = playIMG, command = start)
    playBut.place(x=515, y=175)

    instructIMG = PhotoImage(file='instructions.png')
    instruct = Button(menu, image = instructIMG, command = helping)
    instruct.place(x=452, y=280)

    pokedex= PhotoImage(file='pokedextext.png')

    pokeList = Button(menu, image = pokedex, command= pokeLists)
    pokeList.place(x=478, y=370)

    copyWrite = Label(menu, text = "© 2020 All Rights Reserved")
    copyWrite.place(x=0,y=644)
    copyWrite.config(font=("Courier", 30))

    snakeGame = PhotoImage(file='snake.png')
    snake = Button(menu, image = snakeGame, command = snakeLadder)
    snake.place(x=335, y=450)
    


    

    menu.mainloop()

#First Screen ----------------------------------------------------
def logMenu():
    #global Variables
    global off
    global login
    login = Tk()
    login.title("Pokemon")
    login.geometry('1000x750')
    
    #Made it so the screen could not be made full size
    login.resizable(False, False)
    
    #Creating background image
    
    background_image=PhotoImage(file='background.png')
    background_label = Label(login, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # True statement for the def play to avoid destroy error
    
    off = True

    #Creating labels and buttons as well as image variables

    title = PhotoImage(file='title.png')

    lbl = Label(login, image = title)
    lbl.place(x=25, y=20)

    messagebox.showinfo('WELCOME TO MY POKEMON GAME', 'HOPE YOU HAVE A GREAT TIME :')

    begin= PhotoImage(file='begin.png')
    btn = Button(login, image=begin, command = play)
    btn.place(x=75, y=300)


    login.mainloop()
#---------------------------------------------

#Main Program--------------------------------

logMenu()
