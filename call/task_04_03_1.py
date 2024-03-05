"""
Создайте класс Homer.
Создайте в классе Homer метод __init__(self, name), который создает атрибут name.
Создайте пустой класс Daughter и сделайте его дочерним классом для Homer. Используйте pass для пустого класса.
Создайте экземпляр daughter1 для класса Daughter и присвойте атрибуту name значение Lisa.
Выведите на экран значение атрибута name через экземпляр daughter1.
"""


class Homer:
    def __init__(self, name):
        self.name = name


class Daughter(Homer):
    pass


daughter1 = Daughter('Lisa')
print(daughter1.name)
