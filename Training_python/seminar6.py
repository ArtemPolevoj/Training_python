def get_number(str):
    try:
        number = int(input(str))
    except ValueError:
        print('Введено не число')
        return get_number(str)
    return number


def get_number_not_negativ(str):
    number = get_number(str)
    if number < 0:
        print('Количество не может быть отрицательным')
        return get_number_not_negativ(str)
    return number

"""
Задача 30:
Заполните массив элементами арифметической прогрессии. Её первый элемент,
разность и количество элементов нужно ввести с клавиатуры.
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.
"""
array = []
first_element = get_number_not_negativ('Enter first element: ')
difference = get_number_not_negativ('Enter differens: ')
quantity = get_number_not_negativ('Enter quantity: ')
for i in range(1,quantity + 1):
    array.append(first_element + (i - 1) * difference)
print(*array, sep = '\n')