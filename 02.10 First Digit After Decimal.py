#input pos real num
num = float(input("Enter Number: "))
#print first digit to right of decimal
tenthsNum = int((num*10)%10)
print("Tenths Value: {}".format(tenthsNum))