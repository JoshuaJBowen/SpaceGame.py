# OOP_spacegame.py
# Josh Bowen
# 3/26/2022

#set up the currency part
#also figure out multiple bad guys
#maybe make player and bad guy different colors
#add in the game infor title and losing lives when hit by a lazer


import turtle
import random

class Spaceship():
    """class for representing a spaceship and its various actions"""

    def __init__(self, x, y, lives, turt_player, turt_shoot, dist):
        """constructor for the graphic and theoretical representation of a Spaceship"""
        
        self.lives = lives
        
        self.x = x
        self.y = y

        self.appear = turt_player
        self.appear.ht()
        self.appear.up()
        self.appear.color("white")
        self.appear.shape("ship")
        self.appear.goto(self.x, self.y)
        self.appear.st()

        self.heading = 90
        self.appear.seth(self.heading)

        self.distance = dist

        self.weapon = turt_shoot
        self.weapon.ht()
        self.weapon.up()
        self.weapon.color("aqua")
        self.weapon.shape("bullet")

        self.currency = 0

    def get_lives(self):
        """reader method for number of lives"""
        return self.lives

    def get_x(self):
        """reader method for Spaceship x-position"""
        return self.x
    
    def get_y(self):
        """reader method for Spaceship y-position"""
        return self.y

    def get_heading(self):
        """reader method for Spaceship heading (angle from x-axis)"""
        return self.heading

    def get_distance(self):
        """reader method for the distance a spaceship can travel"""
        return self.distance
    
    def get_currency(self):
        """reader method for the currency on a spaceship"""
        return self.currency

    def set_lives(self, lives):
        """writer method for number of lives"""
        self.lives = lives
        #might update display here

    def set_heading(self, heading):
        self.heading = heading
        self.appear.seth(self.heading)

    def forward(self):#you could use cos and sin once you scale up 
        """writer method that updates Spaceship positon based on its heading and distance"""
        if self.get_heading() == 0:
            self.x = self.x + self.distance
        elif self.get_heading() == 90:
            self.y = self.y + self.distance
        elif self.get_heading() == 180:
            self.x = self.x - self.distance
        elif self.get_heading() == 270:
            self.y = self.y - self.distance
        else:
            print("An Error has occured with the forward method")
            
        self.appear.goto(self.x, self.y)
        #update world coordinates
        
    def right(self):
        """writer method that rotates heading right 90 degrees"""
        self.heading = (self.heading + 270)%360
        self.appear.seth(self.heading)

    def left(self):
        """writer method that rotates heading left 90 degrees"""
        self.heading = (self.heading + 90)%360
        self.appear.seth(self.heading)

    def shoot(self):
        "writer method that shoots in the direction Spaceship is facing"""
        #I may need to update this
        self.weapon.goto(self.x, self.y)
        self.weapon.seth(self.heading)
        self.weapon.st()#update this so that it wont show if it hits the bad guy
        self.weapon.fd(self.distance*2)#might change the shooting multiplier -- make sure to change it in the enemys decision to shoot or not
        self.weapon.ht()

    def set_currency(self, currency):
        """writer method for the Spaceship currency"""

#--------------------------

def main():

    #user inputs like dist and lives and number of bad guys
    wn = turtle.Screen()
    wn.bgcolor("black")
    #wn.title("Space Game! \t \t Enemy Lives: \t \t" + str(3) + "\t \t Your Lives: \t \t" + str(3) + "\t \t Currency: \t \t $" + str(0))
    wn.setworldcoordinates(-50,-50,50,50)

    #register shapes for game characters
    wn.register_shape("ship", ((0,-7), (-5,0), (0,25), (5,0)))
    wn.register_shape("bullet", ((0,-6), (-4,0), (0,9), (4,0)))
    wn.register_shape("money", ((-4,-8), (-4,8), (4,8), (4,-8)))


    #Set up the user's character
    player = turtle.Turtle()
    bullet = turtle.Turtle()
    starship = Spaceship(0, 0, 3, player, bullet, 10) # user inputs


    #set up one bad guy
    bad_guy = turtle.Turtle()
    lazer = turtle.Turtle()
    alienship = Spaceship(-50, -50, 2, bad_guy, lazer, 10)#Spaceship(random.randint(-10,11)*5, random.randint(-10,11)*5, 2, bad_guy, lazer, 10) # user inputs# might need to change coefficients


    #I want to have it based on of user inputs - use input function not key board events
    #the enemy only moves after the player moves and the enemy automatically shoots if in range
    #only need to evaluate lives (and money) after shoot
    
    while starship.get_lives() > 0:
        cmd = input("what would you like your spaceship to do?\nF for forward, R for Right, L for left, S for Shoot: ")
        while cmd.upper() != "F" and cmd.upper() != "R" and cmd.upper() != "L" and cmd.upper() != "S":
            cmd = input("what would you like your spaceship to do?\nF for forward, R for Right, L for left, S for Shoot: ")
        if cmd.lower() == "f":
            starship.forward()
            
            if abs(starship.get_x() - alienship.get_x()) > abs(starship.get_y() - alienship.get_y()):
                if starship.get_x() - alienship.get_x() < 0:
                    alienship.set_heading(180)
                else:
                    alienship.set_heading(0)
            else:
                if starship.get_y() - alienship.get_y() < 0:
                    alienship.set_heading(270)
                else:
                    alienship.set_heading(90)

            alienship.forward()

            if starship.get_x() == alienship.get_x() and starship.get_y() == alienship.get_y():
                alienship.set_heading(starship.get_heading())
                alienship.shoot()

            elif starship.get_x() == alienship.get_x() and abs(starship.get_y() - alienship.get_y()) <= 2*10: #change 10 to dist and 2 to shoot multiplier
                if starship.get_y() - alienship.get_y() >= 0:
                    alienship.set_heading(90)
                else:
                    alienship.set_heading(270)
                alienship.shoot()
                 
            elif starship.get_y() == alienship.get_y() and abs(starship.get_x() - alienship.get_x()) <= 2*10: #change 10 to dist and 2 to shoot multiplier
                if starship.get_x() - alienship.get_x() >= 0:
                    alienship.set_heading(0)
                else:
                    alienship.set_heading(180)
                alienship.shoot()

            #if abs(starship.get_x() - alienship.get_x()) < 10*2 or abs(starship.get_y() - alienship.get_y()) < 10*2: #note that the 10 is dist and the 2 is from the shoot multiplier update these for initial user input
             #   alienship.shoot() #lots of possibility for error come back and fix
        elif cmd.lower() == "r":
            starship.right()
        elif cmd.lower() == "l":
            starship.left()
        elif cmd.lower() == "s":
            starship.shoot()
        else:
            print("An Error has Occured with the IF statment")
# ---------------------

main()

            

