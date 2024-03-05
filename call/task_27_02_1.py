list_person = ['hobby', 'work', 'study']


class Person:
    pass


id_1 = Person()
id_1.hh = "hello"
id_1.work = "AQA"
id_1.study = "RedRover"

for value in list_person:
    print(getattr(id_1, value, "No data"))
