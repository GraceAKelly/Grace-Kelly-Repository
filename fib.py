#Grace Kelly 30-01-2018
# Week 1 exercise My name is Grace, so the first and last letter of my name (G + E = 7 + 5) give the number 12. 
# The 12th Fibonacci number is 144
# Week 2 exercise: My surname is Kelly The first letter K is number 75 
# The last letter y is number 121 Fibonacci number 196 is 40934782466626840596168752972961528246147
# ord() is a built in function in python that returns the unique numeric value assigned in unicode for the given character input


def fib(n):
  """This function returns the nth Fibonacci number."""
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    n = n - 1
  
  return i

name = "Kelly"
first = name[0]
last = name[-1]
firstno = ord(first)
lastno = ord(last)
x = firstno + lastno

ans = fib(x)
print("My surname is", name)
print("The first letter", first, "is number", firstno)
print("The last letter", last, "is number", lastno)
print("Fibonacci number", x, "is", ans)
