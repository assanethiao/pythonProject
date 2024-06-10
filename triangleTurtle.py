from turtle import *

def triangle(couleur):

    color(couleur)
    forward(100)
    left(120)
    forward(100)
    left(120)
    forward(100)
    left(120)

mescouleurs = ["green", "yellow", "red"]
while True:
    for i in range(5):
        up()
        goto(-200, 200)
        down()
        triangle("green")
        up()
        goto(100, 100)
        down()
        triangle("yellow")
        up()
        goto(-200, 0)
        down()
        triangle("red")
