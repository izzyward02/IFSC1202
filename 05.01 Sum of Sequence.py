#prompt for a sequence of nums, the last num being zero
numSum = 0
n = int(input("Enter a Number (zero to quit): "))
while n > 0:
    numSum += n
    n = int(input("Enter a Number (zero to quit): "))
print("Sum: {}".format(numSum))
