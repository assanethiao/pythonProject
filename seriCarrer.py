from turtle import *

def triangle():
    color("red")
    forward(100)
    left(120)
    forward(100)
    left(120)
    forward(100)
    left(120)

def carrer():
    color("blue")
    forward(50)
    right(90)
    forward(50)
    right(90)
    forward(50)
    right(90)
    forward(50)
    right(90)

for i in range(10):
    up()
    goto(-300 + 70*i, 10)
    down()
    carrer()
    triangle()

a = input()
