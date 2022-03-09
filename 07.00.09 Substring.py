#recall use of indices in a string
#if a slice is called with two parameters s[a:b]
#   it returns substring length of b-a, starting w/ character at index a and ends w/ character at index b, not inclusive
#can mix positive and negative indices in same slice

s = 'Hello'
print(s[1:4])
print(s[-4:-1])
print(s[1:-1])