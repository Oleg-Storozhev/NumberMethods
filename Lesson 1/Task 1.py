import math
import numpy as np
import matplotlib.pyplot as plt


def function(vars):
    answer = []
    for i in vars:
        answer.append(math.exp(i/2)*math.sin(i))
    return answer


def lagranz(x, y, t):
    z = 0
    for j in range(len(y)):
        p1 = 1
        p2 = 1
        for i in range(len(x)):
            if i == j:
                p1 = p1 * 1
                p2 = p2 * 1
            else:
                p1 = p1 * (t - x[i])
                p2 = p2 * (x[j] - x[i])
        z = z + y[j] * p1 / p2
    return z


x = np.array([0, 1, 2, 3], dtype=float)  # переменные из таблицы
y = np.array(function(x), dtype=float)  # находим переменные y из функции
print("x", x)
print("y", y)

x_new = np.linspace(np.min(x), np.max(x), 100)  # задаем 100 случайных точек из от 8 до 14 на прямой x
y_new = [lagranz(x, y, i) for i in x_new]  # ищем у по новым точкам х используя Полином Лагранжа
plt.plot(x_new, function(x_new), 'b')  # по тем же точкам ресуем функцию f(x) = ln(x) ^ 13/7
plt.plot(x, y, 'o', x_new, y_new)  # рисуем полином Лагранжа и начальные точки х
plt.grid(True)
plt.show()
