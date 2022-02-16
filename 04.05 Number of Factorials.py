#given and int 'n', print sum of: 1! + 2! + 3! +...+ N!
#problem's solution is only one loop (don't use math library)
n = int(input("Enter N: "))
factSum = 0
for n in range(1, n + 1):
    factSum += n*n
print("Sum of Factorials: {}".format(factSum))

#input n = 4 generates factSum = 30, when it should be 33? ***prob may be on line 6