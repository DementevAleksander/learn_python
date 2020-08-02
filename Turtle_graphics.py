#Проект - черепашья графика.
from turtle import *
def turtle_controller(do, val):
    do = do.upper()
    if do == 'F':
        forward(val)
    elif do == 'B':
        backward(val)
    elif do == 'R':
        right(val)
    elif do == 'L':
        left(val)
    elif do == 'U':
        penup()
    elif do == 'D':
        pendown()
    elif do == 'N':
        reset()
    else:
        print('Я не знаю такой команды.')
# turtle_controller('f',100)
# turtle_controller('R',90)
# turtle_controller('F',50)


def string_artist(program): # Функция принимает от пользователся строку с командами (например, F100-R90).
    cmd_list = program.split('-') # Разделить строку на список с командами. Например, F100 R90
    for command in cmd_list: #Для каждой команды из списка
        cmd_len = len(command) #Что строка не пустая, напиример F100- -R90
        if cmd_len == 0: # Если значение пустое, то перейти к следующему элементу списка.
            continue
        cmd_type = command[0] # тип команды - это первая буква. Берёт первую букву, как параметр do. Например, для F100, программа возмёт значение F.
        num = 0
        if cmd_len > 1: # если есть ещё символы
            num_string = command[1:]
            num = int(num_string) # преобразовывываем в число. Берём значение, как параметр val.
        print(command, ':', cmd_type, num) # Печатает команду на экране, чтобы пользователь видел, что происходит.
        turtle_controller(cmd_type, num) # передаём команду контроллеру черепашке.

string_artist('N-L90-F100-R45-F70-R90-F70-R45-F100-R90-F100')

instruction = '''
Введите значения для рисования:
Например, домик: N-L90-F100-R45-F70-R90-F70-R45-F100-R90-F100
Команды:
'F': вперёд + числовое значение,
'B': назад + числовое значение,
'R': вправо + числовое значение,
'L': влево + числовое значение,
'U': поднять перо,
'D': опустить перо,
'N': Очистить всё.

'''
screen = getscreen() #Получает данные, необходимые для созания окна.
while True:
    t_program = screen.textinput('Рисовалка', instruction) #указываем, что нужно вывести в окошке.
    print(t_program) #вывод в окно.
    if t_program == None or t_program.upper() == 'Конец': #Останавливает программу, если введено слово Конец или нажата кнопка Cancel
        break
    string_artist(t_program)

# Домик N-F100-L90-F200-L90-F50-R60-F30-L120-F30-R60-F40-R60-F30-L120-F30-R60-F50-L90-F200-L90-F100-L90-U-F150-L90-F20-D-F30-L90-F30-L90-F30-L90-F30-R90-U-F40-D-F30-R90-F30-R90-F30-R90-F30-L180-U-F60-R90-D-F40-L120-F40-L120-F40

# Ёлочка N-L90-F200-L150-F70
