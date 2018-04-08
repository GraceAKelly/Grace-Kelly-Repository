# Grace Kelly 10 March 2018
# https://github.com/ianmcloughlin/problems-python-fundamentals
# test > simpleinterest(1000, 3, 5) 1150.0
# test > simpleinterest(1000, 7, 10) 1700.0

def simpleinterest(p, r, n):
# Inputs principal, interest rate and a number of periods
i = p * (0.01 * r) # Intrest for one period
t = i * n # Interest for all periods
return round(p + t, 2) # Round function to round off value, return total interest
print(simpleinterest(1000, 3, 5)) #Output
print(simpleinterest(1000, 7, 10)) #Output
