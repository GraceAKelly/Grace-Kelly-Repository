#Grace Kelly 07/03/2018
#Exercise 5

#Read iris data set
#Print out four numerical values
#Decimal places aligned
#Space between columns

with open("data/iris.csv") as f:
    for line in f:
        print(line.split(',') [:4])
