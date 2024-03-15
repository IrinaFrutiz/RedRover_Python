class Animal:

    def __init__(self, name, age):
        self.__types = None
        self.name = name
        self.age = age

    @property
    def types(self):
        return self.__types

    @types.setter
    def types(self, new_type):
        self.__types = new_type

    def speak(self):
        print(f"We don't know how {self.name} speak")


class Dog(Animal):

    def __init__(self, name, age):
        super().__init__(name, age)
        setattr(self, "types", "dog")

    def speak(self):
        print(f"{self.name} says woof-woof")


class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        setattr(self, "types", "cat")

    def speak(self):
        if self.age <= 1:
            print(f"{self.name} says mi-mi-mi")
        else:
            print(f"{self.name} says meow")


class Duck(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        setattr(self, "types", "duck")

    def speak(self):
        print(f"{self.name} says quack-quack")
