from tkinter import *

def cercle(abscis, ordonner, rayon, couleur="black"):
    caneva.create_oval(abscis-rayon, ordonner-rayon, abscis+rayon, ordonner+rayon, outline=couleur)


def figure1():
    caneva.delete(ALL)
    caneva.create_line(100, 0, 100, 200, fill="blue")
    caneva.create_line(0, 100, 200, 100, fill="blue")
    rayon = 15
    while rayon <100:
        cercle(100, 100, rayon)
        rayon += 15


def figure2():
    caneva.delete(ALL)
    visage = [[100, 100, 80, "red"],  # visage
          [70, 70, 15, "blue"],  # yeux
          [130, 70, 15, "blue"],
          [70, 70, 5, "black"],
          [130, 70, 5, "black"],
          [44, 115, 20, "red"],  # joues
          [156, 115, 20, "red"],
          [100, 95, 15, "purple"],  # nez
          [100, 145, 30, "purple"]]  # bouche
    i = 0
    while i < len(visage):
        element = visage[i]
        cercle(element[0], element[1], element[2], element[3])
        i += 1


window = Tk()
caneva = Canvas(window, width=200, height=200, bg="ivory")
caneva.pack(side="top", padx=5, pady=5)
buton1 = Button(window, text="Dessin 1", command=figure1)
buton1.pack(side="left", padx=3, pady=3)
buton2 = Button(window, text="Dessin 2", command=figure2)
buton2.pack(side="right", padx=3, pady=3)
window.mainloop()
