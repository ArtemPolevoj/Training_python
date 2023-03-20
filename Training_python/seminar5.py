"""
Задача 26:
Напишите программу, которая на вход принимает
два числа A и B, и возводит число А в целую степень B с
помощью рекурсии.
"""
def get_number(string):
    global num
    try:
        num = int(input(string))
    except ValueError:
        print('Введено не число')
        get_number(string)
    return num

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
def get_number(string):
    global num
    try:
        num = int(input(string))
    except ValueError:
        print('Введено не число')
        get_number(string)
    if num < 0:
        print('Введено отрицательное число')
        get_number(string)
    return num

def get_sum(a, b):
    if b == 0:
        return a
    else:
        return get_sum(a + 1, b - 1)

num_A = get_number('Введите целое не отрицательное число A: ')
num_B = get_number('Введите целое не отрицательное число B: ')
result = get_sum(num_A, num_B)
print(f'{num_A} + {num_B} = {result}')