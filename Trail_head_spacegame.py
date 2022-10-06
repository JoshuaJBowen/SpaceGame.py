#Trail_head_spacegame.py
#Josh Bowen
#1/15/2022

import turtle
import version1
import version2

def trailmain():
    wn = turtle.Screen()
    options = turtle.Turtle()
    options.ht()
    options.write("Press 1 for version 1 or Press 2 for version 2", False, "center", ("Times New Roman", 20, "normal"))

    def one():
        version1.version1main()
    def two():
        version2.version2main()

    
    wn.onkey(one, "1")
    wn.onkey(two, "2")

    wn.listen()

trailmain()
