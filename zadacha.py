# Создайте программу для игры с конфетами человек против человека.
# *' Условие игры: На столе лежит 117 конфет. 
# Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход.

import os
os.system('cls||clear')

count = int(input('Введите общее количество конфет для игры: '))
gamer1, gamer2 = input('Введите имя 1-го игрока: '), input('Введите имя 2-го игрока: ')
current = gamer1
while count > 0:
    print('Количество оставшихся конфет: {}'.format(count))
    while True:
        number = int(input('Ход игрока {} от 1 до 28 конфет: '.format(current)))
        if number >= 1 and number <= 28:
            break
    count -= number
    current = gamer2 if current == gamer1 else gamer1
print('Выиграл игрок {}'.format(current))