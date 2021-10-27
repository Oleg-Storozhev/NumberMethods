import numpy as np
import matplotlib.pyplot as plt


def coefficient(x, y):
    m = len(x)
    x = np.copy(x)
    a = np.copy(y)
    for k in range(1, m):
        a[k:m] = (a[k:m] - a[k - 1])/(x[k:m] - x[k - 1])
    return a


def newton(x_data, y_data, x):
    a = coefficient(x_data, y_data)
    n = len(x_data) - 1
    p = a[n]

    for k in range(1, n + 1):
        p = a[n - k] + (x - x_data[n - k])*p

    return p


x = np.array([1, 2, 3, 4, 5, 6])  # взято из таблицы
y = np.array([0, -9, -16, -15, 0, 35])  # взято из таблицы

x_new = np.linspace(np.min(x), np.max(x), 100)  # задаем случайные значения х от 1 до 6
y_new = [newton(x, y, i) for i in x_new]  # по тем значениям х что нам уже даны находим у, строим полином Ньютона
plt.plot(x, y, 'o', x_new, y_new, 'r')  # строим график полинома

print(newton(x_new, y_new, 1))  # чему равен полином при х = 1
plt.grid(True)
plt.show()
