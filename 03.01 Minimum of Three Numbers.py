#input three numbers
num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
num3 = int(input("Enter Third Number: "))
#cascade if-elif-else
if num1 > num2:
    print(num2)
elif num2 > num3:
    print(num3)
else:
    print(num1)