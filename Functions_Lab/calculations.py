def calculate(operator, num1, num2):
    if operator == "multiply":
        return num1 * num2
    elif operator == "divide":
        return num1 // num2   # integer division
    elif operator == "add":
        return num1 + num2
    elif operator == "subtract":
        return num1 - num2


# input comes from three separate lines
operator = input()
num1 = int(input())
num2 = int(input())

# output the result
print(calculate(operator, num1, num2))
