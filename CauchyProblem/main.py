from utils import * 
from math import exp

def original_function(x: float):
    return 1 / (1 + exp(x))

def function(y: float):
    return -y + y ** 2

original_point = 0

function_string = "y'(x) = -y(x) + y^2(x)"
taylor_function_string = "1/2 - 1/4 * x + 1/48 * x^3 - 1/480 * x^5 + 17/80640 * x^7 - 31/1451520 * x^9"
original_function_string = "1/(1+e^x)"
# taylor_function_string = "1/2 - 1/4 * x + 1/48 * x^3"

print('\nЧисленное решение Задачи Коши для обыкновенного дифференциального уравнения первого порядка\n')
print(f'Дифференциальное уравнение - {function_string}')
print('Задача Коши: y(0) = 0,5')
print(f'Точное решение задачи Коши - {original_function_string}')
print(f'Разложение в ряд Тейлора - {taylor_function_string}')

last_values = []

while True:

    while True:
        count_of_points = int_check('Введите количество точек (> 2) => ')
        if count_of_points <= 2:
            print('Неверное количество точек. Повторите ввод (> 2)')
            continue
        break
    step = float_check('Введите шаг h (расстояние между точками) => ')
    parameters = (original_function, function, step, count_of_points, original_point)
   
    last_values.append(print_table(taylor_function, *parameters))

    last_values.append(print_table(euler_method, *parameters))

    last_values.append(print_table(euler_first_method, *parameters))

    last_values.append(print_table(euler_second_method, *parameters))

    last_values.append(print_table(runge_kutta_method, *parameters))

    # print_adams_table(function, step, count_of_points, [taylor_function(original_point + step * i) for i in range(-2, 3)])

    last_values.append(print_table(extrapolation_adams_method, *parameters))

    print_comparison_table(last_values, original_function, original_point + count_of_points * step)
    last_values = []
    decision = input('\nХотите ввести новые параметры задачи? (Y/N) => ')
    if decision.lower() == 'y':
        continue
    break
