#Grace Kelly 11-02-2018
#Week 3 Assesment 

num = int(input("Please Enter Integer:")) # Enter number to be tested
while num!=1: # Number is not equal to 1
    if num % 2 == 0: # If the remainder of dividing by 2 is 0 
        num = num/2 
        print (num)
    else:
        num = (num * 3) + 1
        print (num) 
