#prompt for a string containing ints separated by spaces
user = input("Enter Values Separated by Spaces: ")
#load values into a list
values = user.split()
#print all elements that are greater than previous element
#don't use list or string functions or methods (except the .split() method)
#don't use the "for x in y" iterator; use "for x in range(n)"
for i in range(1, len(values)):
    if int(values[i]) > int(values[i - 1]):
        print(values[i])
