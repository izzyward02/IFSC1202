#prompt for a sequence of nums, last being zero
pNum = 0
cNum = 1
count = 0
maxNum = 0
newMaxNum = None
#print the max number of consecutive equal elements
#if two values repeat the same num of times, display the first recorded duplicates
while cNum > 0:
    cNum = int(input("Enter a Number (zero to quit): "))
    if cNum > 0:
        if count == 0:
            pNum = cNum
            count = 1
        else:
            if cNum == pNum:
                count += 1
                newMaxNum = cNum
                cNum = pNum
            else:
                if pNum > cNum:
                    newMaxNum = pNum
        pNum = cNum
print("{} repeated {} times".format(newMaxNum, count))
