#prompt for a sequence of nums, the last num being zero
numSum = 0
n = 1
while n > 0:
    n = int(input("Enter a Number (zero to quit): "))
    if n > 0:
        numSum += n
print(numSum)
