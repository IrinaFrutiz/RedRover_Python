"""
Предыстория:
Вася тренируется в программировании GPS навигации.
Он учится ставить точку на 2D карте используя создание экземпляров с координатами x и y.
Задание:
Создайте класс Coordinate и объявите в нём метод __init__.
Метод __init__ будет создавать два атрибута x и y со значениями, которые вы укажите при создании экземпляра. Не забывайте указывать self.
Создайте экземпляр coord и укажите координаты при создании в скобках, чтобы x и y стали равными 100 и 200 соответственно.
Выведите на экран значения x и y в одну строку через пробел.
"""


class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y


coord = Coordinate(100, 200)
print(coord.x, coord.y)