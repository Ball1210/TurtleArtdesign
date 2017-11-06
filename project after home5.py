import turtle

turtle.bgcolor("black")
bob = turtle.Turtle()
bob.fillcolor("blue")
bob.pencolor("blue")
bob.pensize(4)
bob.speed(0)

def drawsq(t, s):
    for i in range(4):
        t.forward(300)
        t.left(90)

for i in range(1,180):
    bob.left(360/i)
    drawsq(bob, 50)

from turtle import *
bob = turtle.Turtle()
bob.goto(0,0)
bob.speed(0)
shape("turtle")
wheel=12
bgcolor("black")
pensize(10)
pencolor("white")

for i in range(wheel):
    begin_fill()
    right(90)
    forward(200)
    left(120)
    forward(200)
    left(120)
    forward(200)
    end_fill()

tracer(0)
for times in range(375):
    bob.penup()
    bob.goto(-590,200)
    bob.pendown()
    bob.circle(100)
    bob.left(1)
    bob.color("white")

for times in range(375):
    bob.penup()
    bob.goto(-590,0)
    bob.pendown()
    bob.circle(65)
    bob.left(1)
    bob.color("blue")

for times in range(375):
    bob.penup()
    bob.goto(-590,-200)
    bob.pendown()
    bob.circle(100)
    bob.left(1)
    bob.color("white")
for times in range(375):
    bob.penup()
    bob.goto(590,200)
    bob.pendown()
    bob.circle(100)
    bob.left(1)
    bob.color("white")

for times in range(375):
    bob.penup()
    bob.goto(590,0)
    bob.pendown()
    bob.circle(65)
    bob.left(1)
    bob.color("blue")

for times in range(375):
    bob.penup()
    bob.goto(590,-200)
    bob.pendown()
    bob.circle(100)
    bob.left(1)
    bob.color("white")

turtle.color("blue")
pensize(5)
def makeSquare (turtle, size):
    for i in range(4):
        bob.penup()
        bob.goto(-590, -200)
        bob.pendown()
        turtle.forward(size)
        turtle.left(90)

makeSquare(turtle, 100)
def makeSpiralSquare(turtle, size):
    for i in range(36):
        makeSquare(turtle, size)
        turtle.left(20)

makeSpiralSquare(turtle, 100)


    




    
