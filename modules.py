# -*- coding: utf-8 -*-
"""Modules.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iKCg2kjcCSKBpUKY9yxskOpRz6Ub9wHA

# Modules

## What is a Module?
Consider a module to be the same as a code library.

A file containing a set of functions you want to include in your application.
"""

examples of modules :

1) random
2) numpy
3) cmaths
4) datetime
etc

"""### Create a Module
To create a module just save the code you want in a file with the file extension .py:

"""

# Example:
def greeting(name):   # Save this code in a file named mymodule.py
  print("Hello, " + name)

"""### Use a Module
Now we can use the module we just created, by using the import statement:

"""

#Example

import mymodule

mymodule.greeting("Jonathan")  # Import the module named mymodule, and call the greeting function:



"""Using the dir() Function
There is a built-in function to list all the function names (or variable names) in a module. The dir() function:

"""

# Example: List all the defined names belonging to the platform module:

import platform

x = dir(platform)
print(x)



Random Number
Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:

Example
Import the random module, and display a random number between 1 and 9:

import random

print(random.randrange(1, 10))

import platform

x = dir(platform)
print(x)

import numpy

x = dir(numpy)

print(x, )

import

import datetime

x = dir(datetime)
print(x)
type(x)



# story line 
import random

when = ['A few years ago', 'Yesterday', 'Last night', 'A long time ago']
who = ['a rabbit', 'an elephant', 'a mouse', 'a turtle']
name = ['Ali', 'Miriam', 'Hoouk', 'Starwalker']
residence = ['Barcelona', 'Germany', 'Venice', 'England']
went = ['cinema', 'university', 'school', 'laundry']
happened = ['made a lot of friends', 'found a secret key', 'solved a mistery', 'wrote a book']

print( random.choice(when) + ', ' + random.choice(who) + ' that lived in ' + random.choice(residence) + ', went to the ' + random.choice(went) + ' and ' + random.choice(happened))

"""https://colab.research.google.com/drive/1doVKryDCRXCEIl_lfTV46ZvSlIe5sxGG?usp=sharing - anonymous functions 

"""