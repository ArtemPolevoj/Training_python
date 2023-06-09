"""
Задача 16: Требуется вычислить, сколько раз встречается некоторое
число X в массиве A[1..N]. Пользователь в первой строке вводит
натуральное число N – количество элементов в массиве. В последующих
строках записаны N целых чисел Ai.
Последняя строка содержит число X
5
1 2 3 4 5
3
-> 1
"""
import random

# array_list = []
# count = 0
# list_length = int(input("Введите количество элементов массива: "))
# number = int(input('Введите искомое число: '))
# for i in range(list_length):
#     array_list.append(random.randint(1, 15))
#     if array_list[i] == number:
#         count = count + 1
# print(list_length)
# print(array_list)
# print(number)
# print(f'-> {count}')

"""
Задача 18: Требуется найти в массиве A[1..N] самый близкий по
величине элемент к заданному числу X. Пользователь в первой строке
вводит натуральное число N – количество элементов в массиве. В
последующих строках записаны N целых чисел Ai.
Последняя строка содержит число X
5
1 2 3 4 5
6
-> 5
"""
array_list = []
element = None
list_length = int(input("Введите количество элементов массива: "))
number = int(input('Введите искомое число: '))
for i in range(list_length):
    array_list.append(random.randint(1, 15))
    if i == 0:
        temp_min = abs(number - array_list[0])
    if abs(number - array_list[i]) <= temp_min:
        temp_min = abs(number - array_list[i])
        element = array_list[i]
print(list_length)
print(array_list)
print(number)
print(f'-> {element}')
"""
Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
ценность. В случае с английским алфавитом очки распределяются так:
● A, E, I, O, U, L, N, S, T, R – 1 очко;
● D, G – 2 очка;
● B, C, M, P – 3 очка;
● F, H, V, W, Y – 4 очка;
● K – 5 очков;
● J, X – 8 очков;
● Q, Z – 10 очков.
А русские буквы оцениваются так:
● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
● Д, К, Л, М, П, У – 2 очка;
● Б, Г, Ё, Ь, Я – 3 очка;
● Й, Ы – 4 очка;
● Ж, З, Х, Ц, Ч – 5 очков;
● Ш, Э, Ю – 8 очков;
● Ф, Щ, Ъ – 10 очков.
Напишите программу, которая вычисляет стоимость введенного пользователем слова.
Будем считать, что на вход подается только одно слово, которое содержит либо только
английские, либо только русские буквы.
Ввод:
ноутбук
Вывод:
12
"""
points = {1: 'AEIOULNSTR''АВЕИНОРСТ',
          2: 'DG''ДКЛМПУ',
          3: 'BCMP''БГЁЬЯ',
          4: 'FHVWY''ЙЫ',
          5: 'K''ЖЗХЦЧ',
          8: 'JZ''ШЭЮ',
          10: 'QZ''ФЩЪ'}
word = input('Введите слово: ').upper()
print(sum([k for i in word for k, v in points.items() if i in v]))
"""
1. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.
Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень
"""
time_year_list = ['зима', "весна", "лето", "осень"]
time_year_dist = {0: 'зима', 1: "весна", 2: "лето", 3: "осень"}
number_mounth = int(input("Введите номер месяца: "))
if 1 <= number_mounth <= 2 or number_mounth == 12:
    print(f'Результат через список: {time_year_list[0]}')
    print(f'Результат через словарь: {time_year_dist.get(0)}')
elif 3 <= number_mounth <= 5:
    print(f'Результат через список: {time_year_list[1]}')
    print(f'Результат через словарь: {time_year_dist.get(1)}')
elif 6 <= number_mounth <= 8:
    print(f'Результат через список: {time_year_list[2]}')
    print(f'Результат через словарь: {time_year_dist.get(2)}')
elif 9 <= number_mounth <= 11:
    print(f'Результат через список: {time_year_list[3]}')
    print(f'Результат через словарь: {time_year_dist.get(3)}')
else:
    print("Нет такого мясяца")
"""
2. Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль (try except).
Пример:
Введите первое число: 10
Введите второе число: 0
Вы что? Пытаетесь делить на 0!
Process finished with exit code 0
Пример:
Введите первое число: 10
Введите второе число: 10
1.0

Process finished with exit code 0
"""
def division(a, b):
    try:
        print(a / b)
    except ZeroDivisionError:
        print("Вы что? Пытаетесь делить на 0!")
    finally:
        print("Process finished with exit code 0")

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
division(a, b)
"""
3. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания,
 email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""
def human(name_lastname=None, year_of_birth=None,
          sity=None, email=None, tel=None):
    print(f'{name_lastname} {year_of_birth} года рождения,'
          f' проживает в городе {sity}, '
          f'email: {email}, телефон: {tel}')

human('Иван Иванов', '1846', 'Москва', 'jackie@gmail.com', '01005321456')
"""
4. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""
def my_func_sort(a,b,c):
    temp_list = [a, b, c]
    temp_list.sort()
    return temp_list[1] + temp_list[2]
def my_func(a, b, c):
    if a >= c and b >= c:
        return a + b
    elif a > b and a < c:
        return a + c
    else:
        return b + c

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))
amount = my_func(a, b, c)
amount_sort = my_func_sort(a,b,c)
print(f'Сумма наибольших чисел = {amount}')
print(f'Сумма наибольших чисел(сортировка) = {amount_sort}')
