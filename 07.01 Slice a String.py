#prompt for a string
s = input("Enter a string: ")
#   line 1: print third character
print(s[2])
#   line 2: print second to last character
print(s[-2])
#   line 3: print first five characters
print(s[:5])
#   line 4: print all but last two characters
print(s[:-2])
#   line 5: print all characters with even indicies (index starts @ 0)
print(s[::2])
#   line 6: print all characters with odd indicies
print(s[1::2])
#   line 7: print all characters in reverse order
print(s[::-1])
#   line 8: print every second character in reverse order, starting with last being 0
print(s[::-2])
#   line 9: print length of given string
print(len(s))
