from tictactoe import Board

board = Board(dimensions=(3, 3))

while board.result() is None:
    print(board)

    while True:
        player_input = list(input(f'Игрок {board.turn} введите координаты : '))
        if len(player_input) != 2 or not player_input[0].isdigit() or not player_input[1].isdigit():
            print("Неправильно указаны координаты")
            continue

        x = int(player_input[0])
        y = int(player_input[1])
        if x > 3 or y > 3:
            print("Неправильно указаны координаты")
            continue
        if board.get_mark_at_position((x, y)) != 0:
            print("Клетка уже занята")
            continue
        break
    board.push((x, y))

if board.result() == 0:
    print("Ничья")
else:
    print(f'Победил игрок {board.result()}')


