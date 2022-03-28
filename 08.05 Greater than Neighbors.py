#prompt for a string containing ints separated by spaces
x = input("Enter Values Separated by Spaces: ")
#load values into a list
a = x.split()
#determine & print quantity of elements that are greater than both neighbors
#   the first and last items shouldn't be considered 
#don't use list or string functions or methods (except .split() method)
#don't use the "for x in y" iterator; use "for x in range(n)"
#for i in range(, len(a) - 1):
 #   if int(a[i]) > int(a[i - 1])
#NOT DONE

#EXAMPLE OUTPUT:

#Enter Values Separated by Spaces: 1 5 1 5 1
#Example Output
#2