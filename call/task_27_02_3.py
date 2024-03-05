class Pokemon:
    pass


pokemons = Pokemon()
lst = ["pikachu", "scyther", "gyarados", "gengar"]

for pok in lst:
    setattr(pokemons, pok, "")

atr = ['lapras', 'pikachu', 'alakazam']
for value in atr:
    print(hasattr(pokemons, value))


print(pokemons.__dict__)
