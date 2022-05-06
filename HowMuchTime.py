import time
import math
ked = 0.0
keds = 0.0
today = time.time()
print(time.ctime(today))
ed = input('Какие единицы расстояния вы хотите использовать(nm, km):' )
if ed == 'km':
    ked = 1.0
elif ed == 'nm':
    ked = 1.60934
else:
    print('Вы допустили ошибку при вводе! Попробуйте ещё раз ')
a = float(input('Введите длину маршрута: '))
s = a * ked
eds = input('Какие единицы скорости вы хотите использовать(mch, km/h, knots): ')
if eds == 'mch':
    keds = 1225.04
elif eds == 'knots':
    keds = 1.852
elif eds == 'km/h':
    keds = 1.0
else:
    print('Вы допустили ошибку при вводе!')
b = float(input('Введите скорость судна: '))
v = keds * b
time = s / v
print('Примерное время полёта соствляет: ' + str(math.ceil(time)) + ' часов')
input()


