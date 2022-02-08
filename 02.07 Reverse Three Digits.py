#input three digit number
num = int(input("Enter a 3 Digit Number: "))
#reverse the digits (use .format() and math)
hund = (num//100)%10
tens = (num//10)%10
ones = num%10
revNum = (ones*100) + (tens*10) + hund
print("Reverse of Digits: {}".format(revNum))