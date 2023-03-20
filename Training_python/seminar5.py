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