# 2.Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


x = bool(input('Введите переменную x: '))
y = bool(input('Введите переменную y: '))
z = bool(input('Введите переменную z: '))
a = not (x or y or z)
b = not x and not y and not z

print(a == b)

