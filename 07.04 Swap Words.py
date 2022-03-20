#prompt for a string consisting of two words w/ a space
s = input("Enter a string: ")
word1 = s[:s.find(" ")]
word2 = s[s.find(" ") + 1:]
swapped = word2 + " " + word1
#print new string w/ first and second word positions swapped (second printed first)
print(swapped)
