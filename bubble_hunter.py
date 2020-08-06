#Игра "Охотник за пузырями"

# ------------------------- Фон и подлодка -------------------- #
from tkinter import *
window = Tk()
window.title('Подводная лодка')
HEIGHT = 600
WIDTH = 1200
c = Canvas(window, width=WIDTH, height=HEIGHT, bg='#0ba0bb')
c.pack()

ship_id = c.create_polygon(5, 5, 5, 25, 30, 15, fill='red')
ship_id2 = c.create_oval(0, 0, 30, 30, outline='red')
SHIP_R = 15
MID_X = WIDTH / 2
MID_Y = HEIGHT / 2
c.move(ship_id, MID_X, MID_Y)
c.move(ship_id2, MID_X, MID_Y)

# ------------------ Управление подлодкой -------------------- #
SHIP_SPD = 10
def move_ship(event):
    key = event.keysym
    if key == 'Up':
        c.move(ship_id, 0, -SHIP_SPD)
        c.move(ship_id2, 0, -SHIP_SPD)
    elif key == 'Down':
        c.move(ship_id, 0, SHIP_SPD)
        c.move(ship_id2, 0, SHIP_SPD)
    elif key == 'Left':
        c.move(ship_id, -SHIP_SPD, 0)
        c.move(ship_id2, -SHIP_SPD, 0)
    elif key == 'Right':
        c.move(ship_id, SHIP_SPD, 0)
        c.move(ship_id2, SHIP_SPD, 0)
c.bind_all('<Key>', move_ship)

# ------------------ Создание пузырей -------------------- #
from random import randint
bub_id = list() #Создаём пустой список для хранения имени пузыря.
bub_r = list() #Создаём пустой список для хранения размера пузыря.
bub_speed = list() #Создаём пустой список для хранения скорости пузыря.
MIN_BUB_R = 10
MAX_BUB_R = 30
MAX_BUB_SPD = 10
GAP = 100
def create_buble():
    x = WIDTH + GAP
    y = randint(0, HEIGHT)
    r = randint(MAX_BUB_R, MAX_BUB_R)
    id1 = c.create_oval(x - r, y - r, x + r, y + r, outline='#37ffde')
    bub_id.append(id1)
    bub_r.append(r)
    bub_speed.append(randint(1, MAX_BUB_SPD))

# ------------------ Движение пузырей -------------------- #
def move_bubbles():
    for i in range(len(bub_id)):
        c.move(bub_id[i], -bub_speed[i], 0)

from time import sleep, time
BUB_CHANCE = 10

def get_coords(id_num):
    pos = c.coords(id_num)
    x = (pos[0] + pos[2])/2
    y = (pos[1] + pos[3])/2
    return x, y

# ------------------ Лопанье пузырей -------------------- #
def del_bubble(i):
    del bub_r[i]
    del bub_speed[i]
    c.delete(bub_id[i])
    del bub_id[i]

def clean_up_bubs():
    for i in range(len(bub_id)-1, -1, -1):
        x, y = get_coords(bub_id[i])
        if x < -GAP:
            del_bubble(i)

# ------------------ Ловим пузыри -------------------- #
# Вычисляем расстояние между объектами
from math import sqrt
def distance(id1, id2):
    x1, y1 = get_coords(id1)
    x2, y2 = get_coords(id2)
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Лопаем пузыри
def collision():
    points = 0
    for bub in range(len(bub_id)-1, -1, -1):
        if distance(ship_id2, bub_id[bub]) < (SHIP_R + bub_r[bub]):
            points += (bub_r[bub] + bub_speed[bub])
            del_bubble(bub)
    return points

# ------------------ Счёт и время игры -------------------- #
c.create_text(50, 30, text='Время', fill='white')
c.create_text(150, 30, text='Очки', fill='white')
time_text = c.create_text(50, 50, fill='white')
score_text = c.create_text(150, 50, fill='white')
def show_score(score):
    c.itemconfig(score_text, text=str(score))
def show_time(time_left):
    c.itemconfig(time_text, text=str(time_left))

# ------------------ Ограничение по времени и количеству очков -------------------- #
BUB_CHANGE = 10
TIME_LIMIT = 30
BONUS_SCORE = 2000
bonus = 0
end = time() + TIME_LIMIT

# ------------------ Основной цикл игры -------------------- #
score = 0
while time() < end:
    if randint(1, BUB_CHANCE) == 1:
        create_buble()
    move_bubbles()
    clean_up_bubs()
    score += collision()
    if (int(score / BONUS_SCORE)) > bonus:
        bonus += 1
        end += TIME_LIMIT
    show_score(score)
    show_time(int(end - time()))
    window.update()
sleep(0.01)

# ------------------ Конец игры -------------------- #
c.create_text(MID_X, MID_Y, \
    text='Игра закончена!', fill='white', font=('Helvetica', 30))
c.create_text(MID_X, MID_Y + 30, \
    text='Очки:'+ str(score), fill='white')
c.create_text(MID_X, MID_Y + 45, \
    text='Бонусное время:'+ str(bonus*TIME_LIMIT), fill='white')