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
    row_format = "{:<25} {:<25.10e} {:<25.10e} {:<25.10e}"
    print()
    print(header_format.format("Метод вычисления", "Значение", "Точное 'J'", "Погрешность"))
    print("-" * 90)
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

def check_ADA(
        down_border: float,
        up_border: float,
        polynomials: List[Callable[[float], float]],
        antiderivatives: List[Callable[[float], float]]
):
    print("Метод вычисления: ")
    methods_names = ['Левый прямоугольник', 'Правый прямоугольник', 'Средний прямоугольник', 'Трапеция', 'Симпсон', '3/8']
    methods_functions = [left_rectangle, right_rectangle, middle_rectangle, trapezoid, simpson, three_eighths]
    ADA = [0, 0, 1, 1, 2, 3]
    for i in range(6):
        print(f'\n{i + 1})', methods_names[i], f'АСТ = {ADA[i]}:')
        def sub_function(function: Callable[[float], float]):
            return methods_functions[i](function, down_border, up_border)
        
        header_format = "\t{:<11} {:<23} {:<17} {:<17}"
        row_format = "\t{:<11} {:<23.10e} {:<17.10e} {:<17.10e}"
        print(header_format.format("Многочлен", "Приближенное значение", "Точное значение", "Погрешность"))
        print("\t" + "-" * 71)
        for j in range(ADA[i] + 1):
            approximate_value = sub_function(polynomials[j])
            accurate_integral = antiderivatives[j](up_border) - antiderivatives[j](down_border)
            inaccuracy = abs(approximate_value - accurate_integral)
            print(row_format.format("1" * (j == 0) + "x" * (j == 1) + f"x^{j}" * (j >= 2), approximate_value, accurate_integral, inaccuracy))
            