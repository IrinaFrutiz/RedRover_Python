"""
Предыстория:
Вася программирует и составляет родословную на компьютере.
Кондратий Палыч - это дедушка Маши, а Вася - это отец Маши.
Но что-то пошло не так и получилось, что Маша - это отец, а Вася - это дед. Исправьте пожалуйста код, чтобы было всё верно.
Задание:
Код уже написан, но с ошибками. Подумайте, что можно поменять чтобы семейный статус выводился верно.
В комментарии указано в какой области кода ошибка, внесите исправления именно там.
В итоге команда print(masha.status) и print(vasya.status), должны выводить слова Дочь и Отец на отдельных строках. Код с выводом на экран написан правильно, его исправлять не нужно.
Sample Input:
Sample Output:
"""


# Дочь
# Отец
class Kondraty_Palich:
    status = 'Деда'


class Vasya(Kondraty_Palich):
    status = 'Отец'


class Masha(Vasya):
    status = 'Дочь'


# подумайте что можно поменять вот здесь:
masha = Masha()
vasya = Vasya()

# эту часть кода не исправляйте:
print(masha.status, vasya.status, sep='\n')
