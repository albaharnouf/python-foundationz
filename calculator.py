number = input("Enter the first number")

if not number.isdigit():
    print("The number is invalid")
    number = input("Enter the first number")

number2 = input("Enter the second number")
if not number2.isdigit():
    print("The number is invalid")
    number2 = input("Enter the second number")

operation = input("Enter the operation (+, -, /,*)")
if operation == "+":
    answer = int(number)+ int(number2)
elif operation == "-":
    answer = int(number)- int(number2)
elif operation == "/":
    answer = float(number)/ float(number2)
elif operation == "*":
    answer = int(number)* int(number2)
else:
    print("Wrong input")
    operation = input("Enter the operation (+, -, /,*)")

print("The answer is %d" %answer)

