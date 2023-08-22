print("hello, world")
x = 1
if x == 1:
    # indented four spaces
    print("x is 1.")
    
# python variables
myfloat = 7.0
print(myfloat)
myfloat = float(7)
print(myfloat)

# Numbers in python
# when you want to define an integer, use the following syntax
myint = 23
print(myint)

# when you working with fload numbers, you may use the following syntax
myfloat = 7.0
print(myfloat)
myfloat = float(7)
print(myfloat)

# working with strings, you can define either with single quotes or double quotes
mystring = 'hello world'
print(mystring)
mystring = "Hello World"
print(mystring)

# The difference between the two is that using double quotes makes it easy to include apostrophes (whereas these would terminate the string if using single quotes)
mystring = "Dont worry about aposstrophes"
print(mystring)

# Exercise on variables
# The target of this exercise is to create a string, an integer, and a floating point number. The string should be named mystring and should contain the word "hello". The floating point number should be named myfloat and should contain the number 10.0, and the integer should be named myint and should contain the number 20.
mystring = "hello"
myfloat = 10.0
myint = 20

# Testing codes
if mystring == "hello":
    print("string: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)



