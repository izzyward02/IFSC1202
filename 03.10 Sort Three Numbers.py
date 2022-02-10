#input three ints
firstNum = int(input("Enter First Number: "))
secondNum = int(input("Enter Second Number: "))
thirdNum = int(input("Enter Third Number: "))
#print in ascending order
if firstNum <= secondNum and secondNum <= thirdNum:
    numOrder = [firstNum, secondNum, thirdNum]
elif secondNum <= thirdNum and thirdNum < firstNum:
    numOrder = [secondNum, thirdNum, firstNum]
elif firstNum <= thirdNum and thirdNum < secondNum:
    numOrder = [firstNum, thirdNum, secondNum]
elif secondNum <= firstNum and firstNum < thirdNum:
    numOrder = [secondNum, firstNum, thirdNum]
elif thirdNum <= firstNum and firstNum < secondNum:
    numOrder = [thirdNum, firstNum, secondNum]
else:
    numOrder = [thirdNum, secondNum, firstNum]
print(numOrder)