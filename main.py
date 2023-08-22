def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def divide(a, b):
    return a / b
def multiply(a, b):
    return a * b

while True:
    print("--CALCULATOR--")
    op = input("Enter operator (+,-,/,*): ")
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    
    try:
    	if op == "+":
        	print("Result: " + str(add(num1, num2)))
    	elif op == "-":
        	print("Result: " + str(subtract(num1, num2)))
    	elif op == "/":
        	print("Result: " + str(divide(num1, num2)))
    	elif op == "*":
        	print("Result: " + str(multiply(num1, num2)))
    	else:
        	print(op + " is not a valid operator.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")
        
    finally:
    	restart = input("Restart the program? [y]/[n]: ")


        if restart == "n":
        exit()