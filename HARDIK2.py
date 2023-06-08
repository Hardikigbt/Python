#!/usr/bin/env python3
# -*- coding: ut
# To comment out:
## WEEK-3##
print("Hello,Python!")

# Install##
# C:\Users\Your Name>python --version- 
# To check- python --version;

# Indentation: Ideal space is 4, Mininum 1; 
#1
if 5 > 2:
 print("five is grate then 2") 
#2
if 5 > 2:
 print("Five is greater than two!") 
if 5 > 2:
    print("Five is less than two!") 
 
# Variables:
x= 10
y= "Python"
print(x,y)

# Casting:
x= str(15)
y= int(12)
z= float(3)
print(x,y,z)    

#Get the type:
x=5
y=3.4
z='true'
print(type(x))
print(type(y))
print(type(z))

# Variable name: CamelCase-myVariableName; Pascal case-MyVariableName; 
# Snake Case-my_variable_name

# Variable-assign Value
x,y,z = "abc","def","ghi"
print(x)
print(y)
print(z)    

# One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

# Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Output Variables : for number + is math
#1
y = "is"
z = "awesome"
print(x, y, z)
#2
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

# Global Variables:
# 1
x = "easy"

def myfunc():
  print("Python is " + x)

myfunc()
#2
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)
#3
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

# Data Type:
#x = str("Hello World")	str	
#x = int(20)	int	
#x = float(20.5)	float	
#x = complex(1j)	complex	
#x = list(("apple", "banana", "cherry"))	list	
#x = tuple(("apple", "banana", "cherry"))	tuple	
#x = range(6)	range	
#x = dict(name="John", age=36)	dict	
#x = set(("apple", "banana", "cherry"))	set	
#x = frozenset(("apple", "banana", "cherry"))	frozenset	
#x = bool(5)	bool	
#x = bytes(5)	bytes	
#x = bytearray(5)	bytearray	
#x = memoryview(bytes(5))	memoryview

# Numbers:
x = 1    # int
y = 2.8  # float
z = 1j   # complex

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))    