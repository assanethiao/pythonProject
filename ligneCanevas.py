from tkinter import *
from random import randrange

def changecolor():
    global couleur
    mescouleurs = ["purple", "red", "green", "blue", "pink", "yellow", "cyan", "orange", "maroon"]
    nomnbreAleatoire = randrange(9)
    couleur = mescouleurs[nomnbreAleatoire]

def tracerLigne():
    global x1, y1, x2, y2, couleur
    if couleur == "red":
        x1 = 0
        y1 = 10
        x2 = 500
        y2 = 10
    elif couleur == "green":
        x1 = 0
        y1 = 20
        x2 = 500
        y2 = 20
    elif couleur == "green":
        x1 = 0
        y1 = 20
        x2 = 500
        y2 = 20
    elif couleur == "maroon":
        x1 = 0
        y1 = 20
        x2 = 500
        y2 = 20
    elif couleur == "blue":
        x1 = 0
        y1 = 30
        x2 = 500
        y2 = 30
    elif couleur == "yellow":
        x1 = 0
        y1 = 40
        x2 = 500
        y2 = 40
    caneva.create_line(x1, y1, x2, y2, width=2, fill=couleur)


def tracerLigne2():
    global x1, y1, x2, y2, couleur, x3, y3, x4, y4

    caneva.create_arc(x1, y1, x2, y2, width=2, fill=couleur)
    caneva.create_arc(x3, y3, x4, y4, width=2, fill=couleur)

# principal
x1, y1, x2, y2, = 0, 0, 1000, 500
x3, y3, x4, y4 = 800, 500, 1000, 900
couleur = "dark green"

# fenetre
window = Tk()
caneva = Canvas(window, bg="dark grey", height=500, width=1000)
caneva.pack(side="left")
buton1 = Button(window, text="Quitter", command=window.quit, bg="red")
buton1.pack(side="bottom")
buton1 = Button(window, text="Tracer une ligne", command=tracerLigne, bg="blue")
buton1.pack()
buton1 = Button(window, text="Changer de couleur", command=changecolor, bg="blue")
buton1.pack()
buton1 = Button(window, text="Ligne croisées", command=tracerLigne2, bg="blue")
buton1.pack()
window.mainloop()
window.destroy()







