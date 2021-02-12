# -*- coding: utf-8 -*-
"""Tuples& sets.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZqRyzVWn4LGwEY3MzGlKNCF7xi6xVGIW
"""

x = (1,3,"hello",4,8,5,"hii", 6.98, [1,2,3,4])
print(type(x))
print(x)
print(len(x))
print ( x[2])   # accessing a item/value in a tuple
print(x[-9])     # gives the first item value
print(x[-1])     # gives the last item value
print(x[2:5])

"""##Tuple
A tuple is a collection which is **ordered** and **unchangeable**. In Python tuples are written with round brackets.

* we could add int, floats, strings, list datatypes inside the tuple as the items/ values inside a tuple

Access Tuple Items
You can access tuple items by referring to the index number, inside square brackets:
"""

thistuple = ("apple", "banana", "cherry")
print(thistuple)
print(thistuple[1])

x = ("applle", [1,2,3,4], "jack", 7.8, 9, 9,"jack")

print(x)
print(x[2])
print(x[-2])
print(x.index("jack"))
print(x.count("jack"))

thistuple = ("apple", "banana", "cherry")
x = ("applle", [1,2,3,4], "jack", 7.8, 9, 9,"jack")
y = x + thistuple
print(y)

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

import keyword # to check which are the keywords
print(keyword.kwlist) # gives the list of keywords present in python

False = 1

#Specify negative indexes if you want to start the search from the end of the tuple:

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

Create Tuple With One Item
To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.

# Example --> One item tuple, remember the commma:

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

Change Tuple Values
Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.

But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

Example --> Convert the tuple into a list to be able to change it:

x = ("apple", "banana", "cherry")
# x[1] = "kiwi"  # we get error
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

x = ("apple", "banana", "cherry")
print(x.index("cherry"))   # here we need to specif only an item in the tuple
print(x[2])  # [index_number] gives us the item present at that index number in the tuple

x = ("apple", "banana", "cherry")
# x[1] = "kiwi"  # we get error
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

#Tuple Length
To determine how many items a tuple has, use the len() method:


thistuple = ("apple", "banana", "cherry")
print(len(thistuple))


# Add Items & removing items
Once a tuple is created, you cannot add items to it or remove items in it. Tuples are unchangeable.

thistuple = ("apple", "banana", "cherry")
thistuple[3] = "orange" # This will raise an error
print(thistuple)

# thus u cannot use methods like append, remove etc in Tuples,  which are used to modify the list items in Lists.

"""### Deleting a tuple"""

# Tuples are unchangeable, so you cannot remove items from it, but you can delete the tuple completely:

Example --> The del keyword can delete the tuple completely:

thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists

thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists

# Join Two Tuples
#To join two or more tuples you can use the + operator:

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

tuple1 = ("a", "ball" , "c")
tuple2 = ("a", 'b' , "call")
tuple3 = ("a", "b" , "c")
tuple4 = ("a", "b" , "c")
tuple5 = ("a", "b" , "c")
tuple6 = (1, 2, 3)

x = tuple1 + tuple2 + tuple3 + tuple4 + tuple5 # + #tuple6
print(x)

t1= ("Hi everyone", "How are you?")
t2= ("I am fine", "How are you?")
t3= ("I am also fine","Thank you")
t4= ("Ok","Need to go","Bye")
t5= ("bye" , )
print(type(t5))
res= t1 + t2 + t3 + t4 + t5
print(res)

x = (1,2,3,4,1,2,3,2,3,2,3)

for i in x :
  print("for i tuple value ",x.count(i))

#The tuple() Constructor/function 
It is also possible to use the tuple() constructor to make a tuple.

Example --> Using the tuple() method to make a tuple:

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

#Check if Item Exists
To determine if a specified item is present in a tuple use the in keyword:



thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

#Loop Through a Tuple
You can loop/iterate through the tuple items by using a for loop, and print the values:

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
You will learn more about for loops in our Python For Loops Chapter.



"""
## Tuple Methods
Python has two built-in methods that you can use on tuples.

### Method	Description
* count() -	Returns the number of times a specified value occurs in a tuple
* index() -	Searches the tuple for a specified value and returns the position of where it was found
"""

help(tuple)

x = (1,2,3,4,1,2,3,2,3,2,3)
print(x.index(2))

