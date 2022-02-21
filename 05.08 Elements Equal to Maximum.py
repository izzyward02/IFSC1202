#prompt for a sequence of nums, zero being last
n = int(input("Enter a Number (zero to quit): "))
maxNum = 1
#print max value of the sequence & number of times it occurs
while n > 0:
    n = int(input("Enter a Number (zero to quit): "))
    while n > maxNum:
        maxNum = n
        n = int(input("Enter a Number (zero to quit): "))
        if maxNum == n:
            i += 1
print("Maximum: {}".format(maxNum))
print("Number of Occurrences: {}".format(i))

#example sequence: 1, 2, 3, 2, 3, 3, 3, 0
#max = 3 and num of occurrences = 4
