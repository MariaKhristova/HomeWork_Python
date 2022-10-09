# Вычислить число c заданной точностью d
# Пример:	при d = 0.001, π = 3.141        10-1 <= d <= 10-10
import math

d = 0.001
pi = math.pi
p = 0
while d < 1:
    d *= 10
    p += 1

print(format(pi, '.' + str(p) + 'f'))
