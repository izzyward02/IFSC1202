#prime num is a natural num greater than 1 w/ no positive divisors other than 1 and itself
#given two ints A & B, print all prime nums between them, inclusively
#hint: copy code from 04.08 & modify so that 'n' varies from A to B
numA = int(input("Enter A: "))
numB = int(input("Enter B: "))
n = 0
if numA > 1:
    for n in range(2, (n//2) + 1):
        for n in range(numA, numB + 1):
            if (n % i) != 0:
                print(numA)



#example inputs of A = 2 and B = 10 generates...
#   2
#   3
#   5
#   7

#NOT DONE; PROBLEM: ONLY PRINTS FIRST INSTANCE OF PRIME NUMBER IN RANGE, DOES NOT CONTINUE