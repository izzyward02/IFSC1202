#prompt for a sequence of nums, last num being zero
n = int(input("Enter a Number (zero to quit): "))
evenNums = 0
while n > 0:
    if n % 2 == 0:
        evenNums += 1
    n = int(input("Enter a Number (zero to quit): "))
#print the number of even values in the sequence
print("Number of Even Values: {}".format(evenNums))
