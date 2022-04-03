#give two ints for rows & columns (m*n) & subsequent m rows of n elements
#   input num of rows and columns in list
user = input("Enter the number of rows and columns: ")
numList = user.split()
#   input array
row = int(numList[0])
column = numList[1]
#   print array
numTable = []
#   find index pos of max element & print two nums representing index (i*j)
#       or row num and column num
#       if multiple elements in diff rows, print one with smaller row num
#       if multiple elements on same row, print smallest column num
for i in range(row):
    row = input(f"Row {i + 1}: Enter {column} values separated by spaces: ")
    rowNums = row.split()
    numTable.append(rowNums)
for i in range(len(numTable)):
    for j in range(len(numTable[i])):
        print(numTable[i][j], end = " ")
    print()

maxNum = 0
c = 1
r = 1

for i in range(len(numTable)):
    for j in range(len(numTable[i])):
        if maxNum < int(numTable[i][j]):
            maxNum = int(numTable[i][j])
            maxColumn = c
            maxRow = r
        r += 1
    c += 1
    r = 1

print("The maximum value {} occurred in row {} column {}".format(maxNum, maxRow, maxColumn))
