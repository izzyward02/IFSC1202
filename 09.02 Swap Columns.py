#create function "print_list(a)" where a is two dimensional list
#   function should print list row by row w/ space in between elements
def print_list(a):
    for b in range(len(a)):
        for c in range(len(a[b])):
            print(a[b][c], end = " ")
        print()
#create function "swap_columns(a,i,j)" that swap columns i and j in list a where... 
#   a is a two dimensional list
#   i and j are nums of colummns to be swapped
def swap_columns(a,b,c):
    for d in range(len(a)):
        a[d][b], a[d][c] = a[d][c], a[d][b]
#read values in file "09.02 NumbersList.txt" into two dimensional list
a = []
numList = open("09.02 NumbersList.txt")
read = numList.readline()
#print list by calling print_list(a)
while read != "":
    split = read.split(" ")
    for b in range(len(split)):
        split[b] = int(split[b])
    a.append(split)
    read = numList.readline()
print_list(a)
#prompt for column number in list to swap by calling swap_columns(a,i,j)
#print list w/ swapped columns by calling print_list(a)
rcOut = input("Enter the columns to swap: ").split()
b = int(rcOut[0])
c = int(rcOut[1])
swap_columns(a, b, c)
print_list(a)

#EXAMPLE OUTPUT:

#11 12 13 14 15 16 
#21 22 23 24 25 26 
#31 32 33 34 35 36 
#41 42 43 44 45 46 
#Enter the columns to swap: 0 5
#16 12 13 14 15 11 
#26 22 23 24 25 21 
#36 32 33 34 35 31 
#46 42 43 44 45 41 