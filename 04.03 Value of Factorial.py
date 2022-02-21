#the factorial of an int 'n' is denoted by 'n!' 
#   gives product 'n! = 1 * 2 *...*n'
#for given int 'n' calculate value of n! (don't use math module)
num = int(input("Enter Number: "))
factorial = 1
#print factorial of 'n' 
for num in range(1, num + 1):
    factorial *= num
#print sum of cubes of 'n' 
print("Factorial: {}".format(factorial))