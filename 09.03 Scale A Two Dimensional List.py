#create function "print_list(a)" where a is a two dimensional list
#   function should print list row by row w/ spaces in between each element
def print_list(a):
    for b in range(len(a)):
        for c in range(len(a[b])):
            print(a[b][c], end = " ")
#create function "scale_list(a,s)" that multiplies every value in list by scale factor, where... 
#   a is two dimensional list
#   s is scale factor
def scale_list(a, s):
    for b in range(len(a)):
        for c in range(len(a[b])):
            a[b][c] = int(a[b][c]) * s
    return a
#read values in file "09.03 NumbersList.txt" into two dimensional array
read = open("09.03 NumbersList.txt")
numList = []

for line in read:
    r = line.split()
    numList.append(r)
#print list by calling print_list(a)
print_list(numList)
#prompt for scale factor
user = int(input("Enter scale value: "))
#multiply every value in list by scale factor using function scaled_list(a,s)
scale = scale_list(numList, user)
#print scaled list by calling print_list(a)
print_list(scale)

#EXAMPLE OUTPUT:

#11 12 
#21 22 23 
#31 32 33 34 
#Enter scale value: 2
#22 24 
#42 44 46 
#62 64 66 68