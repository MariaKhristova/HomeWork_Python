# 5. Реализуйте алгоритм перемешивания списка

from random import randint

list_1 = [1, 2, 3, 4, 5, 6, 7, 8]

for i in range(0, len(list_1)):
    i1 = randint(0, len(list_1) - 1)
    i2 = randint(0, len(list_1) - 1)
    a = list_1[i1]
    b = list_1[i2]
    list_1[i2] = a
    list_1[i1] = b
print(list_1)
