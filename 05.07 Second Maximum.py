#prompt for two nums
num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
sequenceNum = int(input("Enter a Number (zero to quit): "))
#prompt for a sequence, last num being zero
maxNum =  num1
nextMaxNum = num2

if sequenceNum > 0:
    while sequenceNum > 0:
        if sequenceNum > maxNum:
            nextMaxNum = maxNum
            maxNum = sequenceNum
        sequenceNum = int(input("Enter a Number (zero to quit): "))
else:
    maxNum = num1
    nextMaxNum = num2
print("First Maximum: {}".format(maxNum))
print("Second Maximum: {}".format(nextMaxNum))
