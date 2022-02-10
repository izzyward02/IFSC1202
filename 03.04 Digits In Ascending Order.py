#input three digit int
num = int(input("Enter a Number: "))
#put units in separate variables
hund = (num//100)%10
tens = (num//10)%10
ones = num%10
#print YES if in ascending order, NO if not
if hund < tens and tens < ones:
    print("YES")
else:
    print("NO")
