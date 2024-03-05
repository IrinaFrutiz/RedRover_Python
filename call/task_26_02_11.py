class Person:
    setup = ['set_name', 'set_age', 'set_work', 'set_study']


id_1 = Person()
for el in Person.setup:
    setattr(id_1, el, input(f"{el} : "))

for value in id_1.setup:
    print(getattr(id_1, value))
