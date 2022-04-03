#to process 2D lists, typically use nested loops
#   first loop iterates through row num
#   second loop runs through elements inside a row
#   use len(a) for num of rows in array and len(a[i]) for num of elements in a row

a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()

#how to use two nested loops to calculate the sum of all nums in 2D list:

a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
s = 0
for i in range(len(a)):
    for j in range(len(a[i])):
        s += a[i][j]
print("The sum is: {}".format(s))
