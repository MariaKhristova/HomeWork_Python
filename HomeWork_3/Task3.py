# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным
# значением дробной части элементов.

list1 = [1.1, 1.2, 3.1, 5, 10.01]
mx = 0
mn = 1

for i in range(1, len(list1)):
    if list1[i] % 1 > mx:
        mx = round(list1[i] % 1, 3)
    if 0 < list1[i] % 1 < mn:
        mn = round(list1[i] % 1, 3)
print(f'min {mn}, max {mx}, max - min {round(mx - mn, 3)}')
