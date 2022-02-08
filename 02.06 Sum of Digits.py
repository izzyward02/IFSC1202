#input three digit num
num = int(input("Enter a 3 Digit Number: "))
#print sum of digits (use .format() and math)
digitSum = (num//100)%10 + (num//10)%10 + num%10
print("Sum of Digits: {}".format(digitSum))