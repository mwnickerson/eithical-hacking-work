#!/bin/python 3

#importing modules
import sys #system functions and paraameters
from datetime import datetime as dt # imports a specifc part of datetime you can use alias to import to shorten


print(sys.version) #will return and error because we
print(dt.now()) # will return the exact time of now

def nl():
	print('\n')

nl()

#Advanced Strings

my_name = "Matthew"
print(my_name[0])
print(my_name[-1])

sentence = "This is a sentence."
print(sentence[:4])
print(sentence.split())

sentence_split = sentence.split()
sentence_join = ' '.join(sentence_split)
print(sentence_join)
	
quote1 = "he said , 'give me all your money'"
quote2 = "he said , \" give me all your money\""
	
print(quote1)
print(quote2)

nl()

too_much_space = "                              Hello                                       "
print(too_much_space.strip()) #.strip command strips whatever is in the field)

print("A" in "Apple") #will print true its very case senstivie

letter = "A"
word = "Apple"
print(letter.lower() in word.lower()) # helps find the lower case letter in the string .lower() is the command


movie = "The Hangover"
print("My favorite movie is {}.".format(movie)) #rather than typing out palceholder you can use brackets and .format() makes it easier to format and its more fluid

#dictionaries key value pairs {}
drinks = {"white Russian": 7, "Old Fashioned": 10, "lemon drop": 8} #drink is your key price is your value
print(drinks)

employees = {"Finance": ["Bob", "linda", "tina"], "IT": ["gene" , "louise" , "teddy"], "HR": ["jimmy jr" , "mort"]} # this is our dictionary
print(employees)

employees['Legal'] = ["Mr. Frond"] # this will add a new key value pair
print(employees)

employees.update({"Sales": ["Andie", "Ollie"]}) # another way of adding a key value pair to the the dictionary
print(employees)

drinks['White Russian'] = 8  #you can update dictionary values 
print(drinks)

print(drinks.get("White Russian")) # you can print specific entriees in a a dictionary and return their value


nl()

print("Finished")

sys.exit













