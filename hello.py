import sys
print(sys.version)
print("Hello, World!")
#command
a="apple"
b=1
print(a); print(b)
if(5>2):
    print("5 is greater than 2")
print("Same Line", end=" ")
print("Same line too")
print(2*5)
print("I am", 23, "years old")
"""
This is a multi 
line 
comment

"""
x=4
x="Train" #Variables datatype is overwritten

#type casting

x=str(3) #x is '3'
x=int(3) #x is 3
x=float(3) #x is 3.0

print(x)

print(type(x)) #print type of variable

#Python is case sensitive

"""
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.
"""


"""
Camel Case
Each word, except the first, starts with a capital letter:
myVariableName = "John"

Pascal Case
Each word starts with a capital letter:
MyVariableName = "John"

Snake Case
Each word is separated by an underscore character:
my_variable_name = "John"

"""