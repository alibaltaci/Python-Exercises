# Python Basic (Part -I) - Exercises
# https://www.w3resource.com/python-exercises/python-basic-exercises.php



# 1. Write a Python program to print the following string in a specific format (see the output).

"""
Sample String : "Twinkle, twinkle, little star,
                How I wonder what you are! Up above the world so high,
                Like a diamond in the sky. Twinkle, twinkle,
                little star, How I wonder what you are" Output :

Twinkle, twinkle, little star,
	    How I wonder what you are!
		        Up above the world so high,
		        Like a diamond in the sky.
Twinkle, twinkle, little star,
	    How I wonder what you are
"""

print("Twinkle, twinkle, little star, \n\t\tHow I wonder what you are!\n\t\t\t\tHow I wonder what you are!"
      "\n\t\t\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n\t\tHow I wonder what you are")




# 2. Write a Python program to get the Python version you are using.

import sys
print("Python Version")
print(sys.version)
print("\nVersion info")
print(sys.version_info)



# 3. Write a Python program to display the current date and time.

"""
Sample Output :
Current date and time :
2014-07-05 14:34:14
"""

import datetime
now = datetime.datetime.now()
print("Current date time:")
print(now.strftime("%Y-%m-%d %H:%M:%S"))



# 4. Write a Python program which accepts the radius of a circle from the user and compute the area.

"""
Sample Output :
r = 1.1
Area = 3.8013271108436504
"""

from math import pi
r = float(input("Input the radius of the circle:"))
print("The area of the circle with radius {} is {}".format(str(r), str(pi * r**2)))



# 5. Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.

# way 1:
def name():
      fn = input("Input your first name: ")
      ln = input("Input your last name: ")
      print("Hello {} {}".format(ln, fn))

name()

# way 2:
def name_2():
      fn = input("Input your first name: ")
      ln = input("Input your last name: ")
      print("Hello " + ln + " " + fn)

name_2()



# 6. Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.

"""
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')
"""

values = input("Input some coma seprated numbers: ")
list = values.split(",")
tuple = tuple(list)
print("List: ", list)
print("Tuple: ", tuple)