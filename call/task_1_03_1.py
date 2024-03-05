"""
Предыстория
Машенька хочет купить новый журнал с покемонами, но денег у неё нет. Журнал стоит дорого, и полную сумму никто не даст. Поэтому Машенька придумала план, попросить у каждого родственника по чуть-чуть. Она попросила у папы, мамы, деды и бабы по чуть-чуть, но вот незадача, считать то Машенька ещё не умеет. Помогите Машеньке реализовать её план.
Задание:
Создайте класс NewJournal.
Объявите два метода: set_attr() и check_money().
Метод set_attr():
- Имеет 4 параметра: papa, mama, deda, baba. Это значит set_attr(self, papa, mama...и т.д.).
- Создаёт атрибуты papa, mama, deda, baba, а значения этих атрибутов будут равны параметрам papa, mama, deda, baba, соответственно. Например self.papa = papa.
- Создаёт атрибут count_money равный сумме этих четырёх атрибутов: papa, mama, deda, baba.
Метод check_money():
- Проверяет, если атрибут count_money меньше 80, то выводит на экран: Денег не хватает
- Иначе выводит на экран: Ура, денег хватает!
Создайте экземпляр masha.
Вызовите метод set_attr() через экземпляр masha. В аргументах укажите 10, 20, 30, 40 - это наши значения для атрибутов: papa, mama, deda, baba.
Вызовите метод check_money()
Не забывайте про self и скобки при вызове методов.

"""


class NewJournal:

    def set_attr(self, papa, mama, deda, baba):
        self.papa = papa
        self.mama = mama
        self.deda = deda
        self.baba = baba
        self.money = papa + mama + deda + baba

    def check_money(self):
        print("Денег не хватает" if self.money < 80 else "Ура, денег хватает!")


masha = NewJournal()
masha.set_attr(10, 20, 30, 40)
masha.check_money()
