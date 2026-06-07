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
print("I am", 23, "years old").
"""
This is a multi 
line 
comment

"""
x=4
x="Train" #Variables datatype is overwritten

#type casting.

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
""".


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

x,y,z="Apple", "Orange", "Cheery"

x=y=z= "orange"
fruits=["apple","orange","banana"]
x,y,z=fruits

x="Awesome"
def myFnc():
    print("Python is ", x);
myFnc()

def func():
    global x    #Assigning a variale as ghlobal within a function
    x="Cheery"
func()

print(x).

"""
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
"""

""" 
Example	Data Type	
x = "Hello World"	str	
x = 20	int	
x = 20.5	float	
x = 1j	complex	
x = ["apple", "banana", "cherry"]	list	
x = ("apple", "banana", "cherry")	tuple	
x = range(6)	range	
x = {"name" : "John", "age" : 36}	dict	
x = {"apple", "banana", "cherry"}	set	
x = frozenset({"apple", "banana", "cherry"})	frozenset	
x = True	bool	
x = b"Hello"	bytes	
x = bytearray(5)	bytearray	
x = memoryview(bytes(5))	memoryview	
x = None	NoneType
""" 
a = "Hello, World"
print (a[1])

for x in "banana":
    print(x)

print(len(a))

txt = "The best things in life are free!"
print("free" in txt)
if "free" in txt:
  print("Yes, 'free' is present.")

print("expensive" not in txt)
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

b="Hello World"
print(b[2:7])
print(b[:5])
print(b[2:])
print(b[-5:-2])

a = "Hello, World!"
print(a.upper())

a = "Hello, World!"
print(a.lower())

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

a = "Hello, World!".
print(a.replace("H", "J"))

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!'].
