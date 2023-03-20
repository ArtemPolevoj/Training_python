"""
Задача 22:
Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
Выдать без повторений в порядке возрастания все те числа, которые
встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества.
m - кол-во элементов второго множества.
Элементы множеств получаются рандомно.
"""
import random


def get_number(string):
    global number
    try:
        number = int(input(string))
    except ValueError:
        print('Введено не число')
        get_number(string)
    return number


def get_list(string, fist_number, last_number):
    length_list = get_number(string)
    array = []
    for i in range(length_list):
        array.append(random.randint(fist_number, last_number))
    return array


list_1 = get_list('Введите количество элементов первого списка: ', 1, 20)
list_2 = get_list('Введите количество элементов второго списка: ', 1, 20)
print(f'list_1: {list_1}')
print(f'list_2: {list_2}')
set_1 = set(list_1)
set_2 = set(list_2)
arr = list(set(set_1 & set_2))
arr.sort()
print(*arr, sep=', ')
"""
Задача 24:
В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке,
причем кусты высажены только по окружности. Таким образом, у каждого куста есть
ровно два соседних. Всего на грядке растет N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло
различное число ягод – на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники.
Эта система состоит из управляющего модуля и нескольких собирающих модулей.
Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может
собрать за один заход собирающий модуль, находясь перед некоторым кустом
заданной во входном файле грядки.
"""


def get_number(string):
    global number
    try:
        number = int(input(string))
    except ValueError:
        print('Введено не число')
        get_number(string)
    return number


number_of_bushes = get_number("Введите количество кустов: ")
array = []
for i in range(number_of_bushes):
    array.append(get_number(f'Введите количество ягод на {i + 1} кусте: '))
count = []
if number_of_bushes <= 3:
    for i in range(number_of_bushes):
        count.append(array[i])
else:
    for i in range(len(array)):
        count.append(array[i - 2] + array[i - 1] + array[i])
if number_of_bushes <= 3:
    print(f'Максимальное количество ягод - {sum(count)}')
else:
    print(f'Максимальное количество ягод - {max(count)}')
