#if index in slice s[i] is greater than or equal to len(s)
#   or less than -len(s), the following error occurs:
#       IndexError: string index out of range

s = "Good Morning"
print(len(s))
# The last character is the length of the string minus 1
last = len(s) - 1
print(last)
print(s[last])

