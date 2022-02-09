#input four digit num
num = int(input("Enter a Number: "))
#put units in separate variables
thous = num%1000
hund = num%100
tens = num%10
ones = num%1
#print YES if palindrome, NO if not
