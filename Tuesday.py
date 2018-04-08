# Grace Kelly 06-02-18
# Week 3 is it Tuesday

import datetime # functions to loop and determine if the day of the week is Tuesday

if datetime.datetime.today().weekday() == 1: # Tuesday is eqaul to 1 in python
  print("yay! It is Tuesday") # output if it is true today is Tuesday
else:
  print("unfortunetly it is not Tuesday") # output if it is false today i snot Tuesday
