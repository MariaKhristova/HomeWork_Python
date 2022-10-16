#f(x) = -12x^4*sin(cos(x)) - 18x^3+5x^2 + 10x - 30
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

x = np.linspace(-100, 100, 100)
y = -12 * x ** 4 * np.sin(np.cos(x)) - 18 * x ** 3 + 5 * x ** 2 + 10 * x - 30

print(x)
print(y)

#Определить корни
x1 = sp.Symbol('x')
roots = sp.solveset(-12 * x1 ** 4 * sp.sin(sp.cos(x1)) - 18 * x1 ** 3 + 5 * x1 ** 2 + 10 * x1 - 30, x1, domain=sp.S.Reals)
sp.pprint(roots)

dif = np.diff(y)
#Найти интервалы, на которых функция возрастает
d1 = [x[i + 1] for i, di in enumerate(dif) if di > 0]
print(d1)

#Найти интервалы, на которых функция убывает
d2 = [x[i + 1] for i, di in enumerate(dif) if di < 0]
print(d2)

#Построить график
plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()

#Вычислить вершину
print(np.max(y))
print(np.min(y))
#Определить промежутки, на котором f > 0
f1 = [x[i] for i, yi in enumerate(y) if yi > 0]
print(f1)
#Определить промежутки, на котором f < 0
f2 = [x[i] for i, yi in enumerate(y) if yi < 0]
print(f2)


