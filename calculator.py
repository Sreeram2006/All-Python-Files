num1 = int(input("Enter your first number: "))
num2 = int(input("Enter you second number: "))
op = input("Enter your arithmetic operator: ")

elif op== "-":
    if op == "+":
        print(num1
        print(num1-num2)
elif op== "*":
    print(num1*num2)
elif op== "/":
    print(num1/num2)
elif op.lower()== "help":
    print("""
    Enter "+" symbol for addition
    Enter "-" symbol for subtraction
     Enter "*" symbol for multiplication
      Enter "/" symbol for division
    
    """)
else:
    print("Invalid operator")
    print("Operator not recognized")
ask= input("Do you want to make any more arithmetic operations: ")
if ask.lower()== "yes":
    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter you second number: "))
    op = input("Enter your arithmetic operator: ")
    if op == "+":
        print(num1 + num2)
    elif op == "-":
        print(num1 - num2)
    elif op == "*":
        print(num1 * num2)
    elif op == "/":
        print(num1 / num2)
    elif op.lower() == "help":
        print("""
        Enter "+" symbol for addition
        Enter "-" symbol for subtraction
         Enter "*" symbol for multiplication
          Enter "/" symbol for division

        """)
    else:
        print("Invalid operator")
        print("Operator not recognized")
    if ask.lower()== "no":
        print("Calculation process has ended.")


