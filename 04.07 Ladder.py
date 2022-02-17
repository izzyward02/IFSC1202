#for given int 'n<=9' print a ladder of 'n' steps
#the 'k'th step consists of ints from 1-k without spaces in between
#use 'sep=' and 'end=' arguments of the print() function
#hint: use nested for loops
n = int(input("Enter N: "))
k = 1
for k in range(n, 10):
    for n in range(k):
        print(k, end='')
    print('')
#example input of N = 9 generates...
#   1
#   12
#   123
#   1234
#   12345
#   123456
#   1234567
#   12345678
#   123456789

#NOT DONE