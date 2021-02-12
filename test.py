#Quiz on Lambda function:
#Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, also create a lambda function that multiplies argument x with argument y and print the result.
print(""" 1) Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument""")
print("""
This is the first question. 
Whatever input we give, fifteen is added to it. """)
ask= int(input("Please enter your number: "))
first= lambda first:first+15
print(first(ask))
print(""" 2) Create a lambda function that multiplies argument x with argument y and print the result.""")
print("""
This is the second question.
Whatever inputs we give, they will be multiplied""")
print("""
""")
again= int(input("Enter your number to multiply:"))
again1=int(input("Enter second number: "))
second= lambda second: again*again1
print(second(again))

#Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number.
print("""3) Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number.""")
print("In this question, we already have a secret number with us. \n In this case, it is 10.\n We will ask the user for an input.\n The output will give us the input number multiplied by 10")
number =10
ask2 = int(input("Please enter a number: "))
fourth= lambda fourth:ask2*number
print(fourth(ask2))

#Write a Python program to sort a list of tuples using Lambda.
x=(1,2,3)
a=1
b=3
temp=1
a=b
b=temp
#Incomplete

#Write a Python program to filter a list of integers using Lambda
print("4)Write a Python program to filter a list of integers using Lambda.\nHere, we will filter a list of integers using filter proeprty of Lambda function.")
numbers= [1,2,3,4,5]
even= list(filter(lambda x: x%2 ==0, numbers))
print(even)
odd= list(filter(lambda x: x%2 !=0, numbers))
print(odd)

#Write a Python program to square and cube every number in a given list of integers using Lambda
#square:
print("5) Write a Python program to square and cube every number in a given list of integers using Lambda.\n "
      
      "We will do this task using MAP property of LAMBDA function")
numbers1= [1,2,3,4,5,6,7,8,9,10]
square= list(map(lambda x: x**2, numbers1))
print(square)
#cube:
cube= list(map(lambda x: x**3, numbers1 ))
print(cube)


#Write a Python #Write a Python program to add two given lists using map and lambda.
print("6) Write a Python program to add two given lists using map and lambda.\n"
      "Here, we already have two lists.\n We use MAP property again to find the sum of two lists.")
list1= [23,44,50]
list2=[0,400,30]
output= map(lambda x,y: x+y, list1,list2)
print(list(output))

#Write a Python program to sort a list of tuples using Lambda.
b=(1,2,3,4,5,6,7,8,9,20,101)
# x=("Hello", "Python", "Alphabet")
g= lambda s: sorted()












