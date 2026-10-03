# Simple Calculator: Build a CLI-based calculator that supports basic arithmetic operations 
# and handles invalid input gracefully. 
print("Simple Calculator")
try: 
    num1=float(input("Enter first number: "))
    num2=float(input("Enter second number: "))
    operator=input("Enter operator(+,-,*,/): ")

    if operator == '+':
        result=num1+num2
    elif operator == '-':
        result=num1-num2
    elif operator == '*':
        result=num1*num2
    elif operator == '/':
        result=num1/num2
    else:
        raise ValueError("Invalid Operator")
except ValueError as e:
    print("Error:",e)
except ZeroDivisionError:
    print("Cannot Divide by zero")
else:
    print("Result: ",result)
finally:
    print("Calculation completed")
