# Создайте программу для игры в ""Крестики-нолики"".
lines_h = ['a', 'b', 'c']
lines_v = [1, 2, 3]

empty = '⛶'
field = [[empty, empty, empty], [empty, empty, empty], [empty, empty, empty]]

coordinates_h = '  |  a |  b |  c |'
line = '___________________'

game_over = False
count_of_turns = 0
winner = ''
player1 = '❌'
player2 = '⭕'
current_player = player2
while not game_over:
    current_player = player1 if current_player == player2 else player2
    winner_str = current_player + current_player + current_player

    print(coordinates_h)
    print(line)
    for i in range(0, 3):
        print(f'{i + 1} | ' + " | ".join(field[i]) + ' |')
        print(line)

    while True:
        player_input = list(input(f'Игрок {current_player} введите координаты : '))
        if len(player_input) != 2 or not player_input[0].isalpha() or not player_input[1].isdigit():
            print("Неправильно указаны координаты")
            continue

        x = player_input[0]
        y = int(player_input[1])
        if x not in lines_h or y not in lines_v:
            print("Неправильно указаны координаты")
            continue
        if field[lines_v.index(y)][lines_h.index(x)] != empty:
            print("Клетка уже занята")
            continue
        break

    count_of_turns += 1

    field[lines_v.index(y)][lines_h.index(x)] = current_player

    for i in range(0, 3):
        if field[0][i] + field[1][i] + field[2][i] == winner_str:
            winner = current_player
        if field[i][0] + field[i][1] + field[i][2] == winner_str:
            winner = current_player

    if field[0][0] + field[1][1] + field[2][2] == winner_str:
        winner = current_player
    if field[0][2] + field[1][1] + field[2][0] == winner_str:
        winner = current_player

    game_over = count_of_turns == 9 or winner == current_player

print(coordinates_h)
print(line)
for i in range(0, 3):
    print(f'{i + 1} | ' + " | ".join(field[i]) + ' |')
    print(line)

if winner == '':
    print("Ничья")
else:
    print(f'Победил игрок {winner}')


