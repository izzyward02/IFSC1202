#prompt for a sequence of nums, last being zero
pNum = int(input("Enter a Number (zero to quit): "))
count = 0
#print the max number of consecutive equal elements
#if two values repeat the same num of times, display the first recorded duplicates
while n > 0:
    n = int(input("Enter a Number (zero to quit): "))
    if pNum > 0 and pNum == n:
        count += 1
    n = pNum
print("{} repeated {} times".format(n, count))


#example sequence of 1, 7, 7, 9, 1, 0
#   "7 repeated 2 times"    <--didn't print 1 b/c the two instances were not consecutive