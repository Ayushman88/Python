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
