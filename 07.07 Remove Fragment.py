#prompt for a string containing letter "h" at least twice
s = input("Enter a string: ")
#in string, remove first and last occurrence of letter "h" and characters in between them
h1 = s.find("h")
hLast = s.rfind("h")
#print result
result = s[:h1] + s[hLast + 1:]
print(result)
