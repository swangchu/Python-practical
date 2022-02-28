# Activity 6: concentric.py
# -----------------------------------------------------------------
# Write a program using Turtle module to generate two concentric circles.
# The inner circle filled with red color while outer circle is without color.
# 
# ---------------------------------------------------------------------


from turtle import *
shape("turtle")


right(90)
pu()
fd(20)
left(90)
pd()
begin_fill()
color("red")
circle(20)
end_fill()
pu()
setposition(0,0)

right(90)
pu()
fd(50)
left(90)
pd()
circle(50)
pu()
setposition(0,0)
