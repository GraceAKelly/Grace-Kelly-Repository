#Grace Kelly 11-02-2018
#Week 3 Assesment 

num = int(input("Please Enter Integer:")) # Enter number to be tested
while num!=1: # Number is not equal to 1
    if num % 2 == 0: # If the remainder of dividing by 2 is 0 
        num = num/2 # If it is even divide by 2
        print (num) # Print the output 
    else: # Or Else if it is not even 
        num = (num * 3) + 1 # Multiply the number by 3
        print (num) #Print the output
