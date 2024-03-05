"""
Задание:
Создайте три класса King, Queen, Prince. Класс Prince наследуется от (King, Queen).
В классе King создайте атрибут "a" равный 4. В классе Queen создайте атрибут "b" равный 6. В классе Prince создайте атрибут "c" равный 10.
Создайте экземпляр count от класса Prince.
Выведите на экран результат сложения атрибутов "a" и "b" и "c", через экземпляр count (т.е. count.a + ...)
"""


class King:
    a = 4


class Queen:
    b = 6


class Prince(King, Queen):
    c = 10


count = Prince()
print(count.a + count.b + count.c)
