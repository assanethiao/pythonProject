from tkinter import *


def pointeur(event):
    chaine.configure(text="Clic détecté en X =" + str(event.x) + ", Y =" + str(event.y))
    cadre.create_oval(event.x, event.y, event.x + 5, event.y + 5, fill="red")


fen = Tk()
cadre = Canvas(fen, width=200, height=150, bg="light yellow")
cadre.bind("<Button-1>", pointeur)
cadre.pack()
chaine = Label(fen)
chaine.pack()
fen.mainloop()