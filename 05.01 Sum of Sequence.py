#prompt for a sequence of nums, the last num being zero
n = 0
for n in range(n, n + 1):
    while n > 0:
        int(input("Enter a Number (zero to quit): "))   
        n += n
    else: 
        print("Sum: {}".format(n))
