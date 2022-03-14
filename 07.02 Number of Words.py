#prompt for string consisting of words separated by a single space
s = input("Enter a string: ")
#output number of words in the string
#hint: count num of spaces
words = s.count(" ") + 1
print("{} words".format(words))
#EXAMPLE OUTPUT:

#Enter a string: How are you doing?
#4 words