from tkinter import *
from random import randint
def roll():
    text.delete(0.0, END)
    text.insert(END, str(randint(1,6)))
window = Tk()
text = Text(window, width=5, height=5)
knopka = Button(window, text='Бросить кубик!',command=roll)
text.pack()
knopka.pack()