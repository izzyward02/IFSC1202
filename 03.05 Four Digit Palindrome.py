#input four digit num
num = int(input("Enter a Number: "))
#put units in separate variables
thous = (num//1000)%10
hund = (num//100)%10
tens = (num//10)%10
ones = num%10
#print YES if palindrome, NO if not
if thous == ones and hund == tens:
    print("YES")
else:
    print("NO")