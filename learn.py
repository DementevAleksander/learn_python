# a = 10
# b = 5
# print(a + b)
# print(a - b)

# from turtle import *
# forward(100)
# right(90)
# forward(100)
# right(90)
# forward(100)
# right(90)
# forward(100)
# print('Я нарисовал квадрат!')

# # Переменные
# run = 5
# print(run)

# name = 'Yaroslav'
# print(name)

# run = 10
# print(run)

# name = run
# print(run, name)

# run = 7
# print(run, name)

# # Типы данных
# # apple = input('Enter number of apples')
# # print(apple + '1') #Текст+текст

# # apple1 = input('Enter number of apples')
# # print(int(apple1) + 1) #Число+число

# #Вычмсления
# ants = 5
# spiders = 70
# bug = ants + spiders
# print(bug)
# ants = 100
# spiders = 100
# print(bug)

# #Строки
# a = 'run'
# b = ' Пришельцы прилетели!'
# c = a + b + ' war'
# print(c)
# len(c)

# #Нумерация символов
# d = 'Harry Potter'
# d[4]
# d[6:12]
# d[:5]
# d[6:]

# print('Привет!\'Как\' дела?') #\ - экранирование.

# #Ввод и вывод
# name = input('Как тебя зовут?')
# print('Привет,', name, sep=('\n'))

# old = input('Сколько тебе лет?')
# print('Мне,',old,'лет', sep=('-')) 

# #Принятие решений
# toys = 10
# toys == 1

# #Ветвление
# a = int(input('введите знчение a'))
# b = int(input('введите знчение b'))
# deyst = input('+-*/')
# if deyst == '+':
#     c = a + b
# elif deyst == '-':
#     c = a - b
# elif deyst == '*':
#     c = a * b
# elif deyst == '/':
#     c = a / b
# else:
#     c = 'Ошибка!!!'
# print('Результат,', c)

# Циклы в Python
# from turtle import *
# # forward(100)
# # right(120)
# # forward(100)
# # right(120)
# # forward(100)
# # right(120)
# # print('Я нарисовал треугольник!')

# for i in range(3):
#     forward(100)
#     right(120)

# for i in range(3, 14, 5): # от, до, шаг
#     print(i, end=' ') # end=' ' - вывести в строку.

# for i in range(3): # повторить три раза, начиная с 0.
#     print(i, end=' ') # end=' ' - вывести в строку.

# for i in range(10, 0, -1):
#     print(i, end=' ') # end=' ' - вывести в строку.

# Вложенные циклы
# n = 3
# for a in range(1, n + 1): #Повторяет заданное количество раз.
#     for b in range(1, n + 1):
#         print(a, '*', b, '=', b * a)

# answer = 'да'
# while answer == 'да': #Повторяет, пока не будет выполнено условие.
#     answer = input('Пойдёшь плавать?')
#     print('Я? ', answer)
# print('Ну тогда я один пойду.')

# # Выход из цикла
# score = 0
# table = 7
# for i in range(1, 13): 
#     print('Сколько будет', i, '*', table)
#     guess = input()
#     if guess == 'стоп':
#         print('Поздравляю, вы бездарь!')
#         break #Выйти из цикла.
#     if guess == 'не знаю':
#         print('Жаль! Перехожу к следующему вопросу!')
#         continue #Пропустить шаг, не выходя из цикла.
#     ans = i * table
#     if int(guess) == ans:
#         print('Правильно!')
#         score = score + 1
#     else:
#         print('Это не правильный ответ.', ans)
# print('Урок окончен!')
# print('Вы набрали', score, 'очков!')
# if score>6:
#     print('Молодец!')
# else:
#     print('Потренируйся ещё!') 

#Списки
# family = ['Папа', 'Мама', 'Ярослав', 'Ростислав', 'Пломбир(кот)']
# # for i in family:
# #     print('Привет,', i)
# print(family[4])


# family_grandfather = ['Дедушка', 'Бабушка', 'Инна', 'Людмила', 'Мейджер', 'Пауль', 'Муза', 'Ника']

# na_dache = family + family_grandfather
# print(na_dache)
# for i in na_dache:
#     print('Привет,', i)

# food = [['Конфеты', 'Щоколадка', 'Пицца'], ['Борщ', 'Броколи', 'Сельдерей']]
# # print(food)
# print(food[0])
# # print(food[1])
# print(food[1][1])

# # Функции
# def hi():
#     print('Привет!')
#     a = 5
#     b = 5
#     c = a+b
#     print(c)

# #hi()

# def night(people1, people2):
#     print('Спокойной ночи,', people1)
#     print('Спокойной ночи,', people2)

# night('мама', 'папа')
# night('Ростислав','Ярослав')

# def dist(speed, time):
#     distance = speed * time
#     print(distance, 'км')
# # dist(80,5)

# def dist2(question):
#     answer = input(question)
#     num = int(answer)
#     return answer

# speed = dist2('Введите вашу скорость:')
# time = dist2('Введите время, за которое вы проехали расстояние:')
# print('Вы проехали', speed * time, 'км')


# speed = input('Введите вашу скорость:')
# time = input('Введите время, за которое вы проехали расстояние:')
# speed = int(speed)
# time = int(time)
# print('Вы проехали', speed * time, 'км')

# # Забавные фразы
# name = ['папа', 'мама', 'Ярик', 'Ростик', 'Пломбир']
# say = ['летом', 'гулять', 'мяукать', 'зимой', 'домой']
# do = ['идёт', 'летит', 'плывёт', 'бежит', 'прыгает']

# from random import randint
# def pick(words):
#     num_words = len(words) #len() - вычисляет, сколько слов в списке.
#     num_picked = randint(0, num_words - 1) #выбирает случайное число, соответствующее одному из элементов списка.
#     word_picked = words[num_picked] #Сохраняет случайное слово в перменной word_picked.
#     return word_picked
# print(pick(name), pick(do), pick(say), '!')


# # Кортежи и словари
# mama = ('Настя', 31, 1.60)
# print(mama[1])

# name, age, height = mama
# print(name, age, height)

# papa = ('Саша', 31, 1.72)

# parents = [mama, papa]
# print(parents)

# Переменые и функции
def func1():
    a = 10 #локальная переменная (в домике).
    print(a)
# func1()

b = 100000 #глобальная переменная.
def func2():
    print(b)
# func2()

def func3(name1, name2):
    print(name2)
# func3('папа', 'мама')

def func4(y):
    print(y)
    y = 'хлеб'
    print(y)
z = 'бутерброд'
func4(z)
print(z)
