print('hi')
print("hello how are you")
print(2)
print(1+2)
print("i am a good person\nand a good human being")
# keep this text dont remove it
''' {multiline comment}
print(2)
print(1+2)
print("i am a good person\nand a good human being")
'''
print("i am a \"good person\"\nand a good human being")  # \"xyz\" is a escape character for ""
print("hello", 1, 2, 3, sep="~", end="009\n") #seperator for seperate characters
print("ayushman")

x = "hello"
y = "world"
print(x+ " " +y)

x = 5
y = "world"
print(y)
print(x)

x = str(3)
y = int(3)
z = float(3)
print(x, y, z)

x = 5
y = "world"
print(type(x))
print(type(y)) #indicates the type of syntax

'''
# Legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
'''

x, y, z = "A", "B", "C",
print(x, y, z)

x=y=z= "A"
print(x, y, z)

letters = ["A", "B", "C"]
x, y, z = letters
print(x)
print(y)
print(z)

x= "python is great"
print(x)

x= "python"
y="is"
z="awesome"
print(x, y, z)

x = "python"
y= " is"
z= " interesting"
print(x + y + z)


x = "nice"
def myfunc():
    print("python is " + x)
myfunc()

x = "amazing"
def myfunc():
    x = "fantastic"
    print("python is " + x)
myfunc()
print("python is " + x)

def myfunc():
    # global x
    x = "greatest" # now x is used globally
myfunc()
print("python is " + x)

'''
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
'''

z = 1j
print(type(z))

x=1
y=1.1
z=1j
a= float(x)
b= int(y)
c= complex(x)
print(a,b,c)
print(type(a), type(b), type(c))


import random
print(random.randrange(1, 10))
# print(random.randint(0, 10))

a = "hello, world"
print(a[2])

for x in "banana": #for loop to loop through letters in banana
    print(x)

a = "hello, world"
print(len(a))   #to find out the length of the string

txt = "life is going on amazing"
print("going" in txt) #to check if the given string has 'going' if yes it return true if no it return false.

txt = "life is going on amazing"
if "life" in txt:
    print("'life' present in text")
else: print("'life' not present in text")

b = "hello world"
print(b[2:4])

a = "Hello World"
print(a.upper())
print(a.lower())

a = "     hello"
print(a.strip())

a = "World"
print(a.replace("o", "i"))

a = "hello, world!"
print(a.split(","))

a = "hello"
b = " world"
c = a+b
print(c)

'''
this is the wrong way of combining the strings and numbers
age = 10
txt = "John is " + age + " years old"
print(txt)
we can use format to combine it together 
'''

age = 10
txt = "jhon is {} years old"
print(txt.format(age))


quantity = 10
item = "mango"
price = 1000
myorder = "i ordered {} quantity of {} which costed me {}"
print(myorder.format(quantity, item, price))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

# escape character
txt = "We are the so-called \"Vikings\" from the north." 

if 2 > 3:
    print("two is greater than three")
else:
    print("not greater flase ans")

print(bool("Hello"))
print(bool(15))

x = "Hello"
y = 18
print(bool(x))
print(bool(y))

# any number is true except 0 and function: __len__
x = 0
print(bool(x))

class myclass():
    def __len__(self):
        return 0
myobj = myclass()
print(bool(myobj))
# 

def myFunction():
    return True
if myFunction():
    print("Yes")
else: print("No")

x = 100
print(isinstance(x, int)) 

print((4+2) - (2+2))

# list are used to store multiple items in a single variable
myList = ["a", "b", "c", "d", "e"]
print(myList)
print(len(myList))

mylist2 = list(("a", "b", "c", "d", "e"))
print(mylist2)


# PYTHON COLLECTIONS (ARRAYS) --------------------------------
# There are four collection data types in the Python programming language:

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.   

thislist = ["apple", "banana", "cherry", "pear"]
print(thislist[3])

thislist = ["apple", "banana", "cherry", "pear"]
print(thislist[-3]) #negative indexing refers from the back

thislist = ["apple", "banana", "cherry", "pear"]
print(thislist[-3:3]) #range of indexes

