#given two ints A and B, print squares of all ints between them, inclusively
#print formula as shown
#no spaces around * and =
#use either 'sep=' argument of print() statement or .format() method
numA = int(input("Enter A: "))
numB = int(input("Enter B: "))
square = 0
for numA in range(numA, numB + 1):
    square = numA * numA
    print("{}*{}={}".format(numA, numA, square))
    numA += 1
