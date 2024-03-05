def calculator(num1, num2, operator):
    if operator == "+":
        print(text, num2+num1)
    elif operator == "-":
        print(text, num1-num2)
    elif operator == "*":
        print(text, num1*num2)
    elif operator == "/":
        if num2 == 0:
            print("we can't division to zero")
        else:
            print(text, num1/num2)
    else:
        print("Can't find your operator in my calculator")


num1 = int(input("First number is "))
num2 = int(input("Second number is "))
operator = input("Operator is ")
text = f"{num1} {operator} {num2} ="
calculator(num1, num2, operator)
