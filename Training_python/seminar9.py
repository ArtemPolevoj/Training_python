"""
1) реализовать дескрипторы для любых двух классов
"""
from time import sleep


class NonString:
    def __set__(self, instance, value):
        try:
            int(value)
        except ValueError:
            raise ValueError("Не может строкой")
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class Road:
    height = NonString()
    weight_1m = NonString()

    def __init__(self, length, width, height=25, weight_1m=0.05):
        self._length = length
        self._width = width
        self.height = height
        self.weight_1m = weight_1m

    def weight(self):
        return self._length * self._width * self.height * self.weight_1m


road = Road(20, 5000)
result = road.weight()
print(f'{result / 1000} тонн')


class NonNull:
    def __set__(self, instance, value):
        if value == '':
            raise ValueError("Не введено значение")
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class Worker:
    name = NonNull()
    surname = NonNull()

    def __init__(self, name, surname, wage, bonus):
        self.name = name
        self.surname = surname
        self.wage = wage
        self.bonus = bonus

    def __str__(self):
        return f'{self.name} {self.surname}, оклад = {self.wage},' \
               f' премия = {self.bonus}'


worker = Worker('Петр', 'Иванов', 1000, 100)
print(worker)

"""
2) реализовать метакласс. позволяющий создавать всегда
один и тот же объект класса
"""


class Meta_traff(type):
    TrafficLight = None

    def __call__(cls):
        if cls.TrafficLight is None:
            cls.TrafficLight = super().__call__()
            return cls.TrafficLight
        else:
            return cls.TrafficLight


class TrafficLight(metaclass=Meta_traff):
    __color = {"красный": 7, "желтый": 2, "зелёный": 8}

    def running(self):
        print("красный")
        sleep(self.__color["красный"])
        print("желтый")
        sleep(self.__color["желтый"])
        print("зелёный")
        sleep(self.__color["зелёный"])


traffic_ligth = TrafficLight()
traffic_ligth1 = TrafficLight()
traffic_ligth2 = TrafficLight()

print(traffic_ligth is traffic_ligth1)
print(traffic_ligth1 is traffic_ligth2)
print(traffic_ligth2 is traffic_ligth)

