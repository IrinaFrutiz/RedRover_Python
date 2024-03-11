"""Предыстория:
Машенька мечтала, чтобы все люди были красивыми и придумала трансформатор красоты. В трансформаторе присутствует
искусственный интеллект. Человек указывает свой рост и вес, а искусственный интеллект делает волшебные вычисления,
 производя деление роста на вес. Но есть побочный эффект, если человек забудет указать свой вес, искусственный интеллект
  делит рост на ноль, и тело в этот момент может приобрести лицо, как в картине "Крик" Эдварда Мунка.
Задание:
Создайте класс BeautyTransform и два метода: __init__, transformer.
Метод __init__ имеет два параметра: height и weight=0, и создаёт два атрибута height и weight с этими же значениями.
Параметр weight=0 - это параметр по умолчанию, равный нулю.
Метод transformer(self) содержит внутри конструкцию try-except.
В блоке try происходит две операции:
- Создаётся атрибут new_body равный делению self.height / self.weight
- Выводится на экран сообщение: Успешная трансформация с помощью print.
Блок except проверяет код на ошибку ZeroDivisionError, и если она обнаружится, выводит на экран текст:
Лицо как в картине Крик, Эдварда Мунка
Часть кода уже написана, вам нужно лишь сделать то, что написано выше.
Sample Input:"""


class BeautyTransform:
    def __init__(self, height, weight=0):
        self.new_body = None
        self.height = height
        self.weight = weight

    def transformer(self):
        try:
            self.new_body = self.height / self.weight
            print("Успешная трансформация")
        except ZeroDivisionError:
            print("Лицо как в картине Крик, Эдварда Мунка")


vasya = BeautyTransform(172, 70)
nastya = BeautyTransform(100, 50)
lena = BeautyTransform(50)

vasya.transformer()
nastya.transformer()
lena.transformer()
