# Grace Kelly 060218
# Fizzbuzz wikipedia

i = 1

while i <=100: # while i is less than or equal to zero
  if (i % 3 == 0) and (i % 5 == 0): # if the remainder or dividing by 3 is 0 and the remainder of dividing by 5 is zero
    print("FizzBuzz") # if both statements are true print 'fizzbuzz'
  elif i % 3 == 0: # or else if both of those functions are not true and i is only divisable by 3 print 'fizz'
    print ("fizz")
  elif i % 5 == 0: # or else if both of those functions are not true and i is only divisable by 5 print 'buzz'
    print ("buzz")
  else: # if none of those statements are true and number is not divisable by 3 or 5 print the number
    print (i)
  i = i + 1
