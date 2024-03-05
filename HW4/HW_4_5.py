import time


def time_of_function(function):
    def wrapped(*args):
        start_time = time.time()
        res = function(*args)
        print("Время выполнения функции:", time.time() - start_time)
        return res

    return wrapped


@time_of_function
def func(first, second):
    time.sleep(1)
    return first ** second + second ** first // 12589


print(func(150, 985))
