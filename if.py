# Grace Kelly 11-02-2018
# Source: https://docs.python.org/3/tutorial/controlflow.html#if-statements

x = int(input("Please enter an integer: "))
if x < 0:
  x = 0
  print('Negative changed to zero')
elif x == 0:
  print('Zero')
elif x == 1:
  print('Single')
else:
  print('More')
print("The final value of x is:", x)
