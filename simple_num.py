
for i in range(1, 100):
    flag = True
    for j in range(2, i//2 + 1):
        if i % j == 0:
            flag = False
            continue
    if flag:
        print(i, end=" ")
