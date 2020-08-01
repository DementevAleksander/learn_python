from tkinter import *
def mama():
    print('Привет мама!')
    print(5+5)
def papa():
    print('Привет папа!')
window = Tk()
mama = Button(window, text='Передать привет маме!', command=mama)
papa = Button(window, text='Передать привет папе!', command=papa)
mama.pack()
papa.pack()
