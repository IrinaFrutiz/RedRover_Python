class Animal:

    def __init__(self, name, age):
        self.name = name
        self.__type = type
        self.age = age

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, new_type):
        self.__type = new_type

    def speak(self):
        print(f"We don't know how {self.name} speak")


class Dog(Animal):

    def __init__(self, name, age):
        super().__init__(name, age)
        setattr(self, "type", "dog")

    def speak(self):
        print(f"{self.name} says woof-woof")


class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.type("cat")

    def speak(self):
        if self.age <= 1:
            print(f"{self.name} says mi-mi-mi")
        else:
            print(f"{self.name} says meow")


class Duck(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.type("duck")

    def speak(self):
        print(f"{self.name} says quack-quack")
