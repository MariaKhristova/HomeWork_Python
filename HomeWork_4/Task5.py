# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

f1 = open("task5in1.txt", "r")
m1 = f1.read()
f1.close()

f2 = open("task5in2.txt", "r")
m2 = f2.read()
f2.close()

result = m1.replace('= 0', "+ ") + m2

f = open("task5.txt", "w")
f.write(result)
f.close()

print(m1)
