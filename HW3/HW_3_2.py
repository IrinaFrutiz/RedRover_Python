list_1 = ['Hi', 'ananas', 2, 75, 'pizza', 36, 100]
summ = 0
for el in list_1:
    if isinstance(el, str) and "a" in el:
        print(el)
    if isinstance(el, int):
        summ += el
print(summ)
