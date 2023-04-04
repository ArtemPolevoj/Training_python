"""
1. Задание на закрепление знаний по модулю CSV. Написать скрипт,
осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt,
info_3.txt и формирующий новый «отчетный» файл в формате CSV.

Для этого:

Создать функцию get_data(), в которой в цикле осуществляется перебор файлов
с данными, их открытие и считывание данных. В этой функции из считанных данных
необходимо с помощью регулярных выражений извлечь значения параметров
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения каждого параметра поместить в соответствующий список. Должно
получиться четыре списка — например, os_prod_list, os_name_list,
os_code_list, os_type_list. В этой же функции создать главный список
для хранения данных отчета — например, main_data — и поместить в него
названия столбцов отчета в виде списка: «Изготовитель системы»,
«Название ОС», «Код продукта», «Тип системы». Значения для этих
столбцов также оформить в виде списка и поместить в файл main_data
(также для каждого файла);

Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
В этой функции реализовать получение данных через вызов функции get_data(),
а также сохранение подготовленных данных в соответствующий CSV-файл;

Пример того, что должно получиться:

Изготовитель системы,Название ОС,Код продукта,Тип системы

1,LENOVO,Windows 7,00971-OEM-1982661-00231,x64-based

2,ACER,Windows 10,00971-OEM-1982661-00231,x64-based

3,DELL,Windows 8.1,00971-OEM-1982661-00231,x86-based

Обязательно проверьте, что у вас получается примерно то же самое.

ПРОШУ ВАС НЕ УДАЛЯТЬ СЛУЖЕБНЫЕ ФАЙЛЫ TXT И ИТОГОВЫЙ ФАЙЛ CSV!!!
"""

# os_prod_reg = re.compile(r'Изготовитель системы:\s*\S*')
# os_prod_list.append(os_prod_reg.findall(data)[0].split()[2])
import re
import csv


def get_data():
    prod = re.compile(r'Изготовитель системы:\s*\S*')
    name = re.compile(r'Windows \s*\S*')
    code = re.compile(r'Код продукта:\s*\S*')
    type_OS = re.compile(r'Тип системы:\s*\S*')
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    main_data = [
        ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы'],
        [], [], []]
    list_file = ['info_1.txt', 'info_2.txt', 'info_3.txt']
    for path in list_file:
        with open(path) as file:
            file.tell()
            text = file.read()
            os_prod_list.append(prod.findall(text)[0].split()[2])
            os_name_list.append(name.findall(text)[0])
            os_code_list.append(code.findall(text)[0].split()[2])
            os_type_list.append(type_OS.findall(text)[0].split()[2])
            main_data[list_file.index(path) + 1].append(str(list_file.index(path) + 1))
            main_data[list_file.index(path) + 1].append(os_prod_list[list_file.index(path)])
            main_data[list_file.index(path) + 1].append(os_name_list[list_file.index(path)])
            main_data[list_file.index(path) + 1].append(os_code_list[list_file.index(path)])
            main_data[list_file.index(path) + 1].append(os_type_list[list_file.index(path)])
    return main_data


def write_to_csv(file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        wrtie_csv = csv.writer(file)
        data = get_data()
        for i in data:
            wrtie_csv.writerow(i)


write_to_csv('test.csv')
