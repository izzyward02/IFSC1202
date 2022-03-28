#prompt for a string containing ints separated by spaces
user = input("Enter Values Separated by Spaces: ")
#load values into list
values = user.split()
#swap adjacent items in pairs (a[0] with a[1], a[2] with a[3], etc)
#print resulting list
#   if list has an odd nuym of elements, leave last element in place
#don't use list or string functions or methods (except .split() method)
#don't use "for x in y" iterator; use "for x in range(n)"
for i in range(1, len(values), 2):
    newNum = values[i]
    values[i] = values[i - 1]
    values[i - 1] = newNum
print("Swapped Values: ", end = "")

for i in range(len(values)):
    print(values[i], sep = " ", end = " ")
print()
