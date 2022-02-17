#prime num is a natural num greater than 1 w/ no positive divisors other than 1 and itself
#given int n>1, print PRIME if 'n' is prime and COMPOSITE otherwise
#hint: loop from 2 to (half of N) + 1 & check if any num evenly divides into N
n = int(input("Enter N: "))
if n > 1:
    for i in range(2, (n//2) + 1):
        if (n % i == 0):
            print("COMPOSITE")
            break
    else:
        print("PRIME")
else:
    print("COMPOSITE")
