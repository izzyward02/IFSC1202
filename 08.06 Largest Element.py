#prompt for a string containing ints separated by spaces
#load values into a list
a = x.split()
#determine element in list with largest value
maxIndex = 0
#print value of largest element and then index number
#   if highest element is not unique (more than one occurrence), print index of first instance
#don't use list or string functions or methods (except .split() method)
#don't use the "for x in y" iterator; use "for x in range(n)"
for i in range(1, len(a)):
    if int(a[i]) > int(a[maxIndex]):
        maxIndex = i    #NOT DONE

#EXAMPLE OUTPUT:

#Enter Values Separated by Spaces: 1 2 3 2 1
#Largest Value: 3
#Index of Largest Value: 2