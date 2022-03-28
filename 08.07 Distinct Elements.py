#prompt for a string containing ints separated by spaces
user = input("Enter Values Separated by Spaces: ")
#load values into a list
values = user.split()
#print num of disinct elements in list
distinctNum = 1
#don't use string or list functions or methods (except .split() method)
#don't use the "for x in y" iterator; use "for x in range(n)"
for i in range(0, len(values) - 1):
    if int(values[i]) != int(values[i + 1]):
        distinctNum += 1
print("Number of Distinct Elements: {}".format(distinctNum))
