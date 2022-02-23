#prompt for a sequence of nums, zero being last
n = int(input("Enter a Number (zero to quit): "))
i = 0
#print max value of the sequence & number of times it occurs
while i < n:
    value = n
    print (value)
    exit
    i += i
else:
     print("{} repeats {} times".format(n, i))
print()

#example sequence: 1, 2, 3, 2, 3, 3, 3, 0
#max = 3 and num of occurrences = 4
