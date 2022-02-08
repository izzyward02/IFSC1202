#digit input
num = int(input("Enter a Number: "))
#digit swap (use .format())
firstNum = num//10
secondNum = num%10
swappedNum = (secondNum*10)+firstNum
print("Swapped Number: {}".format(swappedNum))