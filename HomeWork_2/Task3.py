# 3. Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

# (1+1/n)^n

n = int(input('Введите число: '))
result = 0.0

for i in range(1, n+1):
    result += (1 + 1 / i) ** i
print(result)