thislist = ["apple", "banana", "cherry", "pear"]
if "apple" in thislist:
    print("this has apple")
else: print("this index does not have an apple") #to check item

thislist = ["apple", "banana", "cherry", "pear"]
thislist[2] = "pineapple"
print(thislist) #changes the third item

thislist = ["apple", "banana", "cherry", "pear"]
thislist.insert(1, "kiwi")
print(thislist) #inserts kiwi as 2nd item as of the 1st index

thislist = ["apple", "banana", "cherry", "pear"]
thislist.append("orange")
print(thislist) #adds orange to thislist item

thislist = ["apple", "banana", "cherry", "pear"]
thislist.insert(1, "orange")
print(thislist) #adds items as the second position

thislist = ["apple", "banana", "cherry", "pear"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical) 
print(thislist)

thislist = ["apple", "banana", "cherry", "pear"]
thislist.remove("apple")
print(thislist)

thislist = ["apple", "banana", "cherry", "pear"]
thislist.pop(1)
print(thislist) #pop() to remove specific index

thislist = ["apple", "banana", "cherry", "pear"]
thislist.pop()
print(thislist) #if you do not specify it removes the last index

thislist = ["apple", "banana", "cherry", "pear"]
del thislist[1]
print(thislist) #remove the given index

thislist = ["apple", "banana", "cherry", "pear"]
thislist.clear()
print(thislist) #clears the list

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i += 1

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

# Condition
#The condition is like a filter that only accepts the items that valuate to True.

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]
print(newlist)

#The condition if x != "apple"  will return True for all elements other than "apple", making the new list contain all fruits except "apple".

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits]
print(newlist) #now there is no if statement thus it prints everythingon the fruits list

# Iterable
# The iterable can be any iterable object, like a list, tuple, set etc. You can use the range() function to create an iterable.
newlist = [x for x in range(10)]
print(newlist)

newlist = [x for x in range(10) if x<5]
print(newlist)


#Expression

fruits = ["Apple", "Banana", "Cherry", "Kiwi", "Mango"]
newlist = [x.upper() for x in fruits]
# newlist = [x.lower() for x in fruits]
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = ['hello' for x in fruits]
print(newlist) # prints hello to all values of newlist

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist) #Returns the item if it is not banana, if it is banana return orange

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort() #sorts alphabetically
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse=True) #sorts alphabetically reversed 
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse=True)
print(thislist)

# Customized Sort Function

#Sort the list based on how close the number is to 50
def myfunc(n):
    return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key=myfunc)
print(thislist)

# Case sensitive sorting can give an unexpected result
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

# Perform a case-insensitive sort of the list
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key=str.lower)
print(thislist)

# Reverse the order of the list items
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)


#to copy a list 
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#another way to copy a list 
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

# Join Lists

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
    list1.append(x) #another method to join lists
print(list1)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2) #another method to join lists
print(list1)


# list methods
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list



#Tuple - Tuple items are ordered, unchangeable, and allow duplicate values.Tuples are indexed.
mytuple = ("apple", "banana", "cherry")
print(mytuple)

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple) #its allows duplicated as tuple are indexed they can have items with same value

thistuple = ("apple", "banana", "cherry")
print(len(thistuple)) #prints the number of items

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple)) # output: type str

#Tuple item can be of any Data type
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
print(tuple1)
print(tuple2)
print(tuple3)

tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)


# Tuple() Constructor
thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)

# Access Tuple Items 
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

# Check if items exists 
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("yes 'apple' is in fruits tuple")

# Change Tuple values 
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

#add items
x = ("apple", "banana", "cherry")
y = list(x)
y.append("kiwi")
x = tuple(y)
print(x)

# add tuple to tuple
x = ("apple", "banana", "cherry")
y = ("orange",)
x += y
print(x)

#remove items
x = ("apple", "banana", "cherry")
y = list(x)
y.remove("cherry")
x = tuple(y)
print(x)

'''
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists
'''

