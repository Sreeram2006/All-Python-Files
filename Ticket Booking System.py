# -*- coding: utf-8 -*-
"""Ticket booking system .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1D0dhv8kMuhJ8upianJ3dxiLr7R70PkVx
"""



"""# Create a bus reservation system.
* The system should have the following feaures. Fares: 
1. Hyderabad-bangalore--400 rs; 
2. Delhi - Pune -- 700 rs
3. Hyderabad- Delhi -- 1000 rs
4. Chennai - Bangalore -- 900 rs etc

*  30% for tickets above 5
*  Children <10 free 
* Only one route bookable


---

**Steps to be followed :-**
* Ask the user to which route they want to travel  ---->   Only one route bookable at once

* Then ask the user how many seats/tickets they want to book
* Then type the details for each ticket/seat ----> like name, age, gender etc
* Then calculate the fare/total price according to the  no of tickets.
* Then Add different prices for adults & children, & Apply discounts i.e
    1. If tickets>5, apply 30% discount. 
    2. Children below 10 will travel free.



"""







no_of_tickets = int(input("Eneter no of tickets to be booked: "))
booking_details = []
#booking_details.fromkeys()

get_details = ["name", "age","gender"]
x = []  # to store each person/seat details in a list

print("\n")
for i in range(1,no_of_tickets+1):
  # x = []
  for d in range(len(get_details)):
    collect = input(f"enter the {get_details[d]} for booking seat no {i} :")
    x.append(collect)
  print("\n")
    
  booking_details.append(x)
  #print(booking_details)
  # x.clear()  ----> it will make clear in the 2 lists, x & booking details, so instead keep x= [] will cover  


print(booking_details)

# Full logic code
book = {"Hyd-Bag" : 1000, "Hyd-Vizag": 800, "hyd-Mub" : 1200}
while True :
  route = input("Enter the route: ")
  if route in book:

    no_of_tickets = int(input("Enetr nof of tickets to be booked: "))
    booking_details = []
    #booking_details.fromkeys()

    details = ["name", "age","gender"]
    print("\n \t\t please enter the details for booking Seats : \t\t \n".upper())

    for i in range(1,no_of_tickets+1):
      x = []  # to store each person/seat details in a list
      for d in range(len(details)):
        collect = input(f"Enter the {details[d]} for booking seat no {i} :")
        x.append(collect)
      print("\n")
      booking_details.append(x)
      # x.clear()  ----> it will make clear in the 2 lists, x & booking details, so instead keep x= [] will cover  
    
    # calculate the fare:
    print(f"The total fare for {no_of_tickets} tickets is {no_of_tickets*book.get(route)}")
    ask_pay = input("Go to payment : ")   # Proceed to Pay / click to payment
    if ask_pay == ["y", "yes", "Y", "YES", "ok", "OK"] :
      # Type the amount to be paid
      print("\n Successfully completed the transcation !!!!! \n")


  print(f"The details for booking {no_of_tickets} are:  ")
  s = 1
  for j in booking_details:
    print(f"Seat {s}  :  {j}")
    s= s+1
  ask = input("Do want to book any other tickets:")

  if ask.lower() == 'yes':   # or can write like this ask == ["y", "yes", "Y", "YES"]
    pass
  else:
    print("Thank you for visiting the site")
    break



x = []
y = [1,2,3]
x.append(y)
y = []
# y.clear()  ----> it will make clear the x value where ever it added 

print(x)



# using dictonaries for storing booking details 
book = {"Hyd-Bag" : 1000, "Hyd-Vizag": 800, "hyd-Mub" : 1200}
while True :
  route = input("Enter the route: ")
  if route in book:

    no_of_tickets = int(input("Enetr nof of tickets to be booked: "))
    booking_details = {}
    details = ["name", "age","gender"]
    print("\n \t\t please enter the details for booking Seats : \t\t \n".upper())

    for i in range(1,no_of_tickets+1):
      x = []  # to store each person/seat details in a list
      for d in range(len(details)):
        collect = input(f"Enter the {details[d]} for booking seat no {i} :")
        x.append(collect)
      print("\n")
      booking_details.fromkeys(x)
      print(booking_details)

