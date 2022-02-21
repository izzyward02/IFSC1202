#prime num is a natural num greater than 1 w/ no positive divisors other than 1 and itself
#given two ints A & B, print all prime nums between them, inclusively
#hint: copy code from 04.08 & modify so that 'n' varies from A to B
numA = int(input("Enter A: "))
numB = int(input("Enter B: "))
for n in range(numA, numB + 1):
    prime = True
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            prime = False
    if prime:
        print(n)
