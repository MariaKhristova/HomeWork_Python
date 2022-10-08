# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

number = input('Введите число: ')
number_sum = 0

for digit in number:
    if digit.isdigit():
        number_sum += int(digit)


print("Сумма:", number_sum)

