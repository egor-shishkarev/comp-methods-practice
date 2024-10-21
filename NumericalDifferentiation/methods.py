from typing import Callable, List
from utils import int_check, float_check, print_table

def create_preparatory_table_equidistant(function: Callable[[float], float], count_of_points: int, initial_point: float, step: float):
    """

    """
    nodes: List[List[float]] = []

    current_point = initial_point
    for i in range(count_of_points):
        nodes.append([current_point, function(current_point)])
        current_point += step

    return nodes

def create_derivatives_table(
        preparatory_table: List[List[float]],
        derivative_first: Callable[[float], float],
        derivative_second: Callable[[float], float]
    ):
    list_of_first_derivatives = _get_first_derivatives(preparatory_table)
    list_of_first_derivatives_new = _get_first_derivatives_new(preparatory_table)
    list_of_second_derivatives = _get_second_derivatives(preparatory_table)
    list_of_inaccuracy_first = []
    list_of_inaccuracy_first_new = []
    list_of_inaccuracy_second = []
    list_of_points = []
    list_of_values = []
    for i in range(len(preparatory_table)):
        list_of_points.append(preparatory_table[i][0])
        list_of_values.append(preparatory_table[i][1])
        list_of_inaccuracy_first.append(abs(derivative_first(preparatory_table[i][0]) - list_of_first_derivatives[i]))
        list_of_inaccuracy_first_new.append(abs(derivative_first(preparatory_table[i][0]) - list_of_first_derivatives_new[i]))
        list_of_inaccuracy_second.append(abs(derivative_second(preparatory_table[i][0]) - list_of_second_derivatives[i]))
    derivative_table = [
        list_of_points,
        list_of_values,
        list_of_first_derivatives,
        list_of_inaccuracy_first,
        list_of_first_derivatives_new,
        list_of_inaccuracy_first_new,
        list_of_second_derivatives,
        list_of_inaccuracy_second
    ]
    return derivative_table

def _get_first_derivatives(preparatory_table: List[List[float]]):
    list_of_derivatives: List[float] = []
    step = preparatory_table[1][0] - preparatory_table[0][0]
    
    for i in range(len(preparatory_table)):
        if i == 0:
            value = (-3 * preparatory_table[i][1] + 4 * preparatory_table[i + 1][1] - preparatory_table[i + 2][1]) / (2 * step)
        elif i == len(preparatory_table) - 1:
            value = (3 * preparatory_table[i][1] - 4 * preparatory_table[i - 1][1] + preparatory_table[i - 2][1]) / (2 * step)
        else:
            value = (preparatory_table[i + 1][1] - preparatory_table[i - 1][1]) / (2 * step)

        list_of_derivatives.append(value)
    return list_of_derivatives

def _get_first_derivatives_new(preparatory_table: List[List[float]]):
    list_of_derivatives_new = []
    step = preparatory_table[1][0] - preparatory_table[0][0]

    for i in range(len(preparatory_table)):
        if i == 0:
            value = 1 / (12 * step) * (
                - 25 * preparatory_table[i][1] 
                + 48 * preparatory_table[i + 1][1] 
                - 36 * preparatory_table[i + 2][1]
                + 16 * preparatory_table[i + 3][1]
                - 3 * preparatory_table[i + 4][1]
            )
        elif i == 1:
            value = 1 / (12 * step) * (
                - 3 * preparatory_table[i - 1][1]
                - 10 * preparatory_table[i][1]
                + 18 * preparatory_table[i + 1][1]
                - 6 * preparatory_table[i + 2][1]
                + preparatory_table[i + 3][1]
            )
        elif i == len(preparatory_table) - 2:
            value = 1 / (12 * step) * (
                3 * preparatory_table[i + 1][1]
                + 10 * preparatory_table[i][1]
                - 18 * preparatory_table[i - 1][1]
                + 6 * preparatory_table[i - 2][1]
                - preparatory_table[i - 3][1]
            )
        elif i == len(preparatory_table) - 1:
            value = 1 / (12 * step) * (
                25 * preparatory_table[i][1]
                - 48 * preparatory_table[i - 1][1]
                + 36 * preparatory_table[i - 2][1]
                - 16 * preparatory_table[i - 3][1]
                + 3 * preparatory_table[i - 4][1]
            )
        else:
            value = 1 / (12 * step) * (
                preparatory_table[i - 2][1]
                - 8 * preparatory_table[i - 1][1]
                + 8 * preparatory_table[i + 1][1]
                - preparatory_table[i + 2][1]
            )

        list_of_derivatives_new.append(value)

    return list_of_derivatives_new

