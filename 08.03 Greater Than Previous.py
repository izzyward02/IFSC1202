#prompt for a string containing ints separated by spaces
x = input("Enter Values Separated by Spaces: ")
#load values into a list
a = x.split()
#print all elements that are greater than previous element
#don't use list or string functions or methods (except the .split() method)
#don't use the "for x in y" iterator; use "for x in range(n)"
for i in range(1, len(a)):
    if int(a[i]) > int(a[i - 1]):
        print(a[i])
