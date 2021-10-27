import numpy as np
from matplotlib import pyplot as plt

x = [1, 2, 3, 4, 5, 6]  # x-координаты из таблицы
y = [0, -9, -16, -15, 0, 35]  # y-координаты из таблицы


def product(val, n):
    """ Вспомогательный генератор для вычисления произведения разностей координат """
    mul = 1
    for i in range(n):
        if i: mul *= val - x[i - 1]
        yield mul


C = []  # список коэффициентов полинома

# вычисляем коэффициенты
for n in range(len(x)):
    p = product(x[n], n + 1)
    C.append((y[n] - sum(C[k] * next(p) for k in range(n))) / next(p))


def f(v):
    """ Значение полинома в точке v """
    return sum(C[k] * p for k, p in enumerate(product(v, len(C))))


x = np.array(x)
y = np.array(y)
x_new = np.linspace(np.min(x), np.max(x), 100)  # задаем случайные значения х от 1 до 6
y_new = [f(i) for i in x_new]  # по тем значениям х что нам уже даны находим у, строим полином Ньютона
plt.plot(x, y, 'o', x_new, y_new, 'r')  # строим график полинома
print(f(1))  # чему равен полином при х = 1
plt.grid()
plt.show()  # показываем графики
