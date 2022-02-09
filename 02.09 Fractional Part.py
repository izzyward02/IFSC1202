#input pos real num
num = float(input("Enter a Number: "))
#round result to 10 digits
fracNum = num%1
round(fracNum, 10)
#print fractional part
print("Fractional Part: {}".format(fracNum))