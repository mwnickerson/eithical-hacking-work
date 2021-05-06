#!/bin/python3

#Variables and Methods
quote = "All is fair in love and war."
print(quote.upper()) #upper case
print(quote.lower()) #lower case
print(quote.title()) #title case
print(len(quote)) #length of quote

name = "Matthew" #string
age = 29 #int int(29)
GPA = 2.1 #float float(2.1)

print(int(age))
print(int(29.7)) 

print("My name is " + name +" and I am " + str(age) + " years old.")

age += 1
print(age)

birthday = 1 
age += birthday
print(age)

print('\n')
#functions

print("here is an example function:")

def who_am_i():  #this is a function
	name = "matthew"
	age = 29
	print("My name is " + name +" and I am " + str(age) + " years old.")

who_am_i()


#adding paramaters
def add_one_hundred(num):
	print(num + 100)

add_one_hundred(100)

#multiple parameters

def add(x,y):
	print(x + y)

add(7,7)

def multiply(x,y):
	return x * y

multiply(7,7)

print(multiply(7,7))

def square_root(x):
	print( x ** .5)

square_root(64)

def nl():
	print('\n')

nl()

#boolean expression (true and false) 

bool1 = True
bool2 = 3*3 == 9
bool3 = False
bool4 = 3*3 != 9

print(bool1,bool2,bool3,bool4)
print(type(bool1))

nl()

#relational and boolean operators
greater_than = 7 > 5
less_than = 5 < 7
greater_than_equal_to = 7 >= 7
less_than_equal_to = 7 <=7

test_and = (7 > 5) and (5 < 7) # this statement is true
test_and2 = (7 > 5) and (5 > 7 ) # this statement is false
test_or = (7 > 5) or (5 < 7) # wil;l return true
test_or2 = (7 > 5) or (5 > 7) #this is also true bc with or only 1 needs to be true
test_not = not True #false

nl()

#conditional statements

def drink(money):
	if money >= 2:
		return "You've got yourself a drink"
	else:
		return "NO drink for you!"
		
print(drink(3))
print(drink(1))

def alcohol(age,money):
	if ( age <= 21 ) and ( money >= 5):
		return "We are getting a drink!"
	elif (age >= 21 ) and ( money < 5):
		return "Comeback with more money."
	elif (age < 21 ) and (money >= 5):
		return "nice try, kid!"
	else:
		return "You're too poor and too young"
		
print(alcohol(21, 5))
print(alcohol(21,4))
print(alcohol(19,6))
print(alcohol(13,1))


nl()

# lists have brackets []
movies = ["godzilla", "the hangover" , "star wars" , "lord of the rings"]
print(movies[1]) #prints second item in list 
print(movies[0]) # prints the first one 0 is the first item 
print(movies[1:4])# need to pull from past the one you are trying to grab
print(movies[1:]) # prints the total list
print(movies[:1]) 
print(movies[:2]) #grabs up to 
print(movies[-1]) # grabs the absolute last last item in list

print(len(movies)) # sees the length of the list 
movies.append("JAWS") # adds jaws to the end of the list its always addeed to the end
print(movies)

movies.pop() #removes the last one from the list
print(movies)


movies.pop(0) # we can use a selector within the "pop" 
print(movies)


nl()

# tupples do not change ()
grades = ("a" , "b" , "c" , "d" , "f")
#commands like pop and append do not work

print(grades[1])



nl()

#looping

#for loops - start to finish of an iterate
vegetables = ["cucumber" , "carrot" , "brocolli"]
for x in vegetables:
	print(x)  # for every item in vegetables it gets printed
	
	
#While loops - executre as long as true

i = 1

while i < 10:  #statement executes when i is less than 0
	print(i)  # prints i 
	i += 1    # adds one to it and the statement runs again until it hits 10
	
	



	






