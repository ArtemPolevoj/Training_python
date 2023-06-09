"""
Задание 3.

Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе с помощью маркировки b'' (без encode decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
--- обязательно!!! усложните задачу, "отловив" исключение,
придумайте как это сделать
"""
list_str = ['attribute', 'класс', 'функция', 'type']
for s in list_str:
    temp = bytes(s, 'UTF-8')
    try:
        if len(s) != len(temp):
            raise ValueError
    except ValueError:
        print(f'"{s}" не возможно записать байтовом формате'
                             ' с помощью маркировки b\'\'.')
    else:
        print(f'"{s}", в байтовом формате - {temp}.')