no_of_tickets = int(input("Enetr nof of tickets to be booked: "))
booking_details = {}
details = ["name", "age","gender"]
print("\n \t\t please enter the details for booking Seats : \t\t \n".upper())
for i in range(1,no_of_tickets+1):
  x = []  # to store each person/seat details in a list
  for d in range(len(details)):
    collect = input(f"Enter the {details[d]} for booking seat no {i} :")
    x.append(collect)
  print("\n")
  booking_details.fromkeys(x)
  print(booking_details)

d = {}
x= ["name","age", "gender"]
#d = d.fromkeys(x)
name = input("Enter the name: ")
kage = input("Enter the age: ")
#gender = input("Enter the gender: ")
d.update(n = name, age = age )
d.setdefault((x[0]), name)  # possible with tuples to add as key name with list
#d.update({})

print(d)

x= ["name","age", "gender"]
y = (x[0], x[1])
print(y)

# bill printer
# we will assign for each item certain price using dictonary datatype
# we access the price of a particular item using get() method or x["key"] ----> so we get the value of the particular key
# we use if cond to check what item they have typed, & print the price
# & then calculate the total cost of the items he has bought

# Quiz
Create a bus ticketing system that gives discounts as per above problem and:
0% discount for 1 ticket
1% discount for 2 tickets
20% discount for 3 tickets
40% discount for 4 tickets



# bill printer

x= {"coffee": 500, "milk": 100, "soaps": 600, "veggies": 300, "pulses": 800 }

while True:
  items =



x= {"coffee": 500, "milk": 100, "soaps": 600, "veggies": 300, "pulses": 800 }
# total = []
total = 0
a= input()
print(x["coffee"] + x["veggies"] + x["milk"] )
print(x.get(a) + x.get("milk") + x.get("soaps"))
# x = x+1
print(type(x.get(a)))
total = total + x.get(a)
print(total)

routes = {"Hyd-Bangalore":1000, "Hyd-Chennai":1200, "Bangalore-Chennai":800,
          "Hyd-Delhi":2000, "Mumbai-Delhi":1500}
print("Hii User, Welcome to Ticket Booking system!!!")
print(routes)
print()
while True :
  ask_route = input("Please enter the your required route from above routes provided:  ")
  if ask_route in routes :
    print(f"The cost for single tickect for traviling {ask_route} is {routes.get(ask_route)}")
    ask2 = input("enter how many children age less than 10 are traviling:")
    no_of_tickets = int(input("please enter how many tickets you want to book : "))
     
    total = (routes.get(ask_route))*(no_of_tickets)

    # collecting details
    booking_details = {}

    details = ["name", "age","gender"]
    

    for i in range(1,no_of_tickets+1):
      x = []
      for j in details:
        ask1 = input(f"Enter the {j} for the seat{i} : ")
        x.append(ask1)
      booking_details.setdefault(f'seat{str(i)}', x)

    for  a in range(1,no_of_tickets+1):
      print(f" seat{a} : {booking_details.get(f'seat{str(a)}')}" )
    #print(booking_details)



    # payment
    print(f"the total fare/cost for {no_of_tickets} tickets for {ask_route} is {(routes.get(ask_route))*(no_of_tickets)}")  # calculating the fare
    payment = input("Do you like to proceed for payment & book tickets: ")
    if payment in ["yes", "y", "YES", "okk", "Y"] :
      #if age< 10 :

      if no_of_tickets >= 5:
        print("You received 30% off on ur tickets!!!")
        print(f"Your total fare after applying discount is {total - ((total * 30)/100) }")
      print("You transcation is successfully!!")
    else:
      pass
    
  else :
    print("You entered a invalid text \n or")
    print("the service for this route is not available")
  exit = input("Do you like to do any other booking / do changes in your booking: ")
  if exit.lower() == "yes" :
    pass
  else :
    break

"4"*5

(10000 * 30)/100