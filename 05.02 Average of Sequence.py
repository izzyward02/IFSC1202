#prompt for a sequence of nums, the last num being zero
n = int(input("Enter a Number (zero to quit): "))
numSum = 0
count = 0
while n > 0:
    numSum += n
    count += 1
    n  = float(input("Enter a Number (zero to quit): "))
if count != 0:
    avg = numSum / count
    print("Average: {}".format(avg))
else:
    print("Sequence Length is 0")
#print the average of the nums
#   "Average: " <-- should be a float
#if no data is entered (only a zero was given), generate an error (division by zero)
#   if input is zero, print...
#   "Sequence Length is 0"