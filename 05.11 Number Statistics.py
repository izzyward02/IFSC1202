#prompt for a sequence of floats or ints, the last num being zero
num = float(input("Enter a Value (zero to quit): "))
maxNum = num
minNum = num
sumNum = 0.0
count = 0

while num > 0:
    sumNum += num
    count += 1
    if num < minNum:
        minNum = num
    if num > maxNum:
        maxNum = num
    num = float(input("Enter a Value (zero to quit): "))
#assume at least one num will be entered
#when zero is entered, display the count, sum, average, min, and max of the sequence
print("Count: {}".format(count))
print("Sum: {}".format(sumNum))
print("Average: {}".format(float(sumNum) / float(count)))
print("Minimum: {}".format(minNum))
print("Maximum: {}".format(maxNum))
