#!/bin/python3

#Programmer: Kyle Rocco
#Program: Functions
#Date: 1.19.2024

def nl(): #new line function
	print('\n')
	
nl()






def who_am_i(): #this is a function without parameters
	name = "Kyle" #local variable
	age = 46
	print("My name is" ,name, "and I am",age, "years old.") 
	
who_am_i()
nl()

def add_one_hundred(num): #num is a Parameter
	print(num + 100)
	
add_one_hundred(2) #2 is the Argument which inserts itself into the Parameter

nl()

def add(x,y):
	print(x + y)
	
add(3,5)
nl()

