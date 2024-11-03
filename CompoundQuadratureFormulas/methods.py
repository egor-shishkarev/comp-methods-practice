from typing import Callable

def left_rectangle(
        function: Callable[[float], float],
        down_border: float,
        up_border: float,
        count_of_intervals: float
    ):
    step = (up_border - down_border) / count_of_intervals
    value = 0
    for i in range(count_of_intervals):
        value += function(down_border + i * step)
    return step * value

def right_rectangle(
        function: Callable[[float], float],
        down_border: float,
        up_border: float,
        count_of_intervals: float
    ):
    step = (up_border - down_border) / count_of_intervals
    value = 0
    for i in range(count_of_intervals):
        value += function(down_border + (i + 1) * step)
    return step * value

def middle_rectangle(
        function: Callable[[float], float],
        down_border: float,
        up_border: float,
        count_of_intervals: float
    ):
    step = (up_border - down_border) / count_of_intervals
    value = 0
    for i in range(count_of_intervals):
        value += function(down_border + (i + 1 / 2) * step)
    return step * value

def trapezoid(
        function: Callable[[float], float],
        down_border: float,
        up_border: float,
        count_of_intervals: float
    ):
    step = (up_border - down_border) / count_of_intervals
    value = 0
    for i in range(count_of_intervals + 1):
        if (i == 0):
            value += function(down_border)
        elif (i == count_of_intervals):
            value += function(up_border)
        else:
            value += 2 * function(down_border + i * step)
    return step / 2 * value

def simpson(
        function: Callable[[float], float],
        down_border: float,
        up_border: float,
        count_of_intervals: float
    ):
    step = (up_border - down_border) / count_of_intervals
    value = 0
    for i in range(count_of_intervals + 1):
        if (i == 0):
            value += function(down_border)
        elif (i == count_of_intervals):
            value += function(up_border)
        else:
            value += 2 * function(down_border + i * step)
            value += 4 * function(down_border + (i + 1 / 2) * step)
    return step / 6 * value

def print_table(
        function: Callable[[float], float],
        down_border: float,
        up_border: float,
        count_of_intervals: float,
        accurate_integral: float
    ):

    header_format = "{:<23} {:<23} {:<24} {:<27}"
    row_format = "{:<23} {:<23.10e} {:<24.10e} {:<27.10f}"
    print()
    print(header_format.format("Метод СКФ", "Приближенное значение", "Абсолютная погрешность", "Относительная погрешность"))
    print('-' * 100)
    methods_names = ["Левый прямоугольник", "Правый прямоугольник", "Средний прямоугольник", "Трапеции", "Симпсон"]
    methods_functions = [left_rectangle, right_rectangle, middle_rectangle, trapezoid, simpson]

    for i in range(5):
        approximate_value = methods_functions[i](function, down_border, up_border, count_of_intervals)
        inaccuracy = abs(approximate_value - accurate_integral)
        relative_inaccuracy = inaccuracy / abs(accurate_integral)
        print(row_format.format(methods_names[i], approximate_value, inaccuracy, relative_inaccuracy))

def print_runge_correction(
        function: Callable[[float], float],
        down_border: float,
        up_border: float,
        count_of_intervals: float,
        multiplier: float,
        accurate_integral: float
    ):
    values_m = []
    values_ml = []
    methods_names = ["Левый прямоугольник", "Правый прямоугольник", "Средний прямоугольник", "Трапеции", "Симпсон"]
    methods_functions = [left_rectangle, right_rectangle, middle_rectangle, trapezoid, simpson]
    ADA = [0, 0, 1, 1, 3]

    for i in range(5):
        value_m = methods_functions[i](function, down_border, up_border, count_of_intervals)
        value_ml = methods_functions[i](function, down_border, up_border, count_of_intervals * multiplier)
        values_m.append(value_m)
        values_ml.append(value_ml)

    header_format = "{:<23} {:<23} {:<24} {:<27}"
    row_format = "{:<23} {:<23.10e} {:<24.10e} {:<27.10f}"
    print('\nУточнение по принципу Рунге:')
    print(header_format.format("Метод СКФ", "Приближенное значение", "Абсолютная погрешность", "Относительная погрешность"))
    print('-' * 100)
    for i in range(5):
        runge_value = runge_correction(values_m[i], values_ml[i], multiplier, ADA[i])
        inaccuracy = abs(runge_value - accurate_integral)
        print(row_format.format(methods_names[i], runge_value, inaccuracy, inaccuracy / abs(accurate_integral)))
    
def runge_correction(first_value: float, second_values: float, multiplier: float, ADA: float):
    return (multiplier ** (ADA + 1) * second_values - first_value) / (multiplier ** (ADA + 1) - 1)
