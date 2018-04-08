 Grace Kelly 18-03-18

#Function called factorial()
#That takes a single positive input  and returns its factorial
#Factorial is number multiplied by all positive integers less than it
#Call for values 5,7 and 10

def multiplyall(upto): # multiplies all integers in list up to number specified
	factorial = 1 # first number in range
	for i in range (1, upto + 1): # Define range to be 1 upto nuber specified as upto in line 8 plus 1 
		factorial = factorial * i # Change definition of factorial to be 1 multiplied by i in range in line 10 
	return factorial # Output 
print("Factorial 5 is equal to:", multiplyall(5)) # Print 5 mulitiplied by all positive integers less than it
print("Factorial 7 is equal to:", multiplyall(7)) # Print 7 mulitiplied by all positive integers less than it
print("Factorial 10 is equal to:", multiplyall(10)) # Print 10 mulitiplied by all positive integers less than it

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

from functools import reduce # Reduce function Applies the two arguement function to successive items from iterable (taking each item of one after another, any time you use a loop you go over a group of items)
from operator import mul # multiplication function
x = reduce(mul, [1,2,3,4,5]) # reduce loop the items in the list and mul multiply them 
print("The multiplication of all items in list is:", x) # print output of x list is up to 5
y = reduce(mul, [1,2,3,4,5,6,7]) # reduce loop the items in the list and mul multiply them 
print("The multiplication of all items in list is:", y) # print output of y list is up to 7
z = reduce(mul, [1,2,3,4,5,6,7,8,9,10]) # reduce loop the items in the list and mul multiply them 
print("The multiplication of all items in list is:", z) # print output of z list is up to 10
