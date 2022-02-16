#input num for 'n' 
n = int(input("Enter N: "))
for i in range(n):
    int(input("Enter a Number: "))
product = 1
#read 'n' and print their product
for i in range(1, n + 1):
    product *= i
#print product of all inputted ints
print(product)