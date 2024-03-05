"""
Задание:
Создайте класс CountDistance и объявите внутри него два метода: __init__() и dist_count().
Метод __init__(self, x, y) создаёт атрибуты "x", "y" с соответствующими значениями.
Метод dist_count(start, finish) будет статическим (@staticmethod). Метод будет принимать экземпляры, т.е. start - это
экземпляр с данными x,y координат старта, а finish - это экземпляр с данными x,y координат конечной точки.
Внутри метода создайте переменную dist = ((finish.x - start.x) ** 2 + (finish.y - start.y) ** 2) ** 0.5 - формула подсчитывает расстояние между точками. В итоге, метод выводит на экран округлённый результат round(dist) с помощью print.
Создайте пустой класс Point (используя pass). Класс Point наследуется от класса CountDistance.
Создайте экземпляр p1 класса Point, и присвойте во время создания атрибутам "x" и "y" - значения 10 и 20 соответственно.
Создайте экземпляр p2 класса Point, и присвойте во время создания атрибутам "x" и "y" - значения 20 и 30 соответственно.
Вызовите метод dist_count через класс CountDistance, в аргументах укажите (p1, p2). Функцию print использовать здесь не нужно.
Данная команда подсчитает расстояние между точками p1, p2.
"""


class CountDistance:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def dist_count(start, finish):
        print(round(((finish.x - start.x) ** 2 + (finish.y - start.y) ** 2) ** 0.5))


class Point(CountDistance):
    pass


p1 = Point(10, 20)
p2 = Point(20, 30)
CountDistance.dist_count(p1, p2)
