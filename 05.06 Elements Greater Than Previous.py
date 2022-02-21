#prompt for a sequence of nums, last num being zero
pNum = int(input("Enter a Number (zero to quit): "))
count = 0
# #print how many elements in the sequence are greater than the previously inputted number
while pNum > 0:
    n = int(input("Enter a Number (zero to quit): "))
    if n > 0 and pNum < n:
        count += 1
    pNum = n
print("Number of Values Greater Than Previous: {}".format(count))
