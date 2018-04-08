# Grace Kelly 21 March 2018
# https://github.com/ianmcloughlin/problems-python-fundamentals
# > compoundinterest(1000, 3, 5) 1159.27
# > compoundinterest(1000, 7, 10) 1967.15

def compoundinterest(p, r, n): # define the output
# Princial, Rate, Number of periods
# Loop over the periods.
for i in range(n): # For values of i range n
p = p + (p * (0.01 * r)) # Increase the principal based on inputted rates
return round(p, 2) # Round function to round off value of returned principal
print(compoundinterest(1000, 3, 5)) # Output 
print(compoundinterest(1000, 7, 10)) # Output 
