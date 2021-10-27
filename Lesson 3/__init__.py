import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.family'] = 'fantasy'


def mnkGP(x,y): # функция которую можно использзовать в програме
              n = len(x) # количество элементов в списках
              s = sum(y) # сумма значений y
              s1 = sum([x[i] for i in  range(0,n)])  # сумма x
              s2 = sum([(x[i])**2 for i in  range(0,n)])  # сумма (x)**2
              s3 = sum([y[i] for i in  range(0,n)])  # сумма y
              s4 = sum([y[i]*x[i]  for i in range(0,n)])  # сумма xy
              a = round((n * s4 - s1 * s3)/(n*s2-s1**2), 3)  # коэфициент а с тремя дробными цифрами
              b = round((s3 - a * s1)/n, 3)  # коэфициент b с тремя дробными цифрами
              s4 = [a*x[i]+b for i in range(0,n)]  # список значений функции
              plt.xlabel('Координата X', size=14)  # оставляю комментарии для графика
              plt.ylabel('Координата Y', size=14)
              plt.plot(x, y, color='r', linestyle=' ', marker='o', label='Data(x,y)')
              plt.plot(x, s4, color='g', linewidth=2, label='Data(x,f(x)=ax+b')
              plt.legend(loc='best')
              plt.grid(True)  # добавляю сетку для графика
              plt.show()  # показываю график


x = [1, 2, 3, 4, 5, 6]
y = [3.9, 10.7, 18.2, 25, 31.9, 38.7]  # данные для проверки по функции y=x
mnkGP(x, y)