# Packing a tuple:
fruits = ("apple", "banana", "cherry")
print(fruits)

# Unpacking a tuple:
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)


fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(*red) #Assigns the rest of the values 

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic) #Add a list of values the "tropic" variable
print(red)


# Loop through a Tuple
thislist = ("apple", "mango", "papaya", "pineapple",)
for x in thislist:
    print(x)


# Loop Through the Index Numbers   
thislist = ("apple", "mango", "papaya")
for i in range(len(thislist)):
    print(thislist[i])


# Using While Loop
thistuple = ("apple", "mango", "papaya")
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i += 1

# Join Two Tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

#Multiply Tuples
fruits = ("apple", "banana", "cherry")
mytuple = fruits*2
print(mytuple)


# Tuple Methods
# Python has two built-in methods that you can use on tuples.
# count()--> Returns the number of times a specified value occurs in a tuple
# index()--> Searches the tuple for a specified value and returns the position of where it was found



# Sets = Sets are used to store multiple items in a single variable.A set is a collection which is unordered, *unchangeable*, and unindexed.

thisset = {"apple", "banana", "cherry"}
print(thisset)

thisset = {"apple", "banana", "cherry", "apple"}
print(thisset) #duplicates will be ignored

thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset) #true and 1 considered to be the same

thisset = {"apple", "banana", "cherry"}
print(len(thisset)) #to get number of items in set

#set can be of any data type 
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
print (set1)
print (set2)
print (set3)

# A set with strings, integers and boolean values
set1 = {"abc", 34, True, 40, "male"}
print(set1)

# The set() Constructor
thisset = set(("apple", "banana", "cherry"))
print(thisset)

#Access Items
thisset = {"apple", "banana", "cherry"}
for x in thisset: 
    print(thisset)

thislist = {"apple", "banana", "cherry"}
print("banana" in thisset) #returs true (banana present)

# Change Items
# Once a set is created, you cannot change its items, but you can add new items.

# Add New Items
thisset = {"apple", "banana", "cherry"}
thisset.add("kiwi")
print(thisset)

# Add Sets
thisset = {"apple", "banana", "cherry"}
tropical = {"orange","kiwi"}
thisset.update(tropical)
print(thisset)

# Add Any Literals
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

# Remove Item
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

#If the item to remove does not exist, remove() will raise an error.

#removing using discard()
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

#using pop() to remove randon item
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

#using clear() and del() empties the set and thus it throws an error while printing it

# Loop Items 
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)

#Join Two sets
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2) #can also use update
print(set1)

# Both union() and update() will exclude any duplicate items.

#To Keep ONLY the Duplicates:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z) #Returns a set that contains the items that exist in both set x, and set y

# Keep All, But NOT the Duplicates
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference(y)
print(x) #Returns a set that contains all items from both sets, except items that are present in both

# NOTE: The values True and 1 are considered the same value in sets, and are treated as duplicates


#Dictionaries = Dictionaries are used to store data values in key:value pairs.A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

#example
thisdict = {
    "brand": "ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

#duplicate values overwrite existing values
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

#To print length of items 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(len(thisdict))

#The values in dictionary items can be of any data type
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict)) #<class 'dict'>

#The dict() Constructor
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

#Accessing Items 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["model"])

#another way to access dict is get() method 
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.get("year")
print(x)

# To see the key values in a dict we use keys()
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
z = thisdict.keys()
print(z)

#Add a new item to the original dictionary, and see that the keys list gets updated as well
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys()
print(x)
car["color"] = "black"
print(x)

# Using values() to get the values of the keys 
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print(x)

# To make a change in the original dictionary, and see that the values list gets updated as well
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print(x)
car["year"] = 2000
print(x)

# Check if the Keys Exists 
thisdict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in thisdict dictionary")

# Change Values
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2023
print(thisdict)

# Update Dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 1999})
print(thisdict)

# Adding Items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

# Update Dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "black"})
print(thisdict)

# Removing Items 
# using pop()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

# using popitem() and removing items randomly
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

#using del()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

#clear() clears the dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
# print(thisdict) throws an error as the dictionary is cleared

