
# Activity 8: fourcircle.py
# Activity 8 : foursquare.py
# -----------------------------------------------------------------
# 
# Write a program using Turtle module to generate four circles.
# These circles just touches eachother and the center of the canvas is
# the center of all the circles.
# ---------------------------------------------------------------------


from turtle import *
shape("turtle")

penup()
setposition(-60,-120)

pd()
circle(60)
pu()
fd(120)

pd()
circle(60)
pu()
fd(120)

setposition(-60, 0)

pd()
circle(60)
pu()
fd(120)

pd()
circle(60)
pu()
fd(120)
