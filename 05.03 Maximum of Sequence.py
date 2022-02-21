#prompt for a sequence of nums, last num being zero
n = int(input("Enter a Number (zero to quit): "))
maxNum = n

while n > 0:
    if n > maxNum:
        maxNum = n
    n = int(input("Enter a Number (zero to quit): "))
print("Maximum: {}".format(maxNum))
