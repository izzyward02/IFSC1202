#input number
num = int(input("Enter a Number: "))
#print tens digit (use .format and math)
tens = (num//10)%10
print("Tens Digit: {}".format(tens))