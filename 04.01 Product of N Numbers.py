#input num for 'n' & print product
n = int(input("Enter N: "))
product = 1
for i in range(n):
    product *= int(input("Enter a Number: "))
print(product)