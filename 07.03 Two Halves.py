#prompt for a string
s = input("Enter a string: ")
#cut into two equal parts (if length is odd, place center character in first string)
half1 = s[:(len(s) + 1) // 2]
half2 = s[(len(s) + 1) // 2:]
swapped = half2 + half1
#print new string on single row with first and second halves interchanged (second first and first second)
print(swapped)
