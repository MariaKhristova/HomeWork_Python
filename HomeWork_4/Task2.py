# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input('Введите число: '))

result = []
d = 2
while d * d <= n:
    if n % d == 0:
        result.append(d)
        n //= d
    else:
        d += 1
if n > 1:
    result.append(n)

print(result)
