# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
import random

total_candies = 10
max_per_turn = 3

table = ['🍬' for x in range(total_candies)]
player_turn = random.randint(1, 2)

print(table)
print(f'Первым ходит игрок {player_turn}')

while len(table) > 0:
    n = 0
    while n <= 0 or n > max_per_turn:
        n = int(input(f'Игрок {player_turn} введите количество конфет: '))
        if n <= 0 or n > max_per_turn:
            print('Введено неправильное количество конфет')
    if n >= len(table):
        n = len(table)
    table = ['🍬' for x in range(len(table) - n)]
    print(table)
    if len(table) == 0:
        print(f'Победил игрок {player_turn}')
    player_turn = 1 if player_turn == 2 else 2

