class Holiday:
    pass


friends = Holiday()
friends.name1 = "Sveta"
friends.name2 = "Katya"
friends.name3 = "Lena"
friends.name4 = "Natasha"
friends.name5 = "Leonardo DiCaprio"
friends.name5 = "Ira"


for i in friends.__dict__:
    if i != 'name5':
        print(getattr(friends, i))
    elif i == 'name5' and getattr(friends, i) == 'Leonardo DiCaprio':
        raise AttributeError('Машенька хочет увидеть вас на ДР')
