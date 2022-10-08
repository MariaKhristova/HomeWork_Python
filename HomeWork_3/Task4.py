# Напишите программу, которая будет преобразовывать десятичное число в двоичное

number = int(input('Введите число: '))
b_number = ''

while number > 0:
    b_number = str(number % 2) + b_number
    number = number // 2

print(b_number)
