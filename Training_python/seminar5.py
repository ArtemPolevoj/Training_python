def get_number(string):
    try:
        number = int(input(string))
    except ValueError:
        print('Введено не число')
        return get_number(string)
    return number

def get_number_not_negativ(str):
    number = get_number(str)
    if number < 0:
        print('Значение не может быть отрицательным')
        return get_number_not_negativ(str)
    return number


"""
Задача 26:
Напишите программу, которая на вход принимает
два числа A и B, и возводит число А в целую степень B с
помощью рекурсии.
"""


def get_degree(number, degree):
    if degree == 1:
        return number
    elif degree == 0:
        return 1
    elif degree > 1:
        number = number * get_degree(number, degree - 1)
    else:
        number = round(1 / get_degree(number, abs(degree)), 5)
    return number

number = get_number('Введите число: ')
degree = get_number('Введите степень: ')
result = get_degree(number, degree)
print(f'{number} в степени {degree} = {result}')
"""
Задача 28:
Напишите рекурсивную функцию sum(a, b),
возвращающую сумму двух целых неотрицательных чисел. Из
всех арифметических операций допускаются только +1 и -1.
Также нельзя использовать циклы.
"""

def get_sum(a, b):
    if b == 0:
        return a
    else:
        return get_sum(a + 1, b - 1)

num_A = get_number_not_negativ('Введите целое не отрицательное число A: ')
num_B = get_number_not_negativ('Введите целое не отрицательное число B: ')
result = get_sum(num_A, num_B)
print(f'{num_A} + {num_B} = {result}')

"""
Задание 1.
Написать программу, которая будет складывать, вычитать,
умножать или делить два числа. Числа и знак операции вводятся пользователем.
После выполнения вычисления программа не должна завершаться, а должна
запрашивать новые данные для вычислений. Завершение программы должно
выполняться при вводе символа '0' в качестве знака операции. Если пользователь
вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна
сообщать ему об ошибке и снова запрашивать знак операции.
Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.
Подсказка:
Вариант исполнения:
- условие рекурсивного вызова - введена операция +, -, *, / - ШАГ РЕКУРСИИ
- условие завершения рекурсии - введена операция 0 - БАЗОВЫЙ СЛУЧАЙ
Решите через рекурсию. В задании нельзя применять циклы.
Пример:
Введите операцию (+, -, *, / или 0 для выхода): +
Введите первое число: 214
Введите второе число: 234
Ваш результат 448
Введите операцию (+, -, *, / или 0 для выхода): -
Введите первое число: вп
Вы вместо трехзначного числа ввели строку (((. Исправьтесь
Введите операцию (+, -, *, / или 0 для выхода):
"""
def get_mark(str):
   mark = input(str)
   if mark == '*' or mark == '/' or mark == '+' or mark == '+' \
           or mark == '-' or mark == '0':
       return mark
   else:
       print('Введен неверный символ, попробуйте еще раз')
       return get_mark(str)

def calculator():
    mark = get_mark('Введите операцию (+, -, *, / или 0 для выхода): ')
    if mark == '0':
        return
    number1 = get_number('Введите первое число: ')
    number2 = get_number('Введите второе число: ')
    if mark == '*':
        print(f'Ваш результат {number1 * number2}')
        return calculator()
    elif mark == '+':
        print(f'Ваш результат = {number1 + number2}')
        return calculator()
    elif mark == '-':
        print(f'Ваш результат = {number1 - number2}')
        return calculator()
    elif mark == '/':
        try:
            print(f'Ваш результат = {number1 / number2}')
        except ZeroDivisionError:
            print('Деление на 0 невозможно')
        finally:
            return calculator()


calculator()

"""
Задание 2.
Подсчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
и смотреть является ли она четной или нечетной.
При этом увеличиваем соответствующий счетчик
Пока все числа не извлечены, рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены
Используем операции % //. Операции взятия по индексу применять нельзя.
Решите через рекурсию. В задании нельзя применять циклы.
Пример:
Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)
"""
def get_count_number(value, number_even = 0, number_odd = 0):
    if value == 0:
        return (number_even, number_odd)
    else:
        temp = value % 10
        value = value // 10
        if temp % 2 == 0:
            return get_count_number(value,number_even + 1, number_odd)
        else:
            return get_count_number(value,number_even, number_odd + 1)


value = get_number('Введите число: ')
list_count = get_count_number(value)
print(f'Количество четных и нечетных цифр в числе равно {list_count}')