# Вариант 4 - a = 0, b = 0.7, x = 0.4, n = 7, m = 15.

from math import sqrt
from utils import int_check, float_check, print_table
from methods import (
    create_preparatory_table_chebyshev,
    create_preparatory_table_equidistant, 
    get_value_of_Lagrange_polynomial,
    get_inaccuracy,
    sort_table_according_to_point)

function_string = "√(1+x^2)" #"x^2 + 1"

def function(x: float):
    return sqrt(1 + x ** 2) #x ** 2 + 1

print('Задача алгебраического интерполирования. Интерполяционный многочлен в форме Лагранжа.')
print(f'Номер варианта - 4, функция - {function_string}')
count_of_points = int_check('\nВведите число m - количество точек в таблице - 1 => ')
left_border = float_check('Введите левую границу отрезка => ')
right_border = float_check('Введите правую границу отрезка => ')
while (left_border >= right_border):
    print('Левая граница не может быть больше правой! Повторите ввод.')
    left_border = float_check('Введите левую границу отрезка => ')
    right_border = float_check('Введите правую границу отрезка => ')

preparatory_table = create_preparatory_table_equidistant(function, count_of_points, left_border, right_border)
print(f'\nЭтап 1 - нахождение таблицы значений для заданного числа m - {count_of_points}')
print(f'Таблица "точка - значение функции" для отрезка [{left_border}, {right_border}]:')
print_table(preparatory_table)

while (True):
    desired_point = float_check('\nВведите точку, в которой хотите найти приближенное значение функции => ')

    while (True):
        degree_of_interpolation_polynomial = int_check('Введите степень интерполяционного многочлена => ')
        if (degree_of_interpolation_polynomial > count_of_points):
            print('Степень интерполяционного многочлена не может быть больше, чем количество точек - 1!')
            print('Повторите ввод.')
            continue
        break

    sorted_table = sort_table_according_to_point(preparatory_table, desired_point, degree_of_interpolation_polynomial)

    print(f'\nЭтап 2 - нахождение значения интерполяционного многочлена Лагранжа:')
    print(f'\nИсходные данные -\n\tФункция - {function_string},\n\tОтрезок - [{left_border}, {right_border}],',
          f'\n\tСтепень искомого многочлена - {degree_of_interpolation_polynomial},\n\tТочка - {desired_point}'
          f'\n\tТаблица значений -')

    print_table(sorted_table)

    desired_value = get_value_of_Lagrange_polynomial(desired_point, sorted_table)

    print(f'\nЗначение в точке {desired_point} вычисленное с помощью интерполяционного многочлена Лагранжа - {desired_value}')

    inaccuracy = get_inaccuracy(desired_value, desired_point, function)

    print(f'Фактическая погрешность значения - {inaccuracy}')

    decision = input('Хотите ввести новые значения искомой точки и степень многочлена? (Y/N)').upper()
    
    if decision != 'Y':
        break
