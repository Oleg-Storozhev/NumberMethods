import numpy as np
from matplotlib import pyplot as plt
from scipy.interpolate import interp1d

x = [1, 2, 3, 4, 5, 6]  # x-координаты из таблицы
y = [0, -9, -16, -15, 0, 35]  # y-координаты из таблицы

f = interp1d(x, y, kind='quadratic')  # считаем параболический сплайм
x = np.array(x)  # переводим список в nparray для дальнейших расчетов
y = np.array(y)
xnew = np.linspace(np.min(x), np.max(x), 100)  # создаем 100 новых случайных точек от 1 до 6
plt.plot(x, y, 'o', xnew, f(xnew), 'r')  # по имеющимся точкам х находим у и рисуем график
plt.legend(['data', 'quadratic'], loc='best')  # оставляем комментарии к графику
plt.grid(True)  # включаем сетку на графике
plt.show()  # показываем график
