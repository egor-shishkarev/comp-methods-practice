from math import sqrt, exp
from utils import int_check, float_check, print_table, print_derivatives_table
from methods import create_preparatory_table_equidistant, create_derivatives_table

function1_string = "√(1+x^2)"
function2_string = "exp(6x)"

def function1(x: float):
    return sqrt(1 + x ** 2)

def derivative_first1(x: float):
    return x / sqrt(1 + x ** 2)

def derivative_second1(x: float):
    return (function1(x) - x * derivative_first1(x)) / (1 + x ** 2)

def function2(x: float):
    return exp(6 * x)

def derivative_first2(x: float):
    return 6 * exp(6 * x)

def derivative_second2(x: float):
    return 36 * exp(6 * x)

print('\n"Нахождение производных таблично-заданной функции по формулам численного дифференцирования"\n')
print("Выберите функцию, для которой хотите решить задачу - ")
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

derivative_table = create_derivatives_table(preparatory_table, derivative_first, derivative_second)

print_derivatives_table(derivative_table)