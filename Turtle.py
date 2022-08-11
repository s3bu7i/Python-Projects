
import turtle
import time

a=turtle.Turtle(shape="turtle")
a.speed(1)

arkaplan = turtle.getscreen()
arkaplan.bgcolor("black")
a.color("red")

def circle(long):
    for i in range(4):
        a.forward(long)
        a.left(90)
longnumber = int(input("Enter long number :"))

circle(longnumber)

time.sleep(3)
