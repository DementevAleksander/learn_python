# from tkinter import colorchooser
# from tkinter import *
# t = Tk()
# colorchooser.askcolor()

from tkinter import *
from random import *
size = 2000
window = Tk()
canvas = Canvas(window, width=size, height=size)
canvas.pack()
while True:
    col = choice(['red', 'pink', 'orange', 'purple', 'yellow'])
    x0 = randint(0, size)
    y0 = randint(0, size)
    d = randint(0, size/50)
    canvas.create_oval(x0, y0, x0 + d, y0 + d, fill=col)
    window.update()