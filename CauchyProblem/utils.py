from typing import Callable
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

def print_taylor_table(taylor_function: Callable[[float], float], function: Callable[[float], float], step: float, count_of_points: int, original_point: float):
    print('Сравнение точного решения и решения "по Тейлору"\n')
    header_format = "{:>6} {:>15} {:>20} {:>25} {:>15}"
    row_format = "{:>6} {:>15.6f} {:>20.6e} {:>25.6e} {:>15.6e}"
    
    print(header_format.format('Точка', 'Значение точки', 'Точное значение', 'Значение по Тейлору', 'Погрешность'))
    print('-' * 85)
    for i in range(-2, count_of_points + 1, 1):
        point = original_point + i * step
        function_value = function(point)
        taylor_function_value = taylor_function(point)
        print(row_format.format(
            f'x{i}',
            point,
            function_value,
            taylor_function_value,
            abs(function_value - taylor_function_value),
        ))

def print_euler_table(original_function: Callable[[float], float], function: Callable[[float], float], step: float, count_of_points: int, original_point: float):
    print('Сравнение точного решения и решения "по Эйлеру"\n')
    header_format = "{:>6} {:>15} {:>20} {:>25} {:>15}"
    row_format = "{:>6} {:>15.6f} {:>20.6e} {:>25.6e} {:>15.6e}"
    
    print(header_format.format('Точка', 'Значение точки', 'Точное значение', 'Значение по Эйлеру', 'Погрешность'))
    print('-' * 85)
    euler_values = euler_method(original_function(original_point), function, step, count_of_points)
    for i in range(1, count_of_points + 1):
        point = original_point + i * step
        function_value = original_function(point)
        print(row_format.format(
            f'x{i}',
            point,
            function_value,
            euler_values[i],
            abs(function_value - euler_values[i]),
        ))

def print_euler_first_table(original_function: Callable[[float], float], function: Callable[[float], float], step: float, count_of_points: int, original_point: float):
    print('Сравнение точного решения и решения "по Эйлеру I"\n')
    header_format = "{:>6} {:>15} {:>20} {:>25} {:>15}"
    row_format = "{:>6} {:>15.6f} {:>20.6e} {:>25.6e} {:>15.6e}"
    
    print(header_format.format('Точка', 'Значение точки', 'Точное значение', 'Значение по Эйлеру I', 'Погрешность'))
    print('-' * 85)
    euler_values = euler_first_method(original_function(original_point), function, step, count_of_points)
    for i in range(1, count_of_points + 1):
        point = original_point + i * step
        function_value = original_function(point)
        print(row_format.format(
            f'x{i}',
            point,
            function_value,
            euler_values[i],
            abs(function_value - euler_values[i]),
        ))

def print_euler_second_table(original_function: Callable[[float], float], function: Callable[[float], float], step: float, count_of_points: int, original_point: float):
    print('Сравнение точного решения и решения "по Эйлеру II"\n')
    header_format = "{:>6} {:>15} {:>20} {:>25} {:>15}"
    row_format = "{:>6} {:>15.6f} {:>20.6e} {:>25.6e} {:>15.6e}"
    
    print(header_format.format('Точка', 'Значение точки', 'Точное значение', 'Значение по Эйлеру II', 'Погрешность'))
    print('-' * 85)
    euler_values = euler_second_method(original_function(original_point), function, step, count_of_points)
    for i in range(1, count_of_points + 1):
        point = original_point + i * step
        function_value = original_function(point)
        print(row_format.format(
            f'x{i}',
            point,
            function_value,
            euler_values[i],
            abs(function_value - euler_values[i]),
        ))

def print_runge_kutta_table(original_function: Callable[[float], float], function: Callable[[float], float], step: float, count_of_points: int, original_point: float):
    print('Сравнение точного решения и решения "по Рунге-Кутта"\n')
    header_format = "{:>6} {:>15} {:>20} {:>25} {:>15}"
    row_format = "{:>6} {:>15.6f} {:>20.6e} {:>25.6e} {:>15.6e}"
    
    print(header_format.format('Точка', 'Значение точки', 'Точное значение', 'Значение по Рунге-Кутта', 'Погрешность'))
    print('-' * 85)
    euler_values = runge_kutta_method(original_function(original_point), function, step, count_of_points)
    for i in range(1, count_of_points + 1):
        point = original_point + i * step
        function_value = original_function(point)
        print(row_format.format(
            f'x{i}',
            point,
            function_value,
            euler_values[i],
            abs(function_value - euler_values[i]),
        ))

def print_adams_table():
    return