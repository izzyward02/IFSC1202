#given and int 'n', print sum of: 1! + 2! + 3! +...+ N!
#problem's solution is only one loop (don't use math library)
n = int(input("Enter N: "))
factSum = 0
factorial = 1
for n in range(1, n + 1):
    factorial *= n
    factSum += factorial
print("Sum of Factorials: {}".format(factSum))
