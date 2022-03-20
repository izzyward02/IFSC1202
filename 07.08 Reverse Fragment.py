#prompt for .coma string co ntaining letter "h" at least twice
s = input("Enter a string: ")
#reverse sequence of characters between first "h" and last "h"
hPrev = s[:s.find("h")]
hBetween = s[s.find("h"):s.rfind("h") + 1]
hAfter = s[s.rfind("h") + 1:]
revHBetween = hBetween[::-1]
rev = hPrev + revHBetween + hAfter
#print result
print(rev)
 