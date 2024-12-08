from utils import * 
from math import exp

def function(x: float):
    return 1 / (1 + exp(x))

def derivative(x: float):
    return - function(x) + (function(x)) ** 2

def taylor_function(x: float):
    return 1 / 2 - 1 / 4 * x + 1 / 48 * x ** 3 - 1 / 480 * x ** 5 + 17 / 80640 * x ** 7 - 31 / 1451520 * x ** 9

original_point = 0

function_string = "y'(x) = -y(x) + y^2(x)"
taylor_function_string = "1/2 - 1/4 * x + 1/48 * x^3 - 1/480 * x^5 + 17/80640 * x^7 - 31/1451520 * x^9"

print('\nЧисленное решение Задачи Коши для обыкновенного дифференциального уравнения первого порядка\n')
print(f'Дифференциальное уравнение - {function_string}')
print('Задача Коши: y(0) = 0,5')

count_of_points = int_check('Введите количество точек (> 0) => ')
step = float_check('Введите шаг h (расстояние между точками) => ')

print(f'\nПриближенное решение методом разложения в ряд Тейлора  - {taylor_function_string}')
print_taylor_table(taylor_function, function, step, count_of_points, original_point)
