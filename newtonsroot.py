# Grace Kelly 21 March 2018
# Take a number x and return its square root correct to six decimal places
# > newtonsroot(100) 10.0
# > newtonsroot(144) 12.0
# https://github.com/ianmcloughlin/problems-python-fundamentals

def newtonsroot(x): # Define output
z = x / 2.0 # Make initial random guess. Try half of x.
n = z - ((z**2 - x)/(2 * z)) # Use formula to set next guess
while abs(z - n) >= 0.0000001: # Loop while the difference between z and n is six decimal places less than 0.000001
z = n
n = z - ((z**2 - x)/(2 * z))
return n
# Tests from question.
print(newtonsroot(100))
print(newtonsroot(144))
