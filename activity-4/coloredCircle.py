# Activity 4: coloredCircle.py
# -----------------------------------------------------------------
# Write a program using Turtle module to generate a chain of 4 circles of radius 25
# pixels.The circles just touches eachother and their outline to be of black, yellow, 
# red, green and blue.
# 
# ---------------------------------------------------------------------

from turtle import *
shape("turtle")

circle(25)
pu()
forward(50)

color("yellow")
pd()
circle(25)
pu()
forward(50)

color("red")
pd()
circle(25)
pu()
forward(50)

color("green")
pd()
circle(25)
pu()
forward(50)

color("blue")
pd()
circle(25)
pu()
forward(50)
