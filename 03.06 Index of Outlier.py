#input three ints, two same & one different
num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
num3 = int(input("Enter Third Number: "))
#print index of outlier (1, 2, or 3)
if num1 == num2:
    print(3)
elif num1 == num3:
    print(2)
else:
    print(1)