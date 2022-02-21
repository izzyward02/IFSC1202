#prompt for a sequence of nums, the last num being zero
n = 1.0
numSum = 0
avg = 0
while n > 0:
    n  = float(input("Enter a Number (zero to quit): "))
    if n > 0:
        numSum += n
    elif numSum != 0: 
        avg = numSum / n    #error here: float division by zero
        print("Average: {}".format(avg))
    else:
        print("Sequence Length is 0")
#print the average of the nums
#   "Average: " <-- should be a float
#if no data is entered (only a zero was given), generate an error (division by zero)
#   if input is zero, print...
#   "Sequence Length is 0"