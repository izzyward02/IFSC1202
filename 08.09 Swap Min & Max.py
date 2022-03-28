#prompt for a string containing ints separated by spaces
#load values into list
#swap min and max elements in list
minIndex = 0
maxIndex = 0
#don't use list or string functions or methods (except .split() method)
#don't use "for x in y" iterator; use "for x in range(n)"
for i in range(1, len(a)):
    if int(a[i]) > int(a[maxIndex]):
        maxIndex = i
    if int(a[i]) < int(a[minIndex]):
        minIndex = i

#NOT DONE

#EXAMPLE OUTPUT:

#Enter Values Separated by Spaces: 3 4 5 2 1
#Swapped Minimum and Maximum: 3 4 1 2 5