"""# Set
A set is a collection which is **unordered** and **unindexed**. In Python, sets are written with **curly brackets**.

* Sets are used to store multiple items in a single variable.

* Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

Note: Sets are unordered, so you cannot be sure in which order the items will appear.

* A set is an unordered collection of items. Every set element is unique (no duplicates) and must be immutable (cannot be changed).

* However, a set itself is mutable. We can add or remove items from it.

* Sets can also be used to perform mathematical set operations like union, intersection, symmetric difference, etc.

## Creating Python Sets
A set is created by placing all the items (elements) inside curly braces {}, separated by comma, or by using the built-in set() function.

It can have any number of items and they may be of different types (integer, float, tuple, string etc.). But a set cannot have mutable elements like lists, sets or dictionaries as its elements.
"""

#Example - Create a Set:

thisset = {"apple", "banana", "cherry", 1,2,3,1,2,3,"apple"}
print(thisset)

l = ["apple", "banana", "cherry", 1,2,3,1,2,3,"apple"]
print(l)
l = set(l)
print(l)

"""### Access Items
You cannot access items in a set by referring to an index or a key.

But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.
"""

# Example --> Loop through the set, and print the values:

thisset = {"apple", "banana", "cherry"}
print("apple" in thisset)
for x in thisset:
  print(x)

thisset = {"apple", "banana", "cherry"}
print(thisset)

set = { 1,2,3}
print(set)

x = {1,2,3,4,5,6}
y = {4,5,6,7,8,9}

print(x & y)  # gives the common items in the given 2 variables

print( x | y) # or combines all  items in the 2 lists

print(x ^ y)  # which are common b/n 2

help(set)

fruits = {"apple", "banana", "cherry"}

fruits.add("orange")

print(fruits)

# To add items from another set into the current set, use the update() method.

#Example --> Add elements from tropical and thisset into newset:

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

# Add Any Iterable
# The object in the update() method does not have be a set, it can be any iterable object (tuples, lists, dictionaries et,).

# Example --> Add elements of a list to at set:

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

Remove Item
To remove an item in a set, use the remove(), or the discard() method.

Example
Remove "banana" by using the remove() method:

thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)
Note: If the item to remove does not exist, remove() will raise an error.

Example
Remove "banana" by using the discard() method:

thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)
Note: If the item to remove does not exist, discard() will NOT raise an error.

You can also use the pop(), method to remove an item, but this method will remove the last item. Remember that sets are unordered, so you will not know what item that gets removed.

The return value of the pop() method is the removed item.

Example
Remove the last item by using the pop() method:

thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)
Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.

Example
The clear() method empties the set:

thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)
Example
The del keyword will delete the set completely:

thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)

help(set)

Help on class set in module builtins:

class set(object)
 |  set() -> new empty set object
 |  set(iterable) -> new set object
 |  
 |  Build an unordered collection of unique elements. 
 |  add(...)
 |      Add an element to a set.
 |      
 |      This has no effect if the element is already present.
 |  
 |  clear(...)
 |      Remove all elements from this set.
 |  
 |  copy(...)
 |      Return a shallow copy of a set.
 |  
 |  difference(...)
 |      Return the difference of two or more sets as a new set.
 |      
 |      (i.e. all elements that are in this set but not the others.)
 |  
 |  difference_update(...)
 |      Remove all elements of another set from this set.
 |  
 |  discard(...)
 |      Remove an element from a set if it is a member.
 |      
 |      If the element is not a member, do nothing.
 |  
 |  intersection(...)
 |      Return the intersection of two sets as a new set.
 |      
 |      (i.e. all elements that are in both sets.)
 |  
 |  intersection_update(...)
 |      Update a set with the intersection of itself and another.
 |  
 |  isdisjoint(...)
 |      Return True if two sets have a null intersection.
 |  
 |  issubset(...)
 |      Report whether another set contains this set.
 |  
 |  issuperset(...)
 |      Report whether this set contains another set.
 |  
 |  pop(...)
 |      Remove and return an arbitrary set element.
 |      Raises KeyError if the set is empty.
 |  
 |  remove(...)
 |      Remove an element from a set; it must be a member.
 |      
 |      If the element is not a member, raise a KeyError.
 |  
 |  symmetric_difference(...)
 |      Return the symmetric difference of two sets as a new set.
 |      
 |      (i.e. all elements that are in exactly one of the sets.)
 |  
 |  symmetric_difference_update(...)
 |      Update a set with the symmetric difference of itself and another.
 |  
 |  union(...)
 |      Return the union of sets as a new set.
 |      
 |      (i.e. all elements that are in either set.)
 |  
 |  update(...)
 |      Update a set with the union of itself and others.