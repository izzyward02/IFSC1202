#for given int 'n<=9' print a ladder of 'n' steps
#the 'k'th step consists of ints from 1-k without spaces in between
#use 'sep=' and 'end=' arguments of the print() function
#hint: use nested for loops
n = int(input("Enter N: "))
k = 1
num = 1
for k in range(1, n + 1):
    for num in range(1, k + 1):
        print(num, end='')
    print()
