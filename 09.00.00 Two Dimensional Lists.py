#tasks can be stored in rectangular data table
#   these are called matrices or 2D arrays
#in Python, any table can be represented as a list of lists (where each element is its own list)

#program creates a numerical table w/ two rows & three columns then manipulates it:
#Example 1
a = [1, 2, 3, 4]
b = [5, 6]
c = [7, 8, 9]
d = []
d.append(a)
d.append(b)
d.append(c)
print (d)
print(d[0])
print(d[1])
print(d[2])
print(d[0][0])
print(d[0][1])
print(d[0][2])
print(d[0][3])
print(d[1][0])
print(d[1][1])
print(d[2][0])
print(d[2][1])
print(d[2][2])
d[0][0] = 10
d[0][1] = 11
d[0][2] = 12
d[0][3] = 13
print(d[0][0])
print(d[0][1])
print(d[0][2])
print(d)

#first elememt a[0] is a list of nums [1,2,3] & elements of the 2D array are:
a[0][0] == 1  
a[0][1] == 2  
a[0][2] == 3  
a[1][0] == 4  
a[1][1] == 5  
a[2][0] == 6  
a[2][1] == 7  
a[2][2] == 8
#NOTE: accessing a[1][2] gets an IndexOutOfRange error bc element DNE
