dic = {"title": "some title",
       "director": "I",
       "year": 2010,
       "budget": 100500,
       "main_actor": "me",
       "slogan": "the best film ever"}


# for key in dic.keys():
#     print(key)
print(*dic.keys(), sep=", ")

# for value in dic.values():
#     print(value)
print(*dic.values(), sep=", ")

for key, value in dic.items():
    print(f"{key} - {value}")
