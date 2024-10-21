from math import sqrt, exp
from utils import int_check, print_derivatives_table
from methods import (
    create_table,
    choose_function,
    create_derivatives_table,
    Runge_Romberg
)

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

array_of_functions = [function1, function1_string, derivative_first1, derivative_second1,
                      function2, function2_string, derivative_first2, derivative_second2]

print('\n"Нахождение производных таблично-заданной функции по формулам численного дифференцирования"\n')
print("Выберите функцию, для которой хотите решить задачу - ")

decision = 1
while (True):
    match(decision):
        case 0:
            print("Программа завершена.")
            break

        case 1:
            [function, function_string, derivative_first, derivative_second] = choose_function(array_of_functions)
            [preparatory_table, count_of_points, initial_point, step] = create_table(function, derivative_first, derivative_second)
            derivatives_table = create_derivatives_table(preparatory_table, derivative_first, derivative_second)
            print_derivatives_table(derivatives_table)
            
        case 2:
            [preparatory_table, count_of_points, initial_point, step] = create_table(function, derivative_first, derivative_second)
            derivatives_table = create_derivatives_table(preparatory_table, derivative_first, derivative_second)
            print_derivatives_table(derivatives_table)

        case 3:
            print("Уточнение по Рунге-Ромбергу:")
            new_table_decision = input('Хотите выбрать новую функцию/таблицу? (Y/N) => ')
            if (new_table_decision.upper() == 'Y'):
                [function, function_string, derivative_first, derivative_second] = choose_function(array_of_functions)
                [preparatory_table, count_of_points, initial_point, step] = create_table(function, derivative_first, derivative_second)
                derivatives_table = create_derivatives_table(preparatory_table, derivative_first, derivative_second)
                print_derivatives_table(derivatives_table)
            
            desired_number = int_check('\nВведите номер значения, для которого хотите уточнить производную => ')
            while (desired_number < 1 or desired_number > len(preparatory_table)):
                desired_number = int_check('Такого значения нет в таблице, повторите ввод => ') 

            Runge_Romberg(function, preparatory_table, derivative_first, derivative_second, desired_number, count_of_points, initial_point, step)
        case _:
            print('Такого значения нет в списке, повторите ввод!')

    print("\nХотите изменить параметры?")
    decision = int_check("Введите цифру чтобы:\n0 - выйти из программы,\n1 - выбрать другую функция,\n2 - ввести новые значения параметров таблицы,\n" +
                "3 - уточнить по Рунге-Ромбергу\n => ")
