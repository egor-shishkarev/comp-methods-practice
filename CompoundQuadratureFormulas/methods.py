from typing import Callable, List

def left_rectangle(
        function: Callable[[float], float],
        down_border: float,
        up_border: float,
        count_of_intervals: int
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
        count_of_intervals: int
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
        count_of_intervals: int
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
        count_of_intervals: int
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
        count_of_intervals: int
    ):   
    step = (up_border - down_border) / count_of_intervals
    value = 0
    
    def point_j(j: float):
        return down_border + j * step

    for j in range(0, count_of_intervals):
        value += function(point_j(j))
        value += 4 * function(point_j(j + 1 / 2))
        value += function(point_j(j + 1))
    
    return (step / 6) * value

def print_table(
        function: Callable[[float], float],
        down_border: float,
        up_border: float,
        count_of_intervals: int,
        accurate_integral: float
    ):

    header_format = "{:>23} {:>20} {:>23} {:>24} {:>27}"
    row_format = "{:>23} {:>20.10e} {:>23.10e} {:>24.10e} {:>26.10f}%"
    print(f"\nТаблица для количества отрезков m = {count_of_intervals}:\n")
    print(header_format.format("Метод СКФ", "Точное значение", "Приближенное значение", "Абсолютная погрешность", "Относительная погрешность"))
    print('-' * 121)
    methods_names = ["Левый прямоугольник", "Правый прямоугольник", "Средний прямоугольник", "Трапеции", "Симпсон"]
    methods_functions = [left_rectangle, right_rectangle, middle_rectangle, trapezoid, simpson]

    for i in range(5):
        approximate_value = methods_functions[i](function, down_border, up_border, count_of_intervals)
        inaccuracy = abs(approximate_value - accurate_integral)
        relative_inaccuracy = inaccuracy / abs(accurate_integral)
        print(row_format.format(methods_names[i], accurate_integral, approximate_value, inaccuracy, relative_inaccuracy * 100))

def print_runge_correction(
        function: Callable[[float], float],
        down_border: float,
        up_border: float,
        count_of_intervals: int,
        multiplier: int,
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

    header_format = "{:>23} {:>20} {:>23} {:>24} {:>27}"
    row_format = "{:>23} {:>20.10e} {:>23.10e} {:>24.10e} {:>26.10f}%"
    print('\nУточнение по принципу Рунге:')
    print(f"Для количества отрезков m = {count_of_intervals} и m * l = {count_of_intervals * multiplier}:\n")
    print(header_format.format("Метод СКФ", "Точное значение", "Приближенное значение", "Абсолютная погрешность", "Относительная погрешность"))
    print('-' * 121)
    for i in range(5):
        runge_value = runge_correction(values_m[i], values_ml[i], multiplier, ADA[i])
        inaccuracy = abs(runge_value - accurate_integral)
        print(row_format.format(methods_names[i], accurate_integral, runge_value, inaccuracy, inaccuracy / abs(accurate_integral) * 100))
    
def runge_correction(first_value: float, second_values: float, multiplier: float, ADA: float):
    return (multiplier ** (ADA + 1) * second_values - first_value) / (multiplier ** (ADA + 1) - 1)

def check_ADA(
        down_border: float,
        up_border: float,
        polynomials: List[Callable[[float], float]],
        antiderivatives: List[Callable[[float], float]],
        count_of_intervals: int
    ):
    print("\nПроверка формул на многочленах степени 0 - 3:")
    methods_names = ['Левый прямоугольник', 'Правый прямоугольник', 'Средний прямоугольник', 'Трапеция', 'Симпсон', '3/8']
    methods_functions = [left_rectangle, right_rectangle, middle_rectangle, trapezoid, simpson]
    ADA = [0, 0, 1, 1, 3]
    for i in range(5):
        print(f'\n{i + 1})', methods_names[i], f'АСТ = {ADA[i]}:')
        def sub_function(function: Callable[[float], float]):
            return methods_functions[i](function, down_border, up_border, count_of_intervals)
        
        header_format = "\t{:>11} {:>23} {:>17} {:>17}"
        row_format = "\t{:>11} {:>23.10e} {:>17.10e} {:>17.10e}"
        print(header_format.format("Многочлен", "Приближенное значение", "Точное значение", "Погрешность"))
        print("\t  " + "-" * 69)
        for j in range(ADA[i] + 1):
            approximate_value = sub_function(polynomials[j])
            accurate_integral = abs(antiderivatives[j](up_border) - antiderivatives[j](down_border))
            inaccuracy = abs(approximate_value - accurate_integral)
            print(row_format.format("1" * (j == 0) + "x" * (j == 1) + f"x^{j}" * (j >= 2), approximate_value, accurate_integral, inaccuracy))
        