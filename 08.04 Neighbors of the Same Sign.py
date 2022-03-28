#prompt for a string containing ints separated by spaces
user = input("Enter Values Separated by Spaces: ")
#load values into a list
values = user.split()
#find and print the first adjacent elements with the same sign
#if there isn't a pair, leave output blank
#don't use list or string functions or methods (except .split() method)
#don't use the "for x in y" iterator; use "for x in range(n)"
for i in range(1, len(values)):
    if(int(values[i]) >= 0 and int(values[i - 1]) >= 0) or (int(values[i]) < 0 and int(values[i- 1]) < 0):
        print(values[i - 1] + " " + values[i])
