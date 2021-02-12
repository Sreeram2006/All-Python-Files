is_hot= False
is_cold= True
if is_hot:
    print("It's a hot day.")
    print("Drink plenty of water.")
elif is_cold:
    print("Its a cold day.")
    print("Wear warm clothes.")
else:
    print("Its a lovely day")

price= 1000000
z= True
if z:
    down_payment= 0.1* price
else:
    down_payment= 0.2* price
print(f"Down payment: ${down_payment}")

#logical operators in Python
#And condition in Python
has_high_income=True
has_good_credit=True
if has_high_income and has_good_credit:
    print("You are eligible for a loan.")

#Or condition in Python
#Same Example
has_high_income=True
has_good_credit=True
if has_high_income or  has_good_credit:
    print("You are eligible for a loan.")
#And: Both conditions should be true
#Or: At least one condition should be true

#Not condition: Reverses any boolean value given
has_high_income=True
has_good_credit=True
has_criminal_record=True
if has_high_income and not  has_criminal_record:
    print("You are eligible for a loan.")

#comparision operators
#Greater than:
temp =30
if temp > 30:
    print("It's a hot day today.")
else:
    print("It's not a hot day.")
#Greater than or equal to:
temp =30
if temp >= 30:
    print("It's a hot day today.")
else:
    print("It's not a hot day.")
#Less than:
temp =30
if temp < 30:
    print("It's a hot day today.")
else:
    print("It's not a hot day.")
#Less than or equal to:
temp =30
if temp <= 30:
    print("It's a hot day today.")
else:
    print("It's not a hot day.")
#Not equal to:
temp =30
if temp != 30:
    print("It's a hot day today.")
else:
    print("It's not a hot day.")

#Name conditions excercise:
name=input("What is your name: ")
if len(name)<3:
    print("Name must be more than 3 characters.")
elif len(name)>50:
    print("Name must be less than 50 characters.")
else:
    print("The name looks perfect.")

