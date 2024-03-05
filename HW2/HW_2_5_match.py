def calculator(num1, num2, operator):
    match operator:
        case "+":
            print(text, num2 + num1)
        case "-":
            print(text, num1 - num2)
        case "*":
            print(text, num1 * num2)
        case "/":
            print("we can't division to zero") if num2 == 0 else print(text, num1/num2)
        case _:
            print("Can't find your operator in my calculator")


num1 = int(input("First number is "))
num2 = int(input("Second number is "))
operator = input("Operator is ")
text = f"{num1} {operator} {num2} ="
calculator(num1, num2, operator)
