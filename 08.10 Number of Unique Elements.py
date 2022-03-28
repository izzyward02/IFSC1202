#prompt for a string containing ints separated by spaces
x = input("Enter Values Separated by Spaces: ")
#load values into a list
a = x.split()
count = 0
print("Unique Elements: ", end=" ")
#find and print elements that appear in list only once (elements must be printed in order in which they occur in original list)
#don't use list or string functions or methods (except .split() method)
#don't use "for x in y" iterator; use "for x in range(n)"
#HINT: loop through each element of list, them loop through list to look for a match
#   don't match element to itself
for i in range(len(a)):
    for j in range(len(a)):
        if i != j and a[i] == a[j]:
            break
    else:
        print(a[i], sep=" ", end=" ")
print()
#SYNTAX ERROR SOMEWHERE


#EXAMPLE OUTPUT:

#Enter Values Separated by Spaces: 4 3 5 2 5 1 3 5
#Unique Elements: 4 2 1