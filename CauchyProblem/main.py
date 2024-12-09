from utils import * 
from math import exp

def original_function(x: float):
    return 1 / (1 + exp(x))

def function(y: float):
    return -y + y ** 2

original_point = 0

function_string = "y'(x) = -y(x) + y^2(x)"
taylor_function_string = "1/2 - 1/4 * x + 1/48 * x^3 - 1/480 * x^5 + 17/80640 * x^7 - 31/1451520 * x^9"
# taylor_function_string = "1/2 - 1/4 * x + 1/48 * x^3"

print('\nЧисленное решение Задачи Коши для обыкновенного дифференциального уравнения первого порядка\n')
print(f'Дифференциальное уравнение - {function_string}')
print('Задача Коши: y(0) = 0,5')

while True:
    count_of_points = int_check('Введите количество точек (> 2) => ')
    if count_of_points <= 2:
        print('Неверное количество точек. Повторите ввод (> 2)')
        continue
    break
step = float_check('Введите шаг h (расстояние между точками) => ')
parameters = (original_function, function, step, count_of_points, original_point)

print_table(taylor_function, *parameters)

print_table(euler_method, *parameters)

print_table(euler_first_method, *parameters)

print_table(euler_second_method, *parameters)

print_table(runge_kutta_method, *parameters)

print_table(extrapolation_adams_method, *parameters)

# Для всех методов найти абсолютную погрешность для последней точки
# Предложить ввести новые точки
