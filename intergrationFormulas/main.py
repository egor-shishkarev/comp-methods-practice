
# Посчитать и вывести на печать абсолютную фактическую погрешность для 
# каждой КФ. 
# Проанализировать полученные результаты (устно). 
# Замечание 1: 
# Обязательно описать в программе кроме произвольной функции также функции
# многочлены от нулевой до третьей степени включительно. 
# Замечание 2: 
# При отладке программы обязательно протестировать все квадратурные формулы на 
# многочленах степеней, соответствующих их (формул) алгебраической степени точ
# ности. 

from utils import *
from math import *

print('\n"Приближённое вычисление интеграла по квадратурным формулам"\n')

function_string = "x^2*e^2x"
const_string = "1"
first_polynomial_string = "2x+3"
second_polynomial_string = "4x^2-3x+1"
third_polynomial_string = "9x^3+4x^2-7x-2"

def function(x: float):
    return (x ** 2) * exp(2 * x)

def antiderivative(x: float):
    return 1 / 2 * (x ** 2 * exp(2 * x) - x * exp(2 * x) + 1 / 2 * exp(2 * x))

def const(x: float):
    return [1, x]

def first_polynomial(x: float):
    return [2 * x + 3, x ** 2 + 3 * x]
 
def second_polynomial(x: float):
    return [4 * x ** 2 - 3 * x + 1, 4 / 3 * x ** 3 - 3 / 2 * x ** 2 + x]

def third_polynomial(x: float):
    return [9 * x ** 3 + 4 * x ** 2 - 7 * x - 2, 9 / 4 * x ** 4 + 4 / 3 * x ** 3 - 7 / 2 * x ** 2 - 2 * x]

print(f'Вычисляем значение интеграла для функции f(x) = {function_string}')

down_border = float_check('Введите нижнюю границу интегрирования => ')
up_border = float_check('Введите верхнюю границу интегрирования => ')
while (True):
    if (up_border < down_border):
        print('Верхняя граница не может быть меньше нижней! Повторите ввод.')
        down_border = float_check('Введите нижнюю границу интегрирования => ')
        up_border = float_check('Введите верхнюю границу интегрирования => ')
        continue
    break

accurate_integral = antiderivative(up_border) - antiderivative(down_border)

print(f'Точное значение интеграла, вычисленное с помощью первообразной = {accurate_integral}')

print('Проверим формулы и их степени точности на многочленах степени 0 - 3: ')

# check_ADA()

print_table(accurate_integral, function, down_border, up_border)
