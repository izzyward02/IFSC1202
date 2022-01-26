#mult. returns int, div. returns float
print(17 / 3)   #gives 5.6666666667
print(2 ** 4)   #gives 16
print(2 ** -2)  #gives 0.25
#various division types
print(17 / 3)   #gives 5.6666666667
print(17 // 3)  #gives 5
print(17 % 3)   #gives 2
#using int() function
print(int(1.3))     #gives 1
print(int(1.7))     #gives 1
print(int(-1.3))    #gives -1
print(int(-1.7))    #gives -1
#using round() function
print(round(1.3))   #gives 1
print(round(1.7))   #gives 2
print(round(-1.3))  #gives -1
print(round(-1.7))  #gives -2
#using round() to specify decimal points
print(round(3.14159, 2))    #gives 3.14
print(round(3.14159, 3))    #gives 3.142
print(round(3.14159, 4))    #gives 3.1416
#floating-point nums can't be precise
print(0.1 + 0.2)    #gives 0.30000000000000000004
#using import & math
import math
from math import ceil
x = 7 / 2
y = ceil(x)
print(y)