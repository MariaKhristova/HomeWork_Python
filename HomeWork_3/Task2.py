# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй
# и предпоследний и т.д

from random import randint

list1 = []
list2 = []
n = int(input('Укажите размер списка: '))

for i in range(n):
    list1.append(randint(-50, 50))
print(list1)
for i in range((len(list1) + 1) // 2):
    c = list1[i] * list1[0-1-i]
    list2.append(c)
print(list2)
