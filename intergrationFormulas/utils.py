from typing import Callable, List
from methods import *

def float_check(input_string: str) -> float:
    """
    Checks the entered value for float compliance

    Args:
        input_string (str): Input string

    Returns:
        float: Input value converted to float
    """

    while (True):
        try:
            x = float(input(input_string))
            break
        except (ValueError, TypeError):
            print("Вы ввели неправильное значение, повторите ввод!")
    return x


def print_table(
        accurate_integral: float,
        function: Callable[[float], float],
        down_border: float,
        up_border: float,
    ):
    header_format = "{:<25} {:<25} {:<25} {:<25}"
    row_format = "{:<25} {:<25e} {:<25e} {:<25e}"
    print(header_format.format("Метод вычисления", "Значение", "Точное 'J'", "Погрешность"))
    methods_names = ['Левый прямоугольник', 'Правый прямоугольник', 'Средний прямоугольник', 'Трапеция', 'Симпсон', '3/8']
    methods_functions = [left_rectangle, right_rectangle, middle_rectangle, trapezoid, simpson, three_eighths]
    for i in range(6):
        value = methods_functions[i](function, down_border, up_border)
        print(row_format.format(
            methods_names[i],
            value,
            accurate_integral,
            abs(accurate_integral - value),
        ))

# def check_ADA(down_border: float, up_border: float, polynomials: Callable[[float], float]):
    
#     header_format = "{:<25} {:<25} {:<25} {:<25} {:<25}"
#     row_format = "{:<25} {:<25e} {:<25e} {:<25e} {:<25e}"
#     print(header_format.format("Метод вычисления", "Степень точности", "Значение", "Точное значение", "Погрешность"))
#     methods_names = ['Левый прямоугольник', 'Правый прямоугольник', 'Средний прямоугольник', 'Трапеция', 'Симпсон', '3/8']
#     methods_functions = [left_rectangle, right_rectangle, middle_rectangle, trapezoid, simpson, three_eighths]
#     ADA = [0, 0, 1, 1, 2, 3]
#     for i in range(6):
#         def sub_function(function: Callable[[float], float]):
#             return methods_functions[i](function, down_border, up_border)
#         const_value = sub_function(polynomials[i][0])
#         const_integral = abs(polynomials[i])
#         print(row_format.format(methods_names[i], ADA[i], ))