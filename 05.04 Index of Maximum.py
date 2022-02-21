#prompt for a sequence of nums, last num being zero
n = int(input("Enter a Number (zero to quit): "))
maxNum =  n
maxIndex = 1
index = 1

if n > 0:
    while n > 0:
        if n > maxNum:
            maxNum = n
            maxIndex = index
        n = int(input("Enter a Number (zero to quit): "))
        index += 1
else:
    maxIndex = 0
print("Maximum: {}".format(maxNum))
print("Index of Maximum: {}".format(maxIndex))
#print largest value & index of largest value in the sequence
