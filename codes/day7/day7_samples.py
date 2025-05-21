# Pythonic Code

# Create a List of squares
# squares = [ x**2 for x in range(10)]
# print(squares)

# Filter Even number
# evens = [ x for x in range(100) if x % 2 == 0 ]
# print(evens)

# Filter Odd number
#odds = [ x for x in range(100) if x % 2 != 0 ]
#print(odds)

# lambda arguments: expression

#add = lambda x, y : x + y 

#print(3, 5) 

# map functions

#numbers = [1, 2, 3, 4]

#squares = map(lambda x: x**2, numbers)

#print(list(squares))

# filter functions

#numbers = [1, 2, 3, 4]

#evenList = filter(lambda x: x%2 == 0, numbers)

#print(list(evenList))

# reduce functions

#from functools import reduce

#numbers = [1, 2, 3, 4]

#product = reduce(lambda x,y: x*y , numbers)

#print(product)


import sys

print(sys.argv)
print(sys.version)