# loop through dictionaries
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
    print(x) 

#print all values
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
    print(thisdict[x])

# to print values we also use values()
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.values():
  print(x)

#to print all the keys we use 
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.keys():
  print(x)

# items() to print both keys and values
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x , y in thisdict.items():
  print(x, y)

#Copy Dictionaries
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

#Make a copy of a dictionary with the dict() function
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)

# Nested Dictionaries
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)


child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily['child2']['name'])


# Python Conditions and If statements

'''
Python supports the usual logical conditions from mathematics:
Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
These conditions can be used in several ways, most commonly in "if statements" and loops.
'''


a = 33
b = 200
if b>a:
  print("b is greater than a")

# Indentation
# Python relies on indentation (whitespace at the beginning of a line) to define scope in the code. Other programming languages often use curly-brackets for this purpose.
# Example
# If statement, without indentation (will raise an error):
# a = 33
# b = 200
# if b > a:
# print("b is greater than a") # you will get an error

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal") # elif is like a else if code

a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else: 
    print("a is greater than b")

a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("a is greater than b")

# statements can be also written in one line
a = 200
b = 33
if a > b: print("a is greater than b")
else: print("a is greater than b")

# we can also write if else statements in same line
a = 330
b = 330
print("A") if a > b else print ("=") if a == b else print("B")

#  'and' also can be used. It is a logical operator and is used to combine conditional statements
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")

#  'Or' also can be used. It is a logical operator and is used to combine conditional statements
a = 200
b = 33
c = 500
if a > b or a > c:
    print("At least one condition is True")

#  'not' also can be used. It is a logical operator and is used to reverse conditional statements
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")

# Nested If
# You can have if statements inside if statements, this is called nested if statements.

x = 41
if x > 10:
    print("Above 10, ")
if x > 20:
    print("and also above 20")
else: 
    print("but not above 20")

# The pass Statement
# if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
a = 33
b = 200
if b > a:
    pass


# Python has two primitive loop commands:
# while loops
# for loops

# The while Loop
i = 1
while i < 6:
    print(i)
    i += 1

# The break Statement
# With the break statement we can stop the loop even if the while condition is true
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

# The continue Statement
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

# The else Statement
i = 1
while i < 6:
    print(i)
    i += 1
else: 
    print("i is no longer than 6")


# Python For Loops
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

# Looping Through a String
fruits = ["apple", "banana", "cherry"]
for x in "banana":
    print(x)

# The break Statement in python array looping
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana": 
      break

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x) #example of break statement where break comes before print

# The continue Statement in python array looping
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x) # output wont show banana 

# The range() Function
for x in range(6):
    print(x)

for x in range(2, 6):
    print(x)

for x in range(2, 30, 3):
    print(x) # starts from 2 prints till 29 +ing 3 to 2

# Else in For Loop
for x in range(6):
    print(x)
else:
    print("finally finished")

for x in range(6):
    if x == 3: break
    print(x) 
else: 
    print("finally finished")

# Nested Loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
    for y in fruits:
        print(x, "-", y)

# The pass Statement
for x  in [0, 1, 2]:
    pass


# Python Functions
# A function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.

# In Python a function is defined using the def keyword
def my_function():
    print("hello function")
my_function()  # you have top call a function to print a function

# Arguments
# Information can be passed into functions as arguments.
# Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.
# The following example has a function with one argument (fname). When the function is called, we pass along a first name, which is used inside the function to print the full name

def my_function(fname):
    print(fname + " Refsnes")
my_function("Emil")
my_function("Tobias")
my_function("Linus")


# Parameters or Arguments?
# The terms parameter and argument can be used for the same thing: information that are passed into a function

# From a function's perspective:
# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the value that is sent to the function when it is called.

# Number of Arguments
def my_function(fname, lname):
  print(fname + " " + lname)
my_function("Ayushman","Mishra")

# Arbitrary Arguments, *args
def my_function(*kids):
    print("The youngest child is " + kids[2])
my_function("Ram", "Shyam", "Mayan")

