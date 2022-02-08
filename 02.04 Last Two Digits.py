#input num > 0
num = int(input("Enter a Number: "))
#print last two digits (use .format() and math)
lastTwo = num%100
print("Last Two Digits: {}".format(lastTwo))