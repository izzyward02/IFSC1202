#find() w/ three arguments: s.find(substring, left, right)
#   performs search inside s[left:right] slice
#   returns absolute index (index in whole string s, not in the slice)
#find() w/ two arguments: s.find(substring, left)
#   performs search in slice s[left:], starting w/ character at index left until end of string

s = 'my name is bond, james bond, okay?'
print(s.find('bond'))
print(s.find('bond', 12))
