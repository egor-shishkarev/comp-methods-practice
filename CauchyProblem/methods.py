from typing import Callable, List

def extrapolation_adams_method(values: List[float], function: Callable[[float], float], step: float, count_of_points: int):
    # ЭМА 4-ого порядка для точек 3, 4, 5, ...
    # 1, 1/2, 5/12, 3/8, 251/720
    values = values
    first_differences = []
    second_differences = []
    third_differences = []
    fourth_differences = []
    #for _ in range(3, count_of_points + 1):

    return

def runge_kutta_method(first_value: float, function: Callable[[float], float], step: float, count_of_points: int):
    list_of_values = [first_value]
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
    list_of_values = [first_value]
    current_value = first_value
    for _ in range(1, count_of_points + 1):
        current_value = current_value + step * function(current_value) # y_k+1 = y_k + h * f(y_k), так как y' = -y + y^2, то есть зависит только от y 
        list_of_values.append(current_value)
    return list_of_values

def euler_first_method(first_value: float, function: Callable[[float], float], step: float, count_of_points: int):
    list_of_values = [first_value]
    current_value = first_value
    for _ in range(1, count_of_points + 1):
        additional_value = current_value + step / 2 * function(current_value)

        current_value = current_value + step * function(additional_value)
        list_of_values.append(current_value)
    return list_of_values

def euler_second_method(first_value: float, function: Callable[[float], float], step: float, count_of_points: int):
    list_of_values = [first_value]
    current_value = first_value
    for _ in range(1, count_of_points + 1):
        additional_value = current_value + step * function(current_value)

        current_value = current_value + step / 2 * (function(current_value) + function(additional_value))
        list_of_values.append(current_value) 
    return list_of_values
