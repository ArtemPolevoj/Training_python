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
        array.append(random.randint(fist_number,last_number))
    return array

list_1 = get_list('Введите количество элементов первого списка: ', 1 , 20)
list_2 = get_list('Введите количество элементов второго списка: ', 1 , 20)
print(f'list_1: {list_1}')
print(f'list_2: {list_2}')
set_1 = set(list_1)
set_2 = set(list_2)
arr = list(set(set_1 & set_2))
arr.sort()
print(*arr, sep=', ')