#prompt for a string containing ints separated by spaces
user = input("Enter Values Separated by Spaces: ")
#load values into a list
values = user.split()
count = 0
#find and print elements that appear in list only once (elements must be printed in order in which they occur in original list)
#don't use list or string functions or methods (except .split() method)
#don't use "for x in y" iterator; use "for x in range(n)"
#HINT: loop through each element of list, them loop through list to look for a match
#   don't match element to itself
for i in range(len(values)):
    for j in range(len(values)):
        if i != j and values[i] == values[j]:
            break
    else:
        print(values[i], sep = " ", end = " ")
print()
print("Unique Elements: ", end = " ")