# Keyword Arguments
def my_function(child3, child2, child1):
  print("The eldest child is " + child1)
my_function(child1 = "Ram", child2 = "Shyam", child3 = "Mayan")

# Arbitrary Keyword Arguments, **kwargs
# If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition

def my_function(**kid):
  print("His last name is " + kid["lname"])
my_function(fname = "Ayushman", lname = "Mishra")


# Default Parameter Value
def my_function(country = "India"):
    print("I am from " + country)
my_function("Sweden")
my_function("United States")
my_function()
my_function("Brazil")

# Passing a List as an Argument
# You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.

def my_function(food):
    for x in food:
      print(x)
fruits = ["apple", "banana", "cherry"]
my_function(fruits)

# Return Values
def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(5))
print(my_function(9))

# The pass Statement {used when fucntion cannot be left empty}
def myfunction():
  pass

'''
# Recursion
Python also accepts function recursion, which means a defined function can call itself.
Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.
The developer should be very careful with recursion as it can be quite easy to slip into writing a function which never terminates, or one that uses excess amounts of memory or processor power. However, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming.
'''

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result
print("\n\nRecursion Example Results")
tri_recursion(6)


# Python Lambda
# A lambda function is a small anonymous function.
#A lambda function can take any number of arguments, but can only have one expression.
# lambda arguments : expression

x = lambda a : a + 10
print(x(5))

x = lambda a, b : a * b 
print(x(5, 6))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

# Why Use Lambda Functions?
# The power of lambda is better shown when you use them as an anonymous function inside another function.

def myfunc(n):
    return lambda a : a * n 
mydoubler = myfunc(2)
print(mydoubler(11))

def myfunc(n):
    return lambda a : a * n 
mytripler = myfunc(3)
print(mytripler(11))

def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
mytripler = myfunc(3)
print(mydoubler(11))
print(mytripler(11))

# What is an Array?
# An array is a special variable, which can hold more than one value at a time.
# If you have a list of items (a list of car names, for example), storing the cars in single variables could look like this:
# car1 = "Ford"
# car2 = "Volvo"
# car3 = "BMW"
# However, what if you want to loop through the cars and find a specific one? And what if you had not 3 cars, but 300?
# The solution is an array!
# An array can hold many values under a single name, and you can access the values by referring to an index number.

cars = ["Ford", "Volvo", "BMW"]
x = cars[0]
print(x)

cars = ["Ford", "Volvo", "BMW"]
cars[0] = "Audi"
print(cars)

cars = ["Ford", "Volvo", "BMW"]
x = len(cars)
print(x)

# Looping Array Elements
cars = ["Ford", "Volvo", "BMW"]
for x in cars:
  print(x)

# Adding Array Elements
cars = ["Ford", "Volvo", "BMW"]
cars.append("Honda")
print(cars)

# Removing Array Elements
cars = ["Ford", "Volvo", "BMW"]
cars.pop(1)
print(cars)

cars = ["Ford", "Volvo", "BMW"]
cars.remove("Ford")
print(cars)



# Python Classes and Objects
class MyClass:
    x = 5
print(MyClass)

p1 = MyClass()
print(p1.x)

# The __init__() Function
# The examples above are classes and objects in their simplest form, and are not really useful in real life applications.
# To understand the meaning of classes we have to understand the built-in __init__() function.
# All classes have a function called __init__(), which is always executed when the class is being initiated.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person("John", 36)
print(p1.name)
print(p1.age)
print(p1.name + " age is " + str(p1.age)) #tried to use str 


# The __str__() Function
# The __str__() function controls what should be returned when the class object is represented as a string.

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
p1 = Person("John", 36)
print(p1)   #without using __str__()

# with __str__()
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        def __str__(self):
            return f"{self.name}({self.age})"
p1 = Person("John",36)
print(p1)


# Object Methods
# Objects can also contain methods. Methods in objects are functions that belong to the object.

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def myfunc(self):
    print("hello my name is " + self.name)
p1 = Person("John", 36)
p1.myfunc()


# The self Parameter
# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

print("The self Parameter")