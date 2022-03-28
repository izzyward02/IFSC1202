#prompt for a string containing ints separated by spaces
user = input("Enter Values Separated by Spaces: ")
#load values into a list
values = user.split()
#determine element in list with largest value
maxIndex = 0
#print value of largest element and then index number
#   if highest element is not unique (more than one occurrence), print index of first instance
#don't use list or string functions or methods (except .split() method)
#don't use the "for x in y" iterator; use "for x in range(n)"
for i in range(1, len(values)):
    if int(values[i]) > int(values[maxIndex]):
        maxIndex = i

print("Largest Value: {}".format(values[maxIndex]))
print("Index of Largest Value: {}".format(maxIndex))
