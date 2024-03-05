"""
Предыстория:
Вася создаёт программу для водителей. В ней вы указываете расстояние, которое планируете проехать, расход топлива на 100км вашей машины, цену на бензин в вашем регионе. Программа выводит на экран информацию о будущих финансовых расходах. Вася вероломно использует статический метод для подсчёта.
Задание:
Создайте класс Driver
Объявите статический метод calculate_fuel_costs() с параметрами (distance, fuel, price). Напоминашка: @staticmethod.
- Создайте переменную result, в ней будет хранится результат подсчётов.
- Готовая формула подсчётов будет в комментариях.
- Выведите на экран округлённое значение result, используя функцию round(). Значение округлите до сотых. Постарайтесь сделать округление имено с round(), иначе ответы могут не совпасть.
Оставшаяся часть кода уже написана, вам нужно сделать то, что указано в задании.
result = price * (fuel / 100) * distance
"""


class Driver:
    @staticmethod
    def calculate_fuel_costs(distance, fuel, price):
        result = price * (fuel / 100) * distance
        print(round(result, 2))


vasya = Driver()
Driver.calculate_fuel_costs(3, 1.3, 50)
vasya.calculate_fuel_costs(100, 7, 50)
vasya.calculate_fuel_costs(50, 7, 50)


class A(Driver):
    @staticmethod
    def calculate_fuel_costs(t, l, m):
        return t*l*m
