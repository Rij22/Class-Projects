print("Hello, World!")
if 5 > 2:
    print("Five is greater than 2")
if 10 < 12:
    print("Ten is less than Twelve")

x = 5
y = "Hello, World!"
# python has no command for declaring a variable
print("x + y ")
# this will still give us an output of x + y

# You can create comments either this way or by placing the comment in a tripple quote.
# example
""" This is a comment """ 

# creating variables
x = 5
y = "John"
print(x)
print(y)
""" x is of type int """
""" y is of type str """

# To make a variable x belong to the global scope
def myfunc():
    global x
    x = "fantastic"

# Casting 
x = str(3) # x will be '3'
y = int(3) # x will be '3'
z = float(3) # x will be 3.0

# Get the data type
x = 5
y = "John"
print(type(x))
print(type(y))

# Variable names. They can have short names or long names or descriptive name (age, girlname, boys name, mass, volume e.t.c.)
# Variable names are case sensitive. 
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# Camel case. Each word except the first starts with capital letter
myVariableName = "John"

# Pascal Case. Each word starts with a capital letter
MyVariableName = "John"

# Snake case. Each word is separated by a underscore.
my_variable_name = "John"

# It is possible to also assign multiple values to multiple variables
x, y, z = "Orange", "Apple", "Mango"
print(x)
print(y)
print(z)

# You can also assign the same value to multiple variables in one line
x = y = z = "Banana"
print(x)
print(y)
print(z)

# Unpacking is one way to extract values into variables.
carname = ["Toyata", "Hyundai", "Lexus"]
x, y, z = carname
print(x)
print(y)
print(z)

# Global variables can be used to create a variable inside/outside of a function
x = "awesome"
def myfunc1():
    print("I am " + x)
myfunc1()

y = "awesome"
def myfunc2():
    y = "fantastic"
    print("Rijaya is " + y)
myfunc2()
print("Rijaya is " + y)

import random
print(random.randrange(1, 10))

















