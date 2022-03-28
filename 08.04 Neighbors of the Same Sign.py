#prompt for a string containing ints separated by spaces
x = input("Enter Values Separated by Spaces: ")
#load values into a list
a = x.split()
#find and print the first adjacent elements with the same sign
#if there isn't a pair, leave output blank
#don't use list or string functions or methods (except .split() method)
#don't use the "for x in y" iterator; use "for x in range(n)"
for i in range(1, len(a)):
    if(int(a[i]) >= 0 and int(a[i - 1]) >= 0) or int(a[i] < 0 and int(a[i- 1]) < 0):    #problem here
        print(a[i])

#NOT DONE

#EXAMPLE OUTPUT:

#Enter Values Separated by Spaces: -1 2 3 -1 -2
#2 3
#-1 -2