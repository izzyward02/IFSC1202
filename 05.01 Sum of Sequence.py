#prompt for a sequence of nums, the last num being zero
num = int(input("Enter a Number (zero to quit): "))
numSum = 0 
while num > 0: 
    numSum += num 
    int(input("Enter a Number (zero to quit): "))
else:
    numSum += 0    
print(numSum)
