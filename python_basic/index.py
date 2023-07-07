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

x = 9
newlist = [x for x in range(10) if x<5]
print(newlist)