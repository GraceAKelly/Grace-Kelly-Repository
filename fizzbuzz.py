# Grace Kelly 060218
# Fizzbuzz wikipedia

i = 1

while i <=100:
  if (i % 3 == 0) and (i % 5 == 0):
    print("FizzBuzz")
  elif i % 3 == 0:
    print ("fizz")
  elif i % 5 == 0:
    print ("buzz")
  else:
    print (i)
  i = i + 1
