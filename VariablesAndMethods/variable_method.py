#!/bin/python3

#Programmer: Kyle Rocco
#Program: Variables and Methods
#Date: 1.11.24

quote = "Michigan sucks!" #variable

print(quote) #call variable to print
print(quote.upper()) #uppercase
print(quote.lower()) #lower
print(quote.title()) #title case
print(len(quote)) #counts number of characters

name = "JJ McCarthy" #string
age = 47 #int
gpa = 1.3 #float - has decimal

print(age)
print(int(gpa)) #casts a float into and integer, won't round up

print("\nMy name is " + name + " and I am " + str(age) + " with a GPA of " + str(gpa) + ".")

print("\nMy name is", name ,"and I am", age , "with a GPA of", str(gpa) + ".")
#Concating using a comma instead of a + while casting our gpa vairable into a string account for the spacing before the period


age += 1 #adds 1 to the variable age

print("\n" + str(age))


age += 10 #adds 10 to the variable age

print("\n" + str(age))

birthday = 1 #We can add two variables with the calues as int together
age += birthday
print(age)
