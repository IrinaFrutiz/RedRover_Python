"""
Предыстория:
У Васи день рождения, и три друга (Masha, Nikita, Lena) придут с подарком. Вася любит красный цвет.
Masha - подарит красную ручку ("pen", "red")
Nikita - подарит красную футболку ("t-shirt", "red")
Lena - подарит красный мяч ("ball", "red")
Задача:
Создайте класс BirthDay и объявите метод __init__. В параметрах __init__ укажите (self, present, color).
Метод __init__ создаёт два атрибута present и color, и присваивает им значения параметров present,
color соответственно. Объявите в методе создание этих атрибутов.
Создайте три экземпляра Masha, Nikita, Lena и создайте у них атрибуты present, color соответственно
 тем подаркам, которые они подарят. Например Masha подарит, present = "pen", color = "red".
Выведите на экран значения атрибутов у каждого экземпляра, согласно примеру ниже.
"""


class BirthDay:
    def __init__(self, present, color):
        self.present = present
        self.color = color


Masha = BirthDay("pen", "red")
Nikita = BirthDay("t-shirt", "red")
Lena = BirthDay("ball", "red")

print(f'Masha подарит, present = "{Masha.present}", color = "{Masha.color}"')
print(f'Nikita подарит, present = "{Nikita.present}", color = "{Nikita.color}"')
print(f'Lena подарит, present = "{Lena.present}", color = "{Lena.color}"')
