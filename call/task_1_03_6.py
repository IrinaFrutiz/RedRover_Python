"""
Предыстория:
Вася узнал про __dict__ по телевизору, когда смотрел передачу "В мире python".
Решил попробовать вывести __dict__ экземпляра, но пока не понял как. Помогите Васе вывести информацию о __dict__.
Задание:
Часть кода уже написана.
Выведите на экран __dict__ экземпляра my с помощью print.
7:32
Вася научился с помощью __dict__ быстро добавлять группы людей в своей соцсети Person.
 Теперь ему нужно быстрым способом увидеть список всех друзей, нажав на одну кнопку. Пока он думает использовать цикл и __dict__.
Задание:
Часть кода уже написана.
Выведите на экран, значения всех атрибутов экземпляра person1. Каждое значение должно быть на отдельной строчке. Можете сделать простым способом, а можете попробовать через цикл, в любом случае используйте __dict__.

"""


class Person:
    pass


person_1 = Person()
person_1.__dict__ = {'name': 'Vasya', 'age': '20', 'work': 'driver'}

print(*person_1.__dict__.values(), sep="\n")