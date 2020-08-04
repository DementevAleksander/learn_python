# Рисование фигур.
# from tkinter import *
# window = Tk()
# size = 500
# drawing = Canvas(window, width=size, height=size)
# drawing.pack()
# rect1 = drawing.create_rectangle(100, 100, 300, 200) #.create_ractangle() - рисует прямоугольник.
# square1 = drawing.create_rectangle(30, 30, 80, 80)
# oval1 = drawing.create_oval(0, 0, 500, 500) #.create_oval() - рисует окружность.
# circle1 = drawing.create_oval(30, 30, 80, 80)

from tkinter import *
from time import sleep
from time import *
window = Tk()
window.title('инопланетянин')
size = 500
drawing = Canvas(window, width=size, height=size)
drawing.pack()
body = drawing.create_oval(100, 150, 300, 250, fill='green')
eye = drawing.create_oval(170, 70, 230, 130, fill='white')
eyeball = drawing.create_oval(190, 90, 210, 110, fill='black')
mouth = drawing.create_oval(150, 220, 250, 240, fill='red')
neck = drawing.create_line(200, 150, 200, 130)
hat = drawing.create_polygon(180, 75, 220, 75, 200, 20, fill='red')

def mouth_open():
    drawing.itemconfig(mouth, fill='black')
def mouth_close():
    drawing.itemconfig(mouth, fill='red')

words = drawing.create_text(200, 280, text='Я инопланетянин!')

window.attributes('-topmost', 1) #Выводит окно tkinter на передний план.
def burb(event):
    mouth_open()
    drawing.itemconfig(words, text='БЭ-Э-Э!')
drawing.bind_all('<Button-1>',burb)

def sorry(event):
    mouth_close()
    drawing.itemconfig(words, text='Извините!')
drawing.bind_all('<Button-3>',sorry)

def eye_close(event):
    drawing.itemconfig(eye, fill='green')
    drawing.itemconfig(eyeball, state=HIDDEN)
def eye_open(event):
    drawing.itemconfig(eye, fill='white')
    drawing.itemconfig(eyeball, state=NORMAL)

drawing.bind_all('<KeyPress-a>', eye_open)
drawing.bind_all('<KeyPress-z>', eye_close)


# def eye_close_open(event):
#     drawing.itemconfig(eye, fill='green')
#     drawing.itemconfig(eyeball, state=HIDDEN)
#     time.sleep(2)
#     drawing.itemconfig(eye, fill='white')
#     drawing.itemconfig(eyeball, state=NORMAL)
# drawing.bind_all('<KeyPress-m>', eye_close_open)

def eye_control(event):
    key = event.keysym
    if key == "Up":
        drawing.move(eyeball, 0, -1)
    elif key == "Down":
        drawing.move(eyeball, 0, 1)
    elif key == "Left":
        drawing.move(eyeball, -1, 0)
    elif key == "Right":
        drawing.move(eyeball, 1, 0)
drawing.bind_all('<Key>', eye_control)