#prompt for a sequence of nums, zero being last
maxNum = 0
i = 0
firstNum = True
#print max value of the sequence & number of times it occurs
while True:
    n = int(input("Enter a Number (zero to quit): "))
    if n == 0:  
        break
    if firstNum or maxNum < n:
        maxNum = n
        i = 1
    elif maxNum == n:
        i += 1
    firstNum = False
print("Maximum: {}".format(maxNum))
print("Number of Occurrences: {}".format(i))
