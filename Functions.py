# -*- coding: utf-8 -*-
"""17.Functions_b2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YhYi5MgskAxyIaGWYndNvhff30jJIx73
"""

char()
print() 
int()
append() --> methods is a function

"""###Fuction: A function is a block of code which runs only when called.
### You can pass inputs to a function and get output from it too.

####Define a function:
Specify what must be done by the function when called in a program.

Syntax:
```
def FunctionName(Parameters):
  code
  code
  code
  return
```


####Calling a funtion:
Call a function when you need that function to be executed in the program.

Syntax:


```
FunctionName(Arguments)
```
* Parameters:The variables that are defined in the funtion.
* Arguments: The variables/values that are passed to the functions.


"""

def Greet():
  #print("Hello!")
  return "hello"
def PrintFullName(FirstName,LastName):
  FullName = FirstName +" " + LastName
  return FullName
Greet()
a = "John"
b = "Wesley"
c = PrintFullName('Joe','Biden')
d = PrintFullName(a,b)
print(c)
print(d)

#Nayonika
#Function to get info of a user
def Info(name,age,color):
  print(name,"is",age,"years old. Their Favourite color is",color)
a = input("what is your name? ")
b = input("What is your age? ")
c = input("What is your favourite color? ")
Info(a,b,c)

"""## Keyword Arguments
You can also send arguments with the key = value syntax.

This way the order of the arguments does not matter.

"""

#Example
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

"""## Arbitrary Arguments, *args
* If you do not know how many arguments that will be passed into your function, add a  *  before the parameter name in the function definition.

* This way the function will receive a tuple of arguments, and can access the items accordingly:

"""

#Example: If the number of arguments is unknown, add a * before the parameter name:

def my_function(*kids):

  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

def my_function(*kids):
  print(type(kids))
  for i in kids:
    print("The youngest child is " + i)

my_function("Emil", "Tobias", "Linus")

def sum(*n):
  sum = 0
  for i in n:
    sum = sum + i
    print(sum)

sum (1,2,3,4,5,6)

x = "hello"  # global   ---> variable can be accessed any where in the entire code
def name(**kid):
  global n 
  n = 2 # local variable  can be accessed only in that particular block
  print(type(kid))
  print(kid)
  print(n)
  for i in kid.keys() :
    print("My name is {}".format(kid[i]))


name(f = "lakshmi", l = "durga", m = 123)

print(n)

x = 3
if x> 2:
  n = 5
  print("yes")
else:
  print("no")

print(n)

for i in range(5):
  n= 7
  pass
print(n)

kid["f"]

"""## Arbitrary Keyword Arguments, **kwargs
* If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.

* This way the function will receive a dictionary of arguments, and can access the items accordingly:
"""

# Example: If the number of keyword arguments is unknown, add a double ** before the parameter name:

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

#Amishi
#Function to record marks of a student and calculate total and percentage
def ReportCard():
  Eng = int(input("What's your English score? "))
  Sci = int(input("What's your Sci score? "))
  Math = int(input("What's your Math score? "))
  print("Eng Marks:",Eng,"\nSci Marks:",Sci,"\nMath Marks:",Math)
  Total = sum([Eng,Sci,Math])
  print("Total Marks:",Total)
  Percentage = int(Total/30*100)
  print("Percentage:",Percentage,"%")
  if(Percentage>90):
    print("Great Job!")
  else:
    print("Do better!")
  return
ReportCard()
ReportCard()

#Zoha
#Function to check if a number is divisible by 6
List=[]
def IsDivisibleBy6(num):
  if num%2==0:
    if num%3==0:
      List.append(num)
  return
for i in range(1,61):
  IsDivisibleBy6(i)
print(List)

#Shaili
#Function to calculate average of the numbers of a list
def Average(listname):
  Sum=sum(listname)
  avg=Sum/len(listname)
  print(avg)
list1=[1,2,3,4,5,6]
Average(list1)



if 
for 
while  are not function

print()  ---> in built function
int()
input()
append()
# all the methods which ever we have in data types are functions



def sum(x,y):  # here parameters /arguments are x,y
  sum = x+y
  print(sum)
  return sum

a= int(input("enter a number"))
b= int(input("enter a number"))
sum(a,b) # calling a function with therequired  arguments(i.e a,b )

def greet():
  print("hello")
  return

greet()

while True:

  ask = input("Do you want to perform any other operation : ")
  #if ask == "yes" or ask == "Yes"
  if ask == "Yes" or "yes":
    1st cond or 2nd cond 
    pass
  else :
    print("Thank you")
    break

def sum():
  a = int(input("enter a number"))
  b = int(input("enter a number"))
  return a+b
  print(a+b)


while True :
  ask = input("enter a text: ")
    #if ask == "yes" or ask == "Yes" : 

  if ask in ["yes", "Yes", "y", "Y", "YES"] :     
    print("if is correct")
    sum()
    break
  else :
    print('else is working')
    break

