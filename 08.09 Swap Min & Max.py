#prompt for a string containing ints separated by spaces
user = input("Enter Values Separated by Spaces: ")
#load values into list
values = user.split()
#swap min and max elements in list
minIndex = 0
maxIndex = 0
#don't use list or string functions or methods (except .split() method)
#don't use "for x in y" iterator; use "for x in range(n)"
for i in range(1, len(values)):
    if int(values[i]) > int(values[maxIndex]):
        maxIndex = i
    if int(values[i]) < int(values[minIndex]):
        minIndex = i

values[minIndex], values[maxIndex] = values[maxIndex], values[minIndex]
print("Swapped Minimum and Maximum: ", end = "")

for i in range(len(values)):
    print(values[i], sep = " ", end = " ")
print()
