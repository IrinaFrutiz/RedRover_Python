def square(side):
    return side * 4, side ** 2, side * (2 ** 0.5)


print(*square(5))
