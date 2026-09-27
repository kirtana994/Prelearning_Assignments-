#Write a simple calculator that accepts two numbers and an operator (+, -, *, /) and prints the result. 
a=float(input("Enter first number:"))
operator=input("Enter operator((+, -, *, /): ")
b=float(input("Enter second number: "))
if operator == "+":
    print(f"Addition:{a+b}")
elif operator == "-":
    print(f"Subtraction:{a-b}")
elif operator == "*":
    print(f"Multiplication:{a*b}")
elif operator == "/":
    if b==0:
        print("Divide by 0 not possible")
    else:
        print(f"Division:{a/b}")
else:
    print("Invalid operator")