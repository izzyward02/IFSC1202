#if a slice is specified with three parameters s[a:\b:d]
#   the third parameter specifies the step (similar to range())
#   only characters w/ indicies a, a+d, a+2*d, etc, until character w/ index b is reached, not inclusive
#if third parameter ==2, slice takes every second character
#   syntax: s[a:\b:2]
#if the step of the slices == -1, characters go in reverse order
#   syntax: s[::-1]

s = 'abcdefg'
print(s[1])
print(s[-1])
print(s[1:3])
print(s[1:-1])
print(s[:3])
print(s[2:])
print(s[:-1])
print(s[::2])
print(s[1::2])
print(s[::-1])

s = 'abcdefghijklm'
print(s[0:10:2])
for i in range(0, 10, 2):
    print(i, s[i])

