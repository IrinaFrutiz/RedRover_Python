from HW5.Animal import *

animal_1 = Animal("Пушок", 2)
animal_1.speak()

dog_1 = Dog("Pit", 3)
dog_1.speak()

cat_1 = Cat("Kitty", 1)
print(cat_1.get_type())
cat_1.speak()
cat_1.age = 2
cat_1.speak()


donald = Animal("Donald", 100)
donald.set_type("duck")
donald.speak()
