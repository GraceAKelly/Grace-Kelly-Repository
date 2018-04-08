# Grace Kelly 11-02-2018
# Source: https://docs.python.org/3/tutorial/controlflow.html#if-statements

x = int(input("Please enter an integer: "))
if x < 0: # if statement if x is less than zero
  x = 0 # x is equal to zero, one = sign is defining character
  print('Negative changed to zero') # output if x is less than zero
elif x == 0: # two equal sign is testing character, test else if above not true test if x is equal to zero
  print('Zero')
elif x == 1: # test else if x is equal to one if abpove statements are not true
  print('Single')
else: # or else print 
  print('More')
print("The final value of x is:", x)
