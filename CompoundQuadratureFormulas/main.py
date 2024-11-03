  
# 6) 
# Знать/найти ответы на следующие вопросы: 
# • Сколько (в терминах m) значений функции f(x) участвует (в теории, а не при 
# Вашей реализации программы) в вычислении интеграла по каждой СКФ? 
# • Почему, несмотря на то, что АСТ КФ средних прямоугольников равна 1, а АСТ 
# Симпсона равна 3, они обе точны для f(x)= 1,27∙x5+2,04∙x при интегрировании по 
# [a, b]= [-5, 5] и для [a, b]= [-90, 90]? 
# • *Если ответ на предыдущий вопрос не находится, подумайте, почему для той же 
# функции не будет точности, например, для [a, b]= [-1, 5]? 

# 10) Уточнить  значения  J(h) и J(h/l) по принципу Рунге для каждой СКФ. 

# 11) Посчитать и вывести на печать абсолютные фактические и относительные 
# фактические погрешности для уточнённых значений. 

# 2) весовая функция  ρ(x) и функция  f(x) (описать в коде  вес ρ(x) положить ≡1 и не
# сколько вариантов для функции f(x), в частности, обязательно рассмотреть 
# функции-многочлены: нулевой, первой и третьей степени); 

# ФОРМЫ КОНТРОЛЯ: 
# 1) Все составные КФ должны быть точны (погрешность 0 или машинный 0) для 
# f(x)=const, однако, наиболее важно проверить точность СКФ левых и правых 
# прямоугольников при тестировании программы; 
# 2) Оставшиеся составные КФ должны быть также точны для f(x)– многочленов 
# первой степени, а КФ Симпсона точна для произвольного многочлена второй и 
# третьей степени. 
# «ПРОВЕРКА НА ПРОЧНОСТЬ»: 
# Протестировать программу для случая, когда искомое значение интеграла довольно 
# велико (подобрать такие f(x) и [A, B]). «Поиграть» числом разбиений m (от 10 000 
# до 1 000 000).  
# • Убедиться, что программа «не ломается». 
# • Убедиться, что СКФ Симпсона при умеренном числе разбиений (1000, 10000) 
# дает результат, более точный чем при миллионе. 
# • Подумать, с чем может быть связана потеря точности «у Симпсона».

from utils import *
from math import *

print('\n"Приближённое вычисление интеграла по составным квадратурным формулам"\n')

function_string = "x^2*sin(2x)"

def function(x: float):
    return x ** 2 * sin(2 * x)

def antiderivative(x: float):
    return x * sin(2 * x) / 2 - x ** 2 * cos(2 * x) / 2 + cos(2 * x) / 4

def const(x: float):
    return 1

def first_polynomial(x: float):
    return x
 
def second_polynomial(x: float):
    return x ** 2

def third_polynomial(x: float):
    return x ** 3

def antiderivative_const(x: float):
    return x

def antiderivative_first(x: float):
    return 1 / 2 * x ** 2

def antiderivative_second(x: float):
    return 1 / 3 * x ** 3

def antiderivative_third(x: float):
    return 1 / 4 * x ** 4

print(f'Вычисляем значение интеграла для функции f(x) = {function_string}')

down_border = float_check('Введите нижнюю границу интегрирования => ')
up_border = float_check('Введите верхнюю границу интегрирования => ')
count_of_intervals = positive_int_check('Введите число промежутков деления (> 0) => ')
while (True):
    if (up_border < down_border):
        print('Верхняя граница не может быть меньше нижней! Повторите ввод.')
        down_border = float_check('Введите нижнюю границу интегрирования => ')
        up_border = float_check('Введите верхнюю границу интегрирования => ')
        continue
    break

accurate_integral = antiderivative(up_border) - antiderivative(down_border)

print(f'\nВходные параметры:\n\tA = {down_border},\n\tB = {up_border},', 
      f'\n\tm = {count_of_intervals},\n\th = {(up_border - down_border) / count_of_intervals},\n\tФункция = {function_string}',
      f'\n\tJ = {accurate_integral}')

print_table(function, down_border, up_border, count_of_intervals, accurate_integral)

multiplier = positive_int_check('\nВведите параметр l - множитель для числа промежутков (> 0) => ')

count_of_intervals_new = count_of_intervals * multiplier

print_table(function, down_border, up_border, count_of_intervals_new, accurate_integral)

print_runge_correction(function, down_border, up_border, count_of_intervals, multiplier, accurate_integral)
