from typing import Callable, List
from methods import *

def float_check(input_string: str) -> float:
    while (True):
        try:
            x = float(input(input_string))
            break
        except (ValueError, TypeError):
            print("Вы ввели неправильное значение, повторите ввод!")
    return x


def int_check(input_string: str) -> int:
    while (True):
        try:
            x = int(input(input_string))
            break
        except (ValueError, TypeError):
            print("Вы ввели неправильное значение, повторите ввод!")
    return x

def positive_int_check(input_string: str) -> int:
    while (True):
        x = int_check(input(input_string))
        if x <= 0:
            print('Вы ввели неположительное значение, повторите ввод!')
            continue
        break
    return x

def print_table(calc_function: Callable[[float], float], original_function: Callable[[float], float], function: Callable[[float], float], step: float, count_of_points: int, original_point: float):
    function_names = {
        taylor_function: "по Тейлору",
        euler_method: "по Эйлеру",
        euler_first_method: "по Эйлеру I",
        euler_second_method: "по Эйлеру II",
        runge_kutta_method: "по Рунге-Кутта",
        extrapolation_adams_method: "по Адамсу"
    }
    name = function_names.get(calc_function)

    print(f'\nСравнение точного решения и решения "{name}"\n')
    header_format = "{:>6} {:>15} {:>20} {:>25} {:>15}"
    row_format = "{:>6} {:>15.6f} {:>20.6e} {:>25.6e} {:>15.6e}"
    
    print(header_format.format('Точка', 'Значение точки', 'Точное y(x)', f'Значение {name}', 'Погрешность'))
    print('-' * 85)
    if (calc_function == taylor_function):
        calc_function_values = [taylor_function(original_point + step * i) for i in range(-2, count_of_points + 1)]
        start, end = -2, count_of_points + 1
    elif (calc_function == extrapolation_adams_method):
        taylor_values = [taylor_function(original_point + i * step) for i in range(-2, 3)]
        calc_function_values = extrapolation_adams_method(taylor_values, function, step, count_of_points)[0]
        start, end = -2, count_of_points + 1
    else:
        calc_function_values = calc_function(original_function(original_point), function,  step, count_of_points)
        start, end = 1, count_of_points + 1
    for i in range(start, end):
        point = original_point + i * step
        function_value = original_function(point)
        calc_function_value = calc_function_values[i - start]
        print(row_format.format(
            f'x{i}',
            point,
            function_value,
            calc_function_value,
            abs(function_value - calc_function_value),
        ))
    print('-' * 85)

def print_adams_table(function: Callable[[float], float], step: float, count_of_points: int, values: List[float]):
    [values, function_values, first_differences, second_differences, third_differences, fourth_differences] = extrapolation_adams_method(values, function, step, count_of_points)
    header_format = "{:>6} {:>20} {:>25} {:>20} {:>20} {:>20} {:>20}"
    row_format = "{:>6} {:>20} {:>25} {:>20} {:>20} {:>20} {:>20}"
    print(header_format.format('Точка', 'Значение точки', "Значение функции y'", 'Первая разность', 'Вторая разность', 'Третья разность', 'Четвертая разность'))
    print('-' * 111)
    for i in range(count_of_points + 3):
        print(row_format.format(
            f'y{i - 2}',
            _get_value(values, i),
            _get_value(function_values, i),
            _get_value(first_differences, i),
            _get_value(second_differences, i),
            _get_value(third_differences, i),
            _get_value(fourth_differences, i),
        ))
    return

def _get_value(list_of_values: List[float], index: int):
    try:
        value = list_of_values[index]
    except IndexError:
        value = None
    
    if value is None:
        return "N/A"
    return f'{value:.6e}'
