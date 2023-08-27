# What are Functions?
# Functions are a convenient way to divide your code into useful blocks, allowing us to order our code, make it more readable, reuse it and save some time. Also functions are a key way to define interfaces so programmers can share their code.

# How do you write functions in Python?
# As we have seen on previous tutorials, Python makes use of blocks.

# A block is a area of code of written in the format of:

# Where a block line is more Python code (even another block), and the block head is of the following format: block_keyword block_name(argument1,argument2, ...) Block keywords you already know are "if", "for", and "while".

# Functions in python are defined using the block keyword "def", followed with the function's name as the block's name. For example:

def my_function():
    print("Hello from my function!")

# Functions may also receive arguments(variables passed from the caller to the function). For example:
def my_function_with_args(username, greeting):
    print("Hello, %s , From my Function!, I wish you %s"% (username, greeting))

# Functions may return a value to the caller, using the keyword - 'return'. for example:
def sum_two_numbers(a, b):
    return a + b

# How do you call functions in Python?
# Simply write the function's name followed by (), placing any required arguments within the brackets. For example, lets call the functions written above (in the previous example):
# Define our 3 functions
def my_function():
    print("Hello From My Function!")

def my_function_with_args(username, greeting):
    print("Hello, %s, From My Function!, I wish you %s"%(username, greeting))

def sum_two_numbers(a, b):
    return a + b

# print(a simple greeting)
my_function()

#prints - "Hello, John Doe, From My Function!, I wish you a great year!"
my_function_with_args("John Doe", "a great year!")

# after this line x will hold the value 3!
x = sum_two_numbers(1,2)