"""Homework:
1. Write a function to return all the factors of a number.

2. Write a function to calculate the bill of a list of items purchased. The bill must also include a GST of 18%. Execute the function for 2 customers.
For example, John purchased the following items:
Eggs - 40 rupees, Cereals - 120 rupees, Honey - 150 rupees, Fruit Juice - 100 rupees,Sanitizer - 80 rupees
The bill must be as follows:
* Customer name - John
* Eggs - 40 rupees
* Cereals - 120 rupees
* Honey - 150 rupees
* Fruit Juice - 100 rupees
* Sanitizer - 80 rupees
* Total - 490 rupees
* GST Amount - 88.2 rupees
* Total including GST - 578.2 rupees

(You can make changes to make the output look like a proper bill)

3. Write a function to find the largest number among a given series of numbers.

4. Write a function to calculate the product of 'n' natural numbers where 'n' is user input.

5. Write a function to format user input which is Full Name. For example, if the user input is "joe biden". The function should change the string to "Joe Biden" and return it.
"""

factors of 12 ----> 3,2,4,6,12,1

factorial of 5! ==> 5! = 5*4*3*2*1

#You can call a function inside another function
#Function to check if a number is prime or not
def factors(n):
  ListOfFactors = []
  for i in range(1,n+1):
    if (n%i==0):
      ListOfFactors.append(i)
  return ListOfFactors
print(factors(166))

def factorial(n):
  factorial = 1
  for i in range(n,0, -1) : # backward numbers
    factorial = factorial * i
  print(factorial)
  return factorial

num = int(input("enter a number: "))
print(factorial(num))

* how many parameters r passe those all parameters should be given while calling the func
* its not cumplosory u should give same varible names or diffrent variable names

def IsPrime(n):
  NoOfFactors = len(factors(n))
  if(NoOfFactors>2):
    return False
  else:
    return True
    
print(IsPrime(4))
print(IsPrime(8))
print(IsPrime(5))

#Recursion: A function call within itself (or) A function calling itself
#Factorial
def Factorial(n):
  if(n==1):
    return n
  else:
    return n*Factorial(n-1)
print(Factorial(4))

"""###Homework:
Create a Virtual Restaurant that
* Asks Customer for his/her name.
* Shows them the various courses (Menu) available in a good format. Hint: Make use of escape characters.
* Calculates a bill including 18% GST and displays it to customer.
* Gives Customer various payment options and takes feedback.

(You can add extra features that you'd like to have)
"""





"""https://colab.research.google.com/drive/1VaMpV93hqGR1z32A_HT1uSfd0uBwMZx7?usp=sharing - recursive function

Global Variables
In Python, a variable declared outside of the function or in global scope is known as a global variable. This means that a global variable can be accessed inside or outside of the function.

Let's see an example of how a global variable is created in Python.
"""

x = "global"

def foo():
    print("x inside:", x)

foo()
print("x outside:", x)

In the above code, we created x as a global variable and defined a foo() to print the global variable x. Finally, we call the foo() which will print the value of x.

What if you want to change the value of x inside a function?

x = "global"

def foo():
    x = x * 2
    print(x)

foo()

"""The output shows an error because Python treats x as a local variable and x is also not defined inside foo().

To make this work, we use the global keyword. Visit Python Global Keyword to learn more.

## Local Variables
A variable declared inside the function's body or in the local scope is known as a local variable.
"""

# Example 2: Accessing local variable outside the scope
def foo():
    y = "local"
foo()
print(y)

# The output shows an error because we are trying to access a local variable y in a global scope 
# whereas the local variable only works inside foo() or local scope.



"""Example 3: Create a Local Variable
Normally, we declare a variable inside the function to create a local variable.


"""

def foo():
    y = "local"
    print(y)

foo()
# Let's take a look at the earlier problem where x was a global variable and we wanted to modify x inside foo().

"""## Global and local variables
Here, we will show how to use global variables and local variables in the same code.

"""

# Example 4: Using Global and Local variables in the same code
x = "global "

def foo():
    global x
    y = "local"
    x = x * 2
    print(x)
    print(y)

foo()

In the above code, we declare x as a global and y as a local variable in the foo(). 
Then, we use multiplication operator * to modify the global variable x and we print both x and y.

After calling the foo(), the value of x becomes global global because we used the x * 2 to print two times global.
After that, we print the value of local variable y i.e local.

# Example 5: Global variable and Local variable with same name
x = 5

def foo():
    x = 10
    print("local x:", x)


foo()
print("global x:", x)

In the above code, we used the same name x for both global variable and local variable.
 We get a different result when we print the same variable because the variable is declared in both scopes, i.e. 
 the local scope inside foo() and global scope outside foo().

When we print the variable inside foo() it outputs local x: 10. This is called the local scope of the variable.

Similarly, when we print the variable outside the foo(), it outputs global x: 5. This is called the global scope of the variable.

"""# Nonlocal Variables
Nonlocal variables are used in nested functions whose local scope is not defined. This means that the variable can be neither in the local nor the global scope.

Let's see an example of how a nonlocal variable is used in Python.

We use nonlocal keywords to create nonlocal variables.
"""

# Example 6: Create a nonlocal variable
def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    inner()
    print("outer:", x)


outer()

In the above code, there is a nested inner() function. We use nonlocal keywords to create a nonlocal variable. 
The inner() function is defined in the scope of another function outer().

Note : If we change the value of a nonlocal variable, the changes appear in the local variable.