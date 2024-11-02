
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

print(f'Вычисляем значение интеграла для функции f(x) = {function_string}\n')

decision = "N"

while (True):
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

    print(f'Точное значение интеграла, вычисленное с помощью первообразной = {accurate_integral}\n')

    if (decision.lower() == 'n'):
        print('Проверим формулы и их алгебраические степени точности на многочленах степени 0 - 3: \n')

        check_ADA(down_border, up_border, 
                [const, first_polynomial, second_polynomial, third_polynomial],
                [antiderivative_const, antiderivative_first, antiderivative_second, antiderivative_third]
        )

    print_table(accurate_integral, function, down_border, up_border)

    decision = input("\nХотите ввести новые границы интегрирования? (Y/N) => ")
    if (decision.lower() != 'y'):
        break
