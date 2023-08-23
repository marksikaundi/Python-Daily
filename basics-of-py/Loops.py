# There are two types of loops in Python, for and while.

# The "for" loop
# For loops iterate over a given sequence. Here is an example:
primes = [2, 3, 5]
for prime in primes:
    print(prime)

# For loops can iterate over a sequence of numbers using the "range" and "xrange" functions. The difference between range and xrange is that the range function returns a new list with numbers of that specified range, whereas xrange returns an iterator, which is more efficient. (Python 3 uses the range function, which acts like xrange). Note that the range function is zero based.
# Prints out the numbers 0, 1, 2, 3, 4
for x in range(3, 6):
    print(x)
    
# Prints out 3, 4, 5
for x in range(3, 6):
    print(x)
    
# Prints out 3,5,7
for x in range(3, 8, 2):
    print(x)









