#slices w/ two parameters never cause IndexError
#   if second parameter was omitted but colon is preserved, then slice continues until end of a string
#   similarly, if first parameter is omitted then Python takes slice starting at beginning of a string
#   to remove last character from a string, use slice s[:-1]
#       this slice s[:] is equal to a string "s" itself

s = 'Hello'
print(s[1:5])    
print(s[1:100])  
print(s[1:])     
print(s[:-1])    
print(s[:])
