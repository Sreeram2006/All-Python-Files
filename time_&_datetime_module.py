# -*- coding: utf-8 -*-
"""Time & datetime module.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JdQl2p7V-WDGSL8s8GCb_3vwNbRgu-21
"""

# Python has a module named datetime to work with dates and times.

"""The epoch is the point where the time starts, and is platform dependent. For Unix, the epoch is January 1, 1970, 00:00:00 (UTC). To find out what the epoch is on a given platform, look at time.gmtime(0)."""

import time
print(time.gmtime(0))

import time
print(time.gmtime(0))
print(time.localtime())  # gives us the present time
a = time.localtime()
print("year: " , a.tm_year)
print(f"{a.tm_mday}-{a.tm_mon}-{a.tm_year}")

print(time.strftime(""))

import time
print(time.time())  # to get present time in sec 
a = time.time()
print(time.localtime(a))
c = time.localtime(a)
print(f"{c.tm_hour + 5.5} : {c.tm_min }: {c.tm_sec}")
# print(isd)

import time
print(time.time())  # to get present time in sec 
a = time.time()
print(time.localtime(a))
c = time.localtime(a)
alarm = time.sleep(10)
print("wake up!!!")



"""https://realpython.com/playing-and-recording-sound-python/ """

pip install playsound
from playsound import playsound
playsound('audio.mp3')

"""### Time module reference links :-


* https://docs.python.org/3/library/time.html 
* https://www.programiz.com/python-programming/datetime 
* https://www.geeksforgeeks.org/python-datetime-module-with-examples/ 

* https://www.geeksforgeeks.org/how-to-create-a-countdown-timer-using-python/ 

* https://www.geeksforgeeks.org/understanding-time-complexity-simple-examples/
* https://www.geeksforgeeks.org/time-functions-in-python-set-1-time-ctime-sleep/

https://docs.python.org/3/library/calendar.html#module-calendar
"""

MODULE  is a spearate file/ library / folder 

----> which contains the data or functions created/defined for that particular topic like maths,  random, date, arrays et

Python Datetime
Python Dates
A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.
https://www.w3schools.com/python/python_datetime.asp

import datetime

x = datetime.datetime.now()
print(x)

import datetime

x = datetime.date.()
print(x)

import datetime

d = datetime.date(2019, 4, 13)
print(d)

We can only import date class from the datetime module. Here's how:


from datetime import date

a = date(2019, 4, 13)
print(a)

Example 4: Get current date
You can create a date object containing the current date by using a classmethod named today(). Here's how:


from datetime import date

today = date.today()

print("Current date =", today)











change = 0
i=0
denom_array = [2000, 1000, 500, 100, 50, 20, 10, 5, 2, 1]
amount = int(input)

"""**Time**
Modules -- libray Time module is a special libray in python that contains logic for time calculation
"""

import time
a = time.time()
#12:00 January 1 1970 until now in sec -----standard calcu
t = 60*60*24*365  # no of sec in year,  ----- no of years scince 1970
b = a/t  #no of years scince 1970
print (a)
print(b)
c = b-50
d = c*12  # months
e = (d-6)*30 
print(e)

# alram = time.time()
z = 0
while (z<5):
  
  name = input("enter name:")
  if name =="honey":
z = z+1
print( "okay")
  else:
      print("sorry type another name")

#GMT - greenwich mean time
time.gmtime()

m = time.ctime()  # ist - 5.5 hrs ahead frm gmt
print(m)

x = time.localtime()
y = time.strftime("%y")  # d- day, m - month, y - year
print(x)
print(y)

x = time.timezone
print(x)

#https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
import os, time
time.strftime('%X %x %Z')
os.environ['TZ'] = 'Asia/Calcutta'
time.tzset()
time.strftime('%X %x %Z')

"""#https://en.wikipedia.org/wiki/List_of_tz_database_time_zones """

#print(time.time())
import time
z=0
while (z<1):
  t = time.time()
d = (2020, 7, 9, 13, 2, 0, 0, 0)
n = time.mtime(d)-t
if n<0:
    print("time is up")
    z+=1

import time
t = time.time()
d = (2020, 7, 9, 13, 10, 0, 0, 0)
n = time.mtime(d)-t
print(n)





# import the time module 
import time 

# define the countdown func. 
def countdown(t): 
	
	while t: 
		mins, secs = divmod(t, 60) 
		timer = '{:02d}:{:02d}'.format(mins, secs) 
		print(timer, end="\r") 
		time.sleep(1) 
		t -= 1
	
	print('Fire in the hole!!') 


# input time in seconds 
t = input("Enter the time in seconds: ") 

# function call 
countdown(int(t))





"""### Time module

https://docs.python.org/3/library/time.html

https://www.geeksforgeeks.org/timer-objects-python/ - set timer

https://www.geeksforgeeks.org/how-to-create-a-countdown-timer-using-python/

https://www.programiz.com/python-programming/time

https://realpython.com/python-time-module/


"""