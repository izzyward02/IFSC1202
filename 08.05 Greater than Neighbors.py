#prompt for a string containing ints separated by spaces
user = input("Enter Values Separated by Spaces: ")
#load values into a list
values = user.split()
count = 0
#determine & print quantity of elements that are greater than both neighbors
#   the first and last items shouldn't be considered 
#don't use list or string functions or methods (except .split() method)
#don't use the "for x in y" iterator; use "for x in range(n)"
for i in range(1, len(values) - 1):
    if int(values[i]) > int(values[i + 1]) and int(values[i]) > int(values[i - 1]):
        count += 1
print(count)
