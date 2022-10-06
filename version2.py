#version2.py
#Josh Bowen
#1/15/2022

import turtle
import random
import Trail_head_spacegame


def version2main():

    # set up screen
    wn = turtle.Screen()
    wn.clearscreen()
    wn.bgcolor("black")
    wn.bgpic("spacepic.png")
    wn.title("You can change the version at any time by pressing t")
    #wn.title("Space Game! \t \t Enemy Lives: \t \t" + str(3) + "\t \t Your Lives: \t \t" + str(3) + "\t \t Currency: \t \t $" + str(0))
    wn.setworldcoordinates(-50,-50,50,50)

    #register shapes for game characters
    wn.register_shape("ship", ((0,-7), (-5,0), (0,25), (5,0)))
    wn.register_shape("bullet", ((0,-6), (-4,0), (0,9), (4,0)))
    wn.register_shape("money", ((-4,-8), (-4,8), (4,8), (4,-8)))


    #Set up the user's character
    man = turtle.Turtle()
    man.ht()
    man.up()
    man.left(90)
    man.color("white")
    man.shape("ship")
    man.st()    


    #set up one bad guy
    bad = turtle.Turtle()
    bad.ht()
    bad.color("red")
    bad.shape("ship")
    bad.speed(5)
    bad.up()
    bad.goto(random.randint(-10,11)*5,random.randint(-10,11)*5)
    bad.st()


    #set up a bullet for the user
    bang1 = turtle.Turtle()
    bang1.ht()
    bang1.shape("bullet")
    bang1.color("aqua")
    bang1.up()


    #set up a bullet for the bad guy
    bang2 = turtle.Turtle()
    bang2.ht()
    bang2.shape("bullet")
    bang2.color("gold")
    bang2.up()


    #set up one treasure
    '''
    treasure = turtle.Turtle()
    treasure.ht()
    treasure.color("chartreuse")
    treasure.shape("money")
    treasure.up()
    treasure.goto(random.randint(-10,11)*5,random.randint(-10,11)*5)
    treasure.st()
    '''

    #checks the postition of a bullet and ship and returns true or false
    def hit(x1,y1,x2,y2):
        if int(x1) == int(x2) and int(y1) == int(y2):
            hit = True
        else:
            hit = False
        return hit

    #what happens upon player victory     
    def win():
        bang1.ht()
        bang2.ht()
        bad.ht()
        man.ht()
        #treasure.ht()
        man.goto(0,0)
        bang1.goto(0,-20)
        wn.setworldcoordinates(-50,-50,50,50)
        man.write("YOU WON!", False, "center", ("Times New Roman", 40, "normal"))
        bang1.write("Click the space bar to Replay", False, "center", ("Times New Roman", 20, "normal"))

    #what happens upon player destruction
    def lose():
        bang1.ht()
        bang2.ht()
        man.ht()
        #treasure.ht()
        bad.ht()
        bad.goto(0,0)
        bang2.goto(0,-20)
        wn.setworldcoordinates(-50,-50,50,50)
        bad.write("You Lose", False, "center", ("Times New Roman", 40, "normal"))
        bang2.write("Click the space bar to Restart", False, "center", ("Times New Roman", 20, "normal"))

    #how the enemy ship shoots
    def bshoot():
        if abs(man.xcor()-bad.xcor()) <= 10 and abs(man.ycor()-bad.ycor()) <= 10:
            bad.ht()
            bang2.goto(bad.xcor(),bad.ycor())
            bang2.seth(bad.heading())
            bad.st()
            bang2.st()
            for i in range(15):
                bang2.fd(1)
                if hit(bang2.xcor(),bang2.ycor(),man.xcor(),man.ycor()):
                    #good_lives = good_lives - 1
                    #screen(bad_lives, good_lives, money)
                    #if good_lives <= 0:
                    lose()
            bang2.ht()

    #get money if the money isnt hit yet
        '''
    def prize():
        if treasure.isvisible():
            treasure.ht()
            treasure.goto(random.randint(-50,50), random.randint(-50,50))
            treasure.st()

    #update the screen title to show game info NEEDS WORK!!
    def screen(b_lives, g_lives, money):
        title = "Space Game! \t \t Enemy Lives: \t \t" + str(b_lives) + "\t \t Your Lives: \t \t" + str(g_lives) + "\t \t Currency: \t \t $" + str(money) 
        wn.title(title)
        '''
    #a function for the enemy to move closer to the user
    def badf():
        bad.seth(bad.towards(man.pos()))
        for n in range(5):
            bad.fd(1)
        
    #make a funtion that will send the turtle forward and recenter him in the world
    def f():
        bad.seth(bad.towards(man.pos()))
        for n in range(5):
            man.fd(1)
            wn.setworldcoordinates(man.xcor()-50,man.ycor()-50,man.xcor()+50,man.ycor()+50)
        badf()
        bshoot()

    #make a funtion that will turn the turtle right
    def r():
        man.right(45)
        badf()
        bshoot()
        
    #make a funtion that will turn the turtle left
    def l():
        man.left(45)
        badf()
        bshoot()

    #make a function that lets the user shoot a bullet
    def shoot():
        man.ht()
        bang1.goto(man.xcor(),man.ycor())
        bang1.seth(man.heading())
        man.st()
        bang1.st()
        for i in range(15):
            bang1.fd(1)
            if hit(bang1.xcor(),bang1.ycor(),bad.xcor(),bad.ycor()):
                #bad_lives = bad_lives - 1
                #screen(bad_lives, good_lives, money)
                #if bad_lives <= 0:
                win()
            #if hit(bang1.xcor(),bang1.ycor(),treasure.xcor(),treasure.ycor()):
               # prize()
                #money = money + (random.randint(1,5))*10
               # screen(bad_lives, good_lives, money)
        bang1.ht()

    def backtotrailhead():
        wn.clearscreen()
        Trail_head_spacegame.trailmain()

    #set up commands for user's turtle
    wn.onkey(f, "Up")
    wn.onkey(r, "Right")
    wn.onkey(l, "Left")
    wn.onkey(shoot, "Down")
    wn.onkey(version2main, "space")
    wn.onkey(backtotrailhead, "t")
    wn.listen()

#bad_lives = 3
#good_lives = 3
#money = 0


