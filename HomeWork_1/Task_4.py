# 4.Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой
# четверти (x и y).


quarter_number = int(input('Введите номер четверти: '))
if quarter_number == 1:
    print('Диапазон первой четверти равен: х > 0 и у > 0')
elif quarter_number == 2:
    print('Диапазон второй четверти равен: х < 0 и у > 0')
elif quarter_number == 3:
    print('Диапазон третьей четверти равен: х < 0 и у < 0')
elif quarter_number == 4:
    print('Диапазон четвёртой четверти равен: х > 0 и у < 0')
else:
    print('Номер четверти должен быть от 1 до 4: ')