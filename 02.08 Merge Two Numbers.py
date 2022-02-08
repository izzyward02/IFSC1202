#input two nums, each two digits
firstNum = int(input("Enter First 2 Digit Number: "))
secondNum = int(input("Enter Second 2 Digit Number: "))
#merge in pattern: first ten, second ten, first one, second one
firstTen = (firstNum//10)%10
secondTen = (secondNum//10)%10
firstOne = firstNum%10
secondOne = secondNum%10
mergedNum = (firstTen*1000) + (secondTen*100) + (firstOne*10) + secondOne
print("Merged Number: {}".format(mergedNum))