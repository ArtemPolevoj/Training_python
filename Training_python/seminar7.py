"""
Задание 1.
Создать класс TrafficLight (светофор)
и определить у него один приватный атрибут color (цвет) и публичный метод
running (запуск).
В рамках метода running реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный)
составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение.
Для имитации "горения" каждого цвета испольщуйте ф-цию sleep модуля time
Переключение между режимами должно осуществляться только
в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""
from time import sleep


class TrafficLight:
    __color = ''

    def running(self):
        self.__color = "красный"
        print(self.__color)
        sleep(7)
        self.__color = "желтый"
        print(self.__color)
        sleep(2)
        self.__color = "зелёный"
        print(self.__color)
        sleep(5)


traffic_ligth = TrafficLight()
traffic_ligth.running()

"""
Задание 2.
Реализовать класс Road (дорога), в котором определить защищенные атрибуты:
length (длина в метрах), width (ширина в метрах).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Реализовать публичный метод расчета массы асфальта, необходимого для покрытия
всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв
метра дороги асфальтом, толщиной в 1 см * число м толщины полотна.
Массу и толщину сделать публичными атрибутами.
Проверить работу метода.
Например: 20м*5000м*25кг*0.05м = 125000 кг = 125 т
"""


class Road:
    _length = 0
    _width = 0

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def weight(self, height, width):
        return self._length * self._width * height * width


road = Road(20, 5000)
result = road.weight(25, 0.05)
print(f'{result / 1000} тонн')

"""
Задание 3.
Реализовать базовый класс Worker (работник),
в котором определить публичные атрибуты name, surname, position (должность),
и защищенный атрибут income (доход). Последний атрибут должен ссылаться
на словарь, содержащий элементы: оклад и премия, например,
{"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker. В классе Position
реализовать публичные методы
получения полного имени сотрудника (get_full_name) и дохода с учетом
премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position,
передать данные,
проверить значения атрибутов, вызвать методы экземпляров).
П.С. попытайтесь добить вывода информации о сотруднике также через
перегрузку str
str(self) - вызывается функциями str, print и format. Возвращает строковое
представление объекта.
"""


class Worker:
    name = ''
    surname = ''
    position = ''
    _income = {}


class Position(Worker):

    def __init__(self, wage, bonus):
        self._income["wage"] = wage
        self._income["bonus"] = bonus

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return sum(self._income.values())

    def __str__(self):
        return f'{self.name} {self.surname}, оклад = {self._income["wage"]},' \
               f' премия = {self._income["bonus"]}'


engineer = Position(5000, 1000)
engineer.name = "Василий"
engineer.surname = "Иванов"
print(engineer.get_full_name())
print(engineer.get_total_income())
print(engineer)

"""
Задание 4.
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
(метод init()), который должен принимать данные (список списков) для
формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенны
в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
31 22
37 43
51 86

3 5 32
2 4 6
-1 64 -8

3 5 8 3
8 3 7 1

Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в
привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения двух
объектов класса Matrix (двух матриц). Результатом сложения должна быть
новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент
первой строки первой матрицы складываем с первым элементом первой строки
второй матрицы и т.д.
"""


class Matrix:
    def __init__(self, data: list):
        self.data = data

    def __str__(self):
        temp = []
        for row in self.data:
            temp.append(' '.join([str(k) for k in row]))
        return '\n'.join(temp)

    def __add__(self, other):
        temp = []
        for i, row in enumerate(self.data):
            temp_list = list(map(lambda x, y: x + y, row, other.data[i]))
            temp.append(temp_list)
        return Matrix(temp)


lists_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
lists_2 = [[4, 5, 6], [7, 8, 9], [1, 2, 3]]

matrix_1 = Matrix(lists_1)
matrix_2 = Matrix(lists_2)
result_matrix = matrix_1 + matrix_2

print(matrix_1)
print()
print(matrix_2)
print()
print(result_matrix)

"""
Задача 34:
Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
Поскольку разобраться в его кричалках не настолько просто, насколько легко он
их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть,
если число слогов (т.е. число гласных букв) в каждой фразе
стихотворения одинаковое. Фраза может состоять из одного слова,
если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются
друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу
с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и
“Пам парам”, если с ритмом все не в порядке
*Пример:*
**Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
    **Вывод:** Парам пам-пам
"""


def rhythm(poem):
    temp = poem.split()
    array = []
    for phrase in temp:
        count = 0
        for i in phrase:
            if i in 'аеёиоуыэюя':
                count = count + 1
        array.append(count)
    return len(array) == array.count(array[0])


poem = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
if rhythm(poem):
    print('Парам пам-пам')
else:
    print('Пам парам')

"""
Задача 36:
Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру
строки и столбца. Аргументы num_rows и num_columns указывают число строк и
столбцов таблицы, которые должны быть распечатаны. Нумерация строк и столбцов
идет с единицы (подумайте, почему не с нуля). Примечание: бинарной операцией
называется любая операция, у которой ровно два аргумента, как, например,
у операции умножения.
*Пример:*
**Ввод:** `print_operation_table(lambda x, y: x * y) ` 
**Вывод:**
"""


def get_number(string):
    try:
        number = int(input(string))
    except ValueError:
        print('Введено не число')
        return get_number(string)
    return number


def print_operation_table(operation, count_rows, count_columns):
    arr = [[operation(i, j) for i in range(1, count_columns + 1)]
           for j in range(1, count_rows + 1)]
    for i in arr:
        print(*[f"{x:>3}" for x in i])


count_rows = get_number('Введите количество строк: ')
count_columns = get_number('Введите количество столбцов: ')
print_operation_table(lambda x, y: x * y, count_rows, count_columns)
