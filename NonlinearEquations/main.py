from numpy import sin, cos
from utils import float_check, int_check
from methods import (
    bisection_method,
    newton_method,
    modified_newton_method,
    secant_method,
    roots_separation)

# Напишите свою функцию здесь
func_str = "x - 10 * sin(x) = 0"


def f(x: float) -> float:
    # Напишите свою функцию здесь
    return x - 10 * sin(x)


def df(x: float) -> float:
    # Напишите производную своей функции здесь
    return 1 - 10 * cos(x)


print("Численные методы решения нелинейных уравнений")
print(f"Текущая функция - {func_str}")

while (True):
    A = float_check("Введите левую границу отрезка => ")
    B = float_check("Введите правую границу отрезка => ")
    if (B > A):
        break
    print("Левая граница отрезка не может быть больше правой! Повторите ввод.")

N = int_check("Введите количество отрезков для отделения корней => ")

while (True):
    degree = int_check("Введите степень точности искомого решения => ")
    if (degree > 15):
        print(
            "На данный момент из-за использования типа данных float",
            "поддерживается степень точности не более 10^(-15).",
            "Повторите ввод."
        )
        continue
    break

e = 10 ** (-degree)

print(f"""\nВходные параметры для задачи:
\tФункция: {func_str},
\tОтрезок поиска корней: [{A}, {B}]
\tТочность решения: 10^({-degree})\n""")

print(f"Этап 1. Отделение корней на отрезке [{A}, {B}]:")

root_segments = roots_separation(A, B, N, f)

print(
    f"\n\tЗаданное пользователем количество отрезков: {N}",
    f"Количество найденных отрезков корней: {len(root_segments)}",
    "\nНайденные отрезки: "
)

for root_segment in root_segments:
    print("\t" + str(root_segment))

print("\nЭтап 2. Нахождение корней численными методами:")

counter_segments = 0

for root_segment in root_segments:
    counter_segments += 1
    header_format = "{:<30} {:<50} {:<20} {:<25} {:<25} {:>25}"
    row_format = "{:<30} {:<50} {:<20} {:<25} {:<25} {:>25}"

    print(
        f"\n{counter_segments})",
        f"Отрезок - [{root_segment[0]}, {root_segment[1]}]",
    )
    print(header_format.format(
        "Название метода",
        "Начальное приближение",
        "Количество шагов",
        "Приближенное решение",
        "Погрешность решения",
        "Невязка функции"
    ))
    print("-" * 180)

    (x, delta, counter) = bisection_method(root_segment, f, e)
    print(row_format.format(
        "Метод бисекции", (root_segment[0] + root_segment[1]) / 2,
        counter, x, delta, abs(0 - f(x))))

    (x, delta, counter) = newton_method(root_segment, f, df, e)
    print(row_format.format(
        "Метод касательных", (root_segment[0] + root_segment[1]) / 2,
        counter, x, delta, abs(0 - f(x))))

    (x, delta, counter) = modified_newton_method(root_segment, f, df, e)
    print(row_format.format(
        "Модиф. метод касательных", (root_segment[0] + root_segment[1]) / 2,
        counter, x, delta, abs(0 - f(x))))

    (x, delta, counter) = secant_method(root_segment, f, e)
    print(row_format.format(
        "Метод секущих", f"[{root_segment[0]}, {root_segment[1]}]",
        counter, x, delta, abs(0 - f(x))))

    print("-" * 180)

input()
