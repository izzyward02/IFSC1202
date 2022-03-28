#prompt for a string containing ints separated by spaces
x = input("Enter Values Separated by Spaces: ")
#load values into a list
a = x.split()
#print values with an odd index number (a[1], a[3], a[5]...)
#don't use list or string functions or methods (except .spit() method)
#don't use the "for x in y" iterator; use "for x in range(n)"
for i in range(1, len(a), 2):
    print(a[i])
