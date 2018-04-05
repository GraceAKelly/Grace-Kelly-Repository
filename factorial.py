 Grace Kelly 18-03-18

#Function called factorial()
#That takes a single positive input  and returns its factorial
#Factorial is number multiplied by all positive integers less than it
#Call for values 5,7 and 10

def multiplyall(upto):
	factorial = 1
	for i in range (1, upto + 1):
		factorial = factorial * i
	return factorial
print("Factorial 5 is equal to:", multiplyall(5))
print("Factorial 7 is equal to:", multiplyall(7))
print("Factorial 10 is equal to:", multiplyall(10))

#Another way to calculate factorial
#in python 3
# Functions import reduce
# Stack overflow https://stackoverflow.com/questions/13840379/how-can-i-multiply-all-items-in-a-list-together-with-python
import operator
import functools
functools.reduce(operator.mul, [1,2,3,4,5], 1)

#operator.mul(a, b)
#operator.__mul__(a, b)
#Return a * b, for a and b numbers.

#reduce(function, iterable[, initializer])
#Apply function of two arguments cumulatively to the items of iterable, from left to right, so as to reduce the iterable to a single value.
# https://docs.python.org/2/library/functions.html#reduce

from functools import reduce
from operator import mul
x = reduce(mul, [1,2,3,4,5])
print("The multiplication of all items in list is:", x)
y = reduce(mul, [1,2,3,4,5,6,7])
print("The multiplication of all items in list is:", y)
z = reduce(mul, [1,2,3,4,5,6,7,8,9,10])
print("The multiplication of all items in list is:", z)
