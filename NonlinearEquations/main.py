from numpy import *

func_str = "x - 10 * sin(x)" # Type your function here

print("Задача решения нелинейных уравнений")
print(f"Текущая функция для нахождения нечетных корней - {func_str}")
# A = int(input("Введите левую границу отрезка => "))
# B = int(input("Введите правую границу отрезка => "))
# print(f"Для начала отделим корни на отрезке [{A}, {B}]")
# N = int(input("Введите количество отрезков "))

def f(x):
    return x - 10 * sin(x)

def df(x):
    return 1 - 10 * cos(x)

def bisection_method(root_segment: list):
    a = root_segment[0]
    b = root_segment[1]
    counter = 0

    while (b - a) > 2 * e:
        c = (a + b) / 2
        if (f(a) * f(c)) <= 0:
            b = c
        else:
            a = c

        counter += 1
    
    x = (a + b) / 2
    delta = (b - a) / 2
    
    return (x, delta, counter)

def newton_method(root_segment):
    a = root_segment[0]
    b = root_segment[1]
    counter = 0

    x_prev = (a + b) / 2
    x_current = x_prev - (f(x_prev)) / (df(x_prev))

    while (abs(x_current - x_prev)) > e:
        x_prev = x_current
        x_current = x_prev - (f(x_prev)) / (df(x_prev))
        counter += 1

    return (x_current, (x_current - x_prev), counter)


def modified_newton_method(root_segment): 
    a = root_segment[0]
    b = root_segment[1]
    x0 = (a + b) / 2
    counter = 0

    x_prev = (a + b) / 2
    x_current = x_prev - (f(x_prev)) / (df(x0))

    while (abs(x_current - x_prev)) > e:
        x_prev = x_current
        x_current = x_prev - (f(x_prev)) / (df(x0))
        counter += 1

    return (x_current, (x_current - x_prev), counter)

def secant_method(root_segment):
    a = root_segment[0]
    b = root_segment[1]
    x0 = (a + b) / 2
    counter = 0

    x_prev = a
    x_current = b
    x_next = x_prev - (f(x_current)) / (f(x_current) - f(x_prev)) * (x_current - x_prev)

    while (abs(x_current - x_prev)) > e:
        x_prev = x_current
        x_current = x_next
        x_next = x_prev - (f(x_current)) / (f(x_current) - f(x_prev)) * (x_current - x_prev)
        counter += 1

    return (x_current, (x_current - x_prev), counter)

A = -5
B = 3
N = 10000
e = 10 ** (-6)

h = (B - A) / N
x1 = A 
x2 = x1 + h
root_segments = []
while (x2 < B):
    y1 = f(x1)
    y2 = f(x2)

    if (y1 * y2 < 0):
        root_segments.append([x1, x2])
    
    x1 = x2
    x2 = x1 + h

for root_segment in root_segments:
    print(f"\nОтрезок - [{root_segment[0]}, {root_segment[1]}]")
    (x, delta, counter) = bisection_method(root_segment)
    print(f"Корень уравнения - {x}, погрешность решения - {delta}, количество итераций - {counter}, невязка - {abs(0 - f(x))}")
    (x, delta, counter) = newton_method(root_segment)
    print(f"Корень уравнения - {x}, погрешность решения - {delta}, количество итераций - {counter}, невязка - {abs(0 - f(x))}")
    (x, delta, counter) = modified_newton_method(root_segment)
    print(f"Корень уравнения - {x}, погрешность решения - {delta}, количество итераций - {counter}, невязка - {abs(0 - f(x))}")
    (x, delta, counter) = modified_newton_method(root_segment)
    print(f"Корень уравнения - {x}, погрешность решения - {delta}, количество итераций - {counter}, невязка - {abs(0 - f(x))}")
    