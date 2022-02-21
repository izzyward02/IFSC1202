#prompt for a sequence of nums, the last num being zero
n = 0
while n > 0:
    int(input("Enter a Number (zero to quit): "))   
    n += n
else: 
    print("Sum: {}".format(n))
