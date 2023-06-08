#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 01:10:13 2023

@author: hetvi
"""
#Week 6

#1. Create 3 favorite things about you using mulitline string 

Hdk = ''' My self Hardik, I am biotechnologist and working with Appotex pharma. 
Due to techsavvy nature i decide to change my profession into software technology.'''
print(Hdk)
print("======================================================")

#E 1. Using variables in string print - student full details . ( firstname,lastname, address) 
first_Name = "Hardik"
last_Name = "Patel"
address = "Scarborough"
full_details = f"{first_Name} {last_Name} {address}"
print(full_details.upper())
print("======================================================")

# E 2 .Create a list of agile software .Insert the values , delete one item from the list . use slicing and display the list of software's 

list_of_Agile_Software = ['Monday','ClickUp','JIRA','wrike']
list_of_Agile_Software.insert(0, 'Smartsheet')
print(list_of_Agile_Software)
del list_of_Agile_Software[1]
print(list_of_Agile_Software)
print(list_of_Agile_Software[:3])
print(len(list_of_Agile_Software))

# E 3 .Start with the list by  printing three course’s name like comp100,comp120,comp213 . 
# Print a message saying that you are enrolled in that course.  
# The text of each message should be the same, but each message should be personalized with the course ’s name.Append a new course GNET 
soft_Eng = ['comp 120','com 171','comp124']
print(soft_Eng)
print("I am enrolled in" + soft_Eng[0])
print("I am enrolled in" + soft_Eng[1])
print("I am enrolled in" + soft_Eng[2])
soft_Eng.append('GNED')
print(soft_Eng)
#week 8

#Exercise 1 
#1. Use the following dictionary and answer the question 

favorite_languages = {'jen': 'HTML','sarah': 'c','edward': 'ruby','phil': 'C#',}
print(favorite_languages)

#Change the value from C# to Python for the key phil 
favorite_languages["phil"] = "Python"
print(favorite_languages)

#Add an item in the dictionary 

favorite_languages["selenium"]="Java"
print(favorite_languages)
#Remove an item from the dictionary

favorite_languages.pop("sarah")
print(favorite_languages)
#List all the values in the dictionary 
k = favorite_languages.keys()
v = favorite_languages.values()
print(k)
print(v)
print("======================================================")
#Exercise 2
#create   a python dictionary called student . Include student name, age, subject, semester, grade and lab keys. Include the value for each key accordingly. Display keys separately and values separately in the print statement 

student_dict = {"student name": "HARDIK","Age":31,"Subject":"Software Eng.","semester":"Winter","Grade":"A+","Lab Keys":123}
print(student_dict)
print("======================================================")

#Week 9
#Write a program in python using if condition . Input the temperature (user input) . Check if the temperature is less than 98 display the result as cold. otherwise  if the temperature more than 98 , display the result as Hot . otherwise display them as normal . 
def Temperture():
    Temp = int (input("Enter Temperature: "))
    if Temp <98:
        print("It is cold")
    elif Temp >=98:
        print("It is Hot")
    elif Temp == 98:
        print("IT is Normal")
Temperture()

#Exercise 2
# Program to iterate agile values  through a list using indexing. create the following agile values in list. use for loop and iterate over the list 

#agile_values = ['Individuals and interactions', 'Working software ', 'Customer collaboration ','Responding to change']

agile_values = ['Individuals and interactions', 'Working software ', 'Customer collaboration ','Responding to change']

for i in range(len(agile_values)):
    print(agile_values[i])
    print("======================================================")

# week 10
#Exercise 1
#Create a function called team_collaboration() . pass two team collaboration software names as the arguments. 

#The function should print "I use ------- software for team collaboration "

def team_collaboration(Asana,Slack):
    
    print("I use" + Asana + "software for team collaboration.")
    print("I use" + Slack + "software for team collaboration.")
    print("======================================================")
team_collaboration("Asana","Slack" ) 

    

#Exercise 2
#Create a function called project() that store project_id globally and locally . Call the function and display both the id's . 
#Print the statement as 
#"My global project id is :"
#"My internal project id is :"
def project():
   global project_id 
   project_id = 12345
   project_id_internal = 67890
   print("My global project id is:", project_id)
   print("My internal project id is:", project_id_internal)
   print("======================================================")
project()
#week 11
#Exercise 1 
#Import the correct library and print a calendar for your project. Print October month calendar of this year 

#sample output as follows :
    
    # importing the calendar module
import calendar
# initializing the year and month
year = 2023
month = 10
# printing the calendar
print(calendar.month(year, month))



#Exercise 2 
#Use 5 Functions in Python Math Module  and print the results 
import math

#square root of 25 which is 5
print(math.sqrt(25))

#factorial of 5 is 120
print(math.factorial(5))

#gcd of 5 and 10 is 5
print(math.gcd(5,10))

#logarithm of 100 base 10 is 2
print(math.log10(100))

#power function: 2^3 is 8
print(math.pow(2,3))

#week 12

#Exercise 1 
#using OSmodule , explore the following functions  and execute the command 

#1. Write a command to create a new directory using OS Library 

import os
Path = '/Volumes/Hardik/ABC'
try:
    os.mkdir(Path)
    print("Folder Created")
except FileExistsError:
    print("File exists:")    
    

#2. Write a command to delete the existing file 
import os
Path = '/Volumes/Hardik/ABC'
#os.remove(Path)

#Exercise 2
#using Pandas library , produce the following output . using pandas data frame organize the data into rows and columns 
import pandas as pd
data = {
        'Subject_id':[1,2,3,4],
        'Student_name':["Joseph","Eva","Kevin","Joseph"],
        'Course':["Soft Eng","Artificial Intelligence","Gaming","Soft Eng Tech"]
        }
data1 = pd.DataFrame(data)
print(data1)