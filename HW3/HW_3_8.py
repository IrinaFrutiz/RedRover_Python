set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
set_set = {i for i in range(100)}

print(set1.intersection(set2))

print(set_set.difference(set1 | set2))

print(set1.issubset(set2))
print(set2.issubset(set1))
