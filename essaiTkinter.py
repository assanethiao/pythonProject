from tkinter import *

fen1 = Tk()
text1 = Label(fen1, text="Assane Thiao", fg="blue")
text1.pack(side="left")
boul1 = Button(fen1, text="Bouton", fg="red", command=fen1.destroy)
boul1.pack()
fen1.mainloop()
