#for given int 'n' calculate sum of cubes of each num from 1 to 'n' 
num = int(input("Enter Number: "))
cubeSum = 0
for num in range(1, num + 1):
    cubeSum += num**3
#print sum of cubes of 'n' 
print(cubeSum)