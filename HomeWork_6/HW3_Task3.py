# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным
# значением дробной части элементов.

list1 = [1.1, 1.2, 3.1, 5, 10.01]

mx = max([round(x % 1, 3) for x in list1])
mn = min([round(x % 1, 3) for x in list1 if x % 1 > 0])
print(f'min {mn}, max {mx}, max - min {round(mx - mn, 3)}')