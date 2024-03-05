# 1.3
num = input()
text = ["Тысячи -", "Сотни -", "Десятки -", "Единицы -"]

for i in range(4):
    print(text[i], num[i])

# 1.4

a = int(input())
b = int(input())
print(f"Квадрат суммы {a} и {b} равен {(a + b)**2}")
print(f"Сумма квадратов {a} и {b} равна {a**2 + b**2}")

