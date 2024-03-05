class Animal:

    def __init__(self, name, age):
        self.name = name
        self.__type = type
        self.age = age

    def get_type(self):
        return self.__type

    def set_type(self, new_type):
        self.__type = new_type

    def speak(self):
        match(self.get_type()):
            case "duck":
                print(f"{self.name} says quack-quack")
            case _:
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
        self.set_type("cat")

    def speak(self):
        if self.age <= 1:
            print(f"{self.name} says mi-mi-mi")
        else:
            print(f"{self.name} says meow")
