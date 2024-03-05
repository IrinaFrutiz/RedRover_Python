def arguments(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


arguments(name="John", last_name="Smith", age=35, position="web developer", abcd="Abracadabra")
arguments(name=None)
arguments()
