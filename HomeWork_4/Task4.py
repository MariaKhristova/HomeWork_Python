# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.
# Пример:	k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random

k = 7
n1 = random.randint(0, 100)
n2 = random.randint(0, 100)
n3 = random.randint(0, 100)

result = str(n1) + 'x^' + str(k) + ' + ' + str(n2) + 'x + ' + str(n3) + ' = 0'
f = open("task4.txt", "w")
f.write(result)
f.close()
