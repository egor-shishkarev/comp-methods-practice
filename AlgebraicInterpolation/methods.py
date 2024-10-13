from typing import Callable, List
from math import cos, pi

def create_preparatory_table_chebyshev(function: Callable[[float], float], count_of_points: int, left_border: float, right_border: float):
    """

    """
    nodes: List[List[float]] = []

    # Use Chebyshev nodes
    chebyshev_nodes: List[float] = []

    for i in range(count_of_points + 1):
        chebyshev_nodes.append(cos(pi * (2 * i + 1) / (2 * count_of_points + 1)))

    for i in range(count_of_points + 1):
        current_point = (left_border + right_border) / 2 + (right_border - left_border) / 2 * chebyshev_nodes[i]
        nodes.append([current_point, function(current_point)])

    return nodes

def create_preparatory_table_equidistant(function: Callable[[float], float], count_of_points: int, left_border: float, right_border: float):
    """

    """
    nodes: List[List[float]] = []


    for i in range(count_of_points + 1):
        current_point = left_border + i * (right_border - left_border) / count_of_points
        nodes.append([current_point, function(current_point)])

    return nodes

def get_value_of_Lagrange_polynomial(desired_point: float, sorted_table: List[List[float]]):
    """

    """
    desired_value = 0

    for i in range(len(sorted_table)):
        numerator = 1
        denominator = 1
        for j in range(len(sorted_table)):
            if (i != j):
                numerator *= (desired_point - sorted_table[j][0])
                denominator *= (sorted_table[i][0] - sorted_table[j][0])
        desired_value += (numerator / denominator) * sorted_table[i][1]
        
    return desired_value

def get_inaccuracy(desired_value: float, desired_point: float, function: Callable[[float], float]):
    """

    """
    return abs(desired_value - function(desired_point))

def sort_table_according_to_point(table: List[List[float]], point: float, degree_of_interpolation_polynomial: int):
    """
    
    """
    return sorted(table, key=lambda element: abs(element[0] - point))[:degree_of_interpolation_polynomial + 1]
