from HW4 import HW_4_5


@HW_4_5.time_of_function
def plus(first, second):
    return first + second


@HW_4_5.time_of_function
def minus(first, second):
    return first - second


@HW_4_5.time_of_function
def multiplication(first, second):
    return first * second


@HW_4_5.time_of_function
def division(first, second):
    return first / second


print(plus(2, 15))
print(minus(6, 158))
print(multiplication(26, 187))
print(division(545175767717, 545454))
