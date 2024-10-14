from typing import Callable, List


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
    list_of_inaccuracy = []
    for i in range(len(preparatory_table)):
        list_of_inaccuracy.append(abs(derivative_first(preparatory_table[i][0]) - list_of_first_derivatives[i]))
    derivative_table = [list_of_first_derivatives, list_of_inaccuracy]
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
                + preparatory_table[i + 1][1]
            )
        list_of_derivatives.append(value)
    
    return list_of_derivatives