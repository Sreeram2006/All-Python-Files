print("Welcome to our restaurant")
x = input("What do you want to order?")
dd = {"Idly": 300, "Dosa": 200, "Noodles": 400}
if x in dd:
    bill = "Idly" + "Dosa" + "Noodles"
    print("Your bill is [bill] rs")
