# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных
# позициях. Позиции хранятся в файле file.txt в одной строке одно число.

n = int(input('Введите число: '))
positions = [1, 3, 6]
result = 1
index = 0

for i in range(-n, n + 1):
    for j in positions:
        if index == j:
            result *= i
    index += 1
print(result)