def _get_second_derivatives(preparatory_table: List[List[float]]):
    list_of_derivatives = []
    step = preparatory_table[1][0] - preparatory_table[0][0]

    for i in range(len(preparatory_table)):
        if i == 0:
            value = 1 / (step ** 2) * (
                2 * preparatory_table[i][1]
                - 5 * preparatory_table[i + 1][1]
                + 4 * preparatory_table[i + 2][1]
                - preparatory_table[i + 3][1]
            )
        elif i == len(preparatory_table) - 1:
            value = 1 / (step ** 2) * (
                2 * preparatory_table[i][1]
                - 5 * preparatory_table[i - 1][1]
                + 4 * preparatory_table[i - 2][1]
                - preparatory_table[i - 3][1]
            )
        else:
            value = 1 / (step ** 2) * (
                preparatory_table[i + 1][1]
                -2 * preparatory_table[i][1]
                + preparatory_table[i - 1][1]
            )
        list_of_derivatives.append(value)
    
    return list_of_derivatives

def create_table(function: Callable[[float], float]):
    while (True):
        count_of_points = int_check("Введите количество точек в таблице (не менее 5) => ")
        if (count_of_points < 5):
            print(f"\nВы ввели недопустимое число - {count_of_points}")
            print("Повторите ввод - >= 5")
            continue
        break

    initial_point = float_check("Введите начальное значение x0 => ")
    while (True):
        step = float_check("Введите шаг h > 0 => ")
        if (step <= 0):
            print(f"Вы ввели недопустимое число - {step}")
            print("Повторите ввод - > 0")
            continue
        break

    preparatory_table = create_preparatory_table_equidistant(function, count_of_points, initial_point, step)
    print_table(preparatory_table)

    return [preparatory_table, count_of_points, initial_point, step]

def choose_function(array_of_functions: List[Callable[[float], float]]):
    [function1, function1_string, derivative_first1, derivative_second1,
    function2, function2_string, derivative_first2, derivative_second2] = array_of_functions
    print(f"1) {function1_string}, 2) {function2_string}")
    while (True):
        function_number = int_check("Введите номер функции => ")
        if (function_number not in [1, 2]):
            print(f"\nВы ввели недопустимое число - {function_number}")
            print("Повторите ввод - 1 или 2")
            continue
        match(function_number):
            case 1: 
                function = function1
                function_string = function1_string
                derivative_first = derivative_first1
                derivative_second = derivative_second1
            case 2:
                function = function2
                function_string = function2_string
                derivative_first = derivative_first2
                derivative_second = derivative_second2
        break
    return [function, function_string, derivative_first, derivative_second]

def clarification_on_Runge_Romberg(approximate_value_h: float, approximate_value_h2: float):
    approximate_value = (2 ** 2 * approximate_value_h2 - approximate_value_h) / (2 ** 2 - 1)
    return approximate_value

def Runge_Romberg(function: Callable[[float], float],
                  preparatory_table: List[List[float]],
                  derivative_first: Callable[[float], float],
                  derivative_second: Callable[[float], float],
                  desired_number: int,
                  count_of_points: int,
                  initial_point: float,
                  step: float):
    derivatives_table = create_derivatives_table(preparatory_table, derivative_first, derivative_second)
    desired_value = derivatives_table[0][desired_number - 1]
    desired_function_value = derivatives_table[1][desired_number - 1]
    first_derivative_accurate = derivative_first(desired_value)
    second_derivative_accurate = derivative_second(desired_value)
    first_derivative_h = derivatives_table[2][desired_number - 1]
    second_derivative_h = derivatives_table[6][desired_number - 1]

    preparatory_table_h2 = create_preparatory_table_equidistant(function, count_of_points * 2 - 1, initial_point, step / 2)
    derivatives_table_h2 = create_derivatives_table(preparatory_table_h2, derivative_first, derivative_second)
    first_derivative_h2 = derivatives_table_h2[2][2 * (desired_number - 1)]
    second_derivative_h2 = derivatives_table_h2[6][2 * (desired_number - 1)]

    first_approximate_value = clarification_on_Runge_Romberg(first_derivative_h, first_derivative_h2)
    second_approximate_value = clarification_on_Runge_Romberg(second_derivative_h, second_derivative_h2)

    header_format = "{:<10} {:<15} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20}"
    row_format = "{:<10.6f} {:<15.6f} {:<20.10e} {:<20.10e} {:<20.10e} {:<20.10e} {:<20.10e} {:<20.10e}"
    print()
    print(header_format.format('xi', 'f(xi)', "J(h)", 'Погрешность', "J(h/2)", "Погрешность", "Уточн. J", "Погрешность"))
    print('-' * 64 + 'Для первой производной' + '-' * 64)
    print(row_format.format(
        desired_value,
        desired_function_value,
        first_derivative_h,
        abs(first_derivative_accurate - first_derivative_h),
        first_derivative_h2,
        abs(first_derivative_accurate - first_derivative_h2),
        first_approximate_value,
        abs(first_approximate_value - first_derivative_accurate)))
    print('-' * 64 + 'Для второй производной' + '-' * 64)
    print(row_format.format(
        desired_value,
        desired_function_value,
        second_derivative_h,
        abs(second_derivative_accurate - second_derivative_h),
        second_derivative_h2,
        abs(second_derivative_accurate - second_derivative_h2),
        second_approximate_value,
        abs(second_approximate_value - second_derivative_accurate)))
