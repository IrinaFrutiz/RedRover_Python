class Person:
    pass


id_1 = Person()
setattr(id_1, "name", "Vasya")
setattr(Person, "name", "Vasya")
setattr(id_1, "name", "Masha")

print(Person.name)
print(id_1.name)
