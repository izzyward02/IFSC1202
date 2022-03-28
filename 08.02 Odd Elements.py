#prompt for a string containing ints separated by spaces
x = input("Enter Values Separated by Spaces: ")
#load values into a list
a = x.split()
#print values that are odd
#don't use list or string functions or methods (except .split() method)
#don't use the "for x in y" iterator; use "for x in range(n)"
for i in range(len(a)):
    if int(a[i]) %  2 == 1:
        print(a[i])
