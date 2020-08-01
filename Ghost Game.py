#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8
# Ghost Game
from random import randint
print('Игра "Убеги от призрака"')
feeling_brave = True
score = 0
print('Перед тобой три двери...')
print('Призрак за одной из них.')
print('Какую дверь ты откроешь?')
while feeling_brave:
    ghost_door = randint(1, 3)
    door = input('1, 2, or 3?')
    door_num = int(door)
    if door_num == ghost_door:
        print('ПРИЗРАК!')
        feeling_brave = False
    else:
        if door_num > 3 or door_num < 1:
            print('Такой двери нет!')
        else:
            print('Нет призрака!')
            print('Вы перешли в следующую комнату. Какую дверь ты откроешь теперь?')
            score = score + 1
print('Бегите !!!!!!')
print('Конец игры! Ваш счёт', score)
