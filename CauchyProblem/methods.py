from typing import Callable, List

def extrapolation_adams_method(values: List[float], function: Callable[[float], float], step: float, count_of_points: int):
    # Рассчитываем f(y) для начальных значений
    function_values = [function(y) for y in values]

    # Рассчитываем конечные разности
    first_differences = [function_values[i] - function_values[i + 1] for i in range(len(function_values) - 1)]
    second_differences = [first_differences[i] - first_differences[i + 1] for i in range(len(first_differences) - 1)]
    third_differences = [second_differences[i] - second_differences[i + 1] for i in range(len(second_differences) - 1)]
    fourth_differences = [third_differences[i] - third_differences[i + 1] for i in range(len(third_differences) - 1)]

    # Текущее значение
    current_value = values[-1]

    # Вычисляем новые значения
    for _ in range(3, count_of_points + 1):
        # Добавляем новое значение y_{n+1}
        current_value += step * (
            function_values[-1] +
            1 / 2 * first_differences[-1] +
            5 / 12 * second_differences[-1] +
            3 / 8 * third_differences[-1] +
            251 / 720 * fourth_differences[-1]
        )
        values.append(current_value)
        new_f = function(current_value)
        function_values.append(new_f)

        # Пересчитываем конечные разности
        first_differences.append(function_values[-2] - function_values[-1])
        second_differences.append(first_differences[-2] - first_differences[-1])
        third_differences.append(second_differences[-2] - second_differences[-1])
        fourth_differences.append(third_differences[-2] - third_differences[-1])

    return [values, function_values, first_differences, second_differences, third_differences, fourth_differences]


def runge_kutta_method(first_value: float, function: Callable[[float], float], step: float, count_of_points: int):
    list_of_values = []
    current_value = first_value
    for _ in range(1, count_of_points + 1):
        first_additional_value = step * function(current_value)
        second_additional_value = step * function(current_value + first_additional_value / 2)
        third_additional_value = step * function(current_value + second_additional_value / 2)
        fourth_additional_value = step * function(current_value + third_additional_value)

        current_value = current_value + 1 / 6 * (first_additional_value + 2 * second_additional_value + 2 * third_additional_value + fourth_additional_value)
        list_of_values.append(current_value)
    return list_of_values

def euler_method(first_value: float, function: Callable[[float], float], step: float, count_of_points: int):
    list_of_values = []
    current_value = first_value
    for _ in range(1, count_of_points + 1):
        current_value = current_value + step * function(current_value) # y_k+1 = y_k + h * f(y_k), так как y' = -y + y^2, то есть зависит только от y 
        list_of_values.append(current_value)
    return list_of_values

def euler_first_method(first_value: float, function: Callable[[float], float], step: float, count_of_points: int):
    list_of_values = []
    current_value = first_value
    for _ in range(1, count_of_points + 1):
        additional_value = current_value + step / 2 * function(current_value)

        current_value = current_value + step * function(additional_value)
        list_of_values.append(current_value)
    return list_of_values

def euler_second_method(first_value: float, function: Callable[[float], float], step: float, count_of_points: int):
    list_of_values = []
    current_value = first_value
    for _ in range(1, count_of_points + 1):
        additional_value = current_value + step * function(current_value)

        current_value = current_value + step / 2 * (function(current_value) + function(additional_value))
        list_of_values.append(current_value) 
    return list_of_values

def taylor_function(x: float):
    return 1 / 2 - 1 / 4 * x + 1 / 48 * x ** 3 - 1 / 480 * x ** 5 + 17 / 80640 * x ** 7 - 31 / 1451520 * x ** 9
    # return 1 / 2 - 1 / 4 * x + 1 / 48 * x ** 3