#input three ints
num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
num3 = int(input("Enter Third Number: "))
#how many ints are equal?
if num1 == num2 == num3:
    print(3)
elif num1 < num2 == num3:
    print(2)
elif num1 == num2 < num3:
    print(2)
else:
    print(0)
#WONT RUN