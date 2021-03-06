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



# 7. Write a Python program to accept a filename from the user and print the extension of that.

"""
Sample filename : abc.java
Output : java
"""

filename = input("Input the filename: ")
filename_ext = filename.split(".")
print("The extension of the file is: " + repr(filename_ext[-1]))




# 8. Write a Python program to display the first and last colors from the following list.

"""
color_list = ["Red","Green","White" ,"Black"]
"""

color_list = ["Red","Green","White" ,"Black"]
print("%s , %s" % (color_list[0], color_list[-1]))



# 9. Write a Python program to display the examination schedule. (extract the date from exam_st_date).

"""
exam_st_date = (11, 12, 2014)
Sample Output : The examination will start from : 11 / 12 / 2014
"""

exam_st_date = (1, 1, 1995)
print("The axamination will start from: %i / %i / %i" % exam_st_date)




# 10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn

"""
Sample value of n is 5
Expected Result : 615
"""

n = int(input("Input a number: "))
n1 = int("%s" % n)
n2 = int("%s%s" % (n,n))
n3 = int("%s%s%s" % (n,n,n))
print("Result for the number {}: {}".format(n, (n1+n2+n3)))



# 11. Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).

"""
# Sample function : abs()
# Expected Result :
# abs(number) -> number
# Return the absolute value of the argument.
"""

print(abs.__doc__)



# 12. Write a Python program to print the calendar of a given month and year.

# Note : Use 'calendar' module.

import calendar
y = int(input("Input the year: "))
m = int(input("Input the month: "))
print(calendar.month(y, m))

def calen(y, m):
      import calendar
      print(calendar.month(y, m))

calen(1995, 1)



# 13. Write a Python program to print the following here document.

"""
Sample string:
a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example
"""

print("""
a string that you "don't" have to escape
This
is a  ....... multi-line
heredoc string --------> example
""")



# 14. Write a Python program to calculate number of days between two dates.

"""
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days
"""

from datetime import date
first_date = date(1995, 1, 1)
last_date = date(2021, 1, 16)
delta = last_date - first_date
print(delta.days)

"""
NOTE:
year = int(input('Enter a year'))
month = int(input('Enter a month'))
day = int(input('Enter a day'))
date1 = datetime.date(year, month, day)
"""



# 15. Write a Python program to get the volume of a sphere with radius 6.

from math import pi
r=6.0
print("The volume of the sphere is: {}".format(4.0/3.0 * pi * r**3))



# 16. Write a Python program to get the difference between a given number
# and 17, if the number is greater than 17 return double the absolute difference.

def difference(n):
      if n <= 17:
            print("17 - {} = {}".format(n, 17-n))
      else:
            print("{} - 17 x 2 = {}".format(n, n - 17 * 2))

difference(45)
difference(3)



# 17. Write a Python program to test whether a number is within 100 of 1000 or 2000.

def near_thousand(n):
      return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))
print(near_thousand(1000))
print(near_thousand(900))
print(near_thousand(800))
print(near_thousand(2200))



# 18. Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum.

def sum_thrice(X,Y,Z):
      sum = X+Y+Z
      if X==Y==Z:
            sum = sum * 3
      return sum

sum_thrice(2,6,9)

sum_thrice(6,6,6)



# 19. Write a Python program to get a new string from a given string where "Is" has been added to the front.
# If the given string already begins with "Is" then return the string unchanged.

def new_string(str):
      if len(str) >= 2 and str[:2] == "Is":
            return str
      return "Is" + str

new_string("Ispython")

new_string("git")



# 20. Write a Python program to get a string which is n (non-negative integer) copies of a given string.

def larger_string(str, n):
      result = ""
      for i in range(n):
            result = result + str
      return result

larger_string("AI", 5)