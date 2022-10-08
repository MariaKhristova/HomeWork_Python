# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов
# фибоначчи F0 = 0, F1 = 1, Fn = Fn-1 + Fn-2, где n >= 2, n ∈ Z
# негафибоначчи F-n = Fn+1 - Fn+2 или F−n = (−1)n+1Fn

def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


list1 = []
for e in range(1, 10):
    list1.append(fib(e))

print(list1)  # 1 1 2 3 5 8 13 21 34
