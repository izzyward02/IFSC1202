#checks that number a is positive and number b is non-negative
#if a > 0 and not (b < 0):

#instead of "not (b<0)", write "(b>=0)"
a = int(input())
b = int(input())
if a > 0 and b >= 0:
# another suitable expression is
# if a > 0 and not b < 0:
    print('A is greater than 0 and B is greater than or equal to 0')
else:
    print('Either A is less then or equal to zero or B is less than 0')