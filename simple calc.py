import termcolor
#A simple calculator that performs four mathematical operations, 
# which are addition, subtraction, multiplication and division, 
# according to the user's choice. It works on two numbers only, according to the user's choice.
termcolor.cprint("Hello", "green")
num_1 = float(input("Enter the first number:\t"))
arithmetic_operation = input("What arithmetic operation do you want?(Just write the sign):\t")
num_2 = float(input("Enter the second number:\t"))

def plus(x , y):
    return x + y

def minus(x , y):
    return x - y

def multiply(x , y):
    return x * y

def divide(x , y):
    return x / y

if arithmetic_operation == "+":
    print(plus(num_1 , num_2))

elif arithmetic_operation == "-":
    print(minus(num_1 , num_2))

elif arithmetic_operation == "*":
    print(multiply(num_1 , num_2))
    
elif arithmetic_operation == "/":
    print(divide(num_1 , num_2))