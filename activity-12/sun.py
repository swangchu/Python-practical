# Activity 12: sun.py
# -----------------------------------------------------------------
# Write a program using Turtle to generate a sun with four rays 
# around it.
# 
# ---------------------------------------------------------------------


from turtle import *
shape("turtle")

speed(5)
bgcolor("skyblue")
hideturtle()

pu()
goto(85,110)
dot(90,"red")

pencolor("yellow")
pu()
goto(85,110)
fd(45)
pd()
fd(85)
pu()
bk(85+45)
lt(90)

fd(45)
pd()
fd(85)
pu()
bk(85+45)
lt(90)

fd(45)
pd()
fd(85)
pu()
bk(85+45)
lt(90)

fd(45)
pd()
fd(85)
pu()
bk(85+45)
lt(90)
