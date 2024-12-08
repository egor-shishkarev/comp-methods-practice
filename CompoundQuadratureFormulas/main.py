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
count_of_intervals = positive_int_check('Введите число промежутков деления (> 1) => ')
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

check_ADA(
    down_border,
    up_border,
    [const, first_polynomial, second_polynomial, third_polynomial],
    [antiderivative_const, antiderivative_first, antiderivative_second, antiderivative_third],
    count_of_intervals
)

print_table(function, down_border, up_border, count_of_intervals, accurate_integral)

while True:
    decision = int_check('\nВыберите действие:\n0 - выйти из программы,' +
      '\n1 - увеличить количество отрезков (вместе с уточнением по Рунге),\n2 - ввести новые параметры\n=> ')
    match (decision):
        case 0:
            break

        case 1:
            multiplier = positive_int_check('\nВведите параметр l - множитель для числа промежутков (> 1) => ')
            count_of_intervals_new = count_of_intervals * multiplier
            print_table(function, down_border, up_border, count_of_intervals_new, accurate_integral)
            print_runge_correction(function, down_border, up_border, count_of_intervals, multiplier, accurate_integral)
            count_of_intervals = count_of_intervals_new

        case 2:
            down_border = float_check('Введите нижнюю границу интегрирования => ')
            up_border = float_check('Введите верхнюю границу интегрирования => ')
            count_of_intervals = positive_int_check('Введите число промежутков деления (> 1) => ')
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

        case _:
            print('Введено недопустимое значение! Повторите ввод.')