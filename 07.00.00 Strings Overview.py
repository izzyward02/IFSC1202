#a string can be read from standard input using function input() or defined in single or double quotes
#   two strings can be concatenated & can also be repeated n times by multiplying by an int

#EXAMPLE 1:
print('>_< ' * 5) #OUTPUT: >_< >_< >_< >_< >_<

#a string in Python is a sequence of characters 
#   function len(some_string) returns how many characters there are in a string (the length)

#EXAMPLE 2:
print(len('abcdefghijklmnopqrstuvwxyz'))    #OUTPUT: 26

#every obj in Python can be converted into a string using function str(some_object)
#   nums can be strings

#EXAMPLE 3: 
s = str(2 ** 100)
print(s)    #OUTPUT: 1267650600228229401496703205376
print(len(s))   #OUTPUT: 31

#SLICES: a slice yields from given string one character or some fragment
#three forms of slices: single character, substring, subsequence

#   single character: simplest form of slice
#       S[i] gives ith character of string
#       count characters from zero
#       in Python, there is no separate type for characters in a string
#       S[i] also has type str, just as source string
#       number S[i] is an index
#       if negative index is specified, it is counted from end, starting with -1

#EXAMPLE 4:
# String S |   H   |   e   |   l   |   l   |   o   |
#Index    |  S[0] |  S[1] |  S[2] |  S[3] |  S[4] |
#Index    | S[-5] | S[-4] | S[-3] | S[-2] | S[-1] |

#if index in slice S[i] is greater than or equal to len(S), or less than -len(S), following error is caused:
#   IndexError: string index out of range

#   substring: slice w/ two parameters S[a:b]
#       returns substring length of b-a, starting w/ character at index a and lasting until character at index b, non inclusive
#       can mix positive and negative indicies in same slice
#       slices w/ two parameters never cause IndexError
#       if second parameter is omitted, but colon is preserved, then slice goes to end of string
#       if first paramter is omitted, then Python takes slice from beginning of string
#       to remove last character from string, use slice S[:-1]. Slice S[:] matches string S itself

#   subsequence: a slice with three parameters S[a:\b:d]
#       the third parameter specifies the step, same as for function range()
#       only characters w/ following index are taken: a, a+d, a+2*d, etc until and not including character with index b
#       if third parameter ==2, slice takes every second character
#       if step ==-1, characters go in reverse order

#EXAMPLE 5:
s = 'abcdefg'
print(s[1])     #b
print(s[-1])    #g
print(s[1:3])   #bc
print(s[1:-1])  #bcdef
print(s[:3])    #abc
print(s[2:])    #cdefg
print(s[:-1])   #abcdef
print(s[::2])   #aceg
print(s[1::2])  #bdf
print(s[::-1])  #gfedcba

#Note how third parameter is similar to third parameter of range()

#EXAMPLE 6:
s = 'abcdefghijklm'
print(s[0:10:2])
for i in range(0, 10, 2):
    print(i, s[i])
#OUTPUT: 
# acegi
# 0 a
# 2 c
# 4 e
# 6 g
# 8 i

#STRING METHODS: find() & rfind()
#method is a function that is bound to an object
#   when method is called, method is applied to object & does computations related to it
#   methods are invoked as object_name.method_name(arguments)
#   find() method searches a substring, passed as an argument, inside the string on which it is called
#       function returns index of first occurrence of substring
#       if substring isn't found, method returns -1

#EXAMPLE 7:
s = 'Hello'
print(s.find('e')) #1
print(s.find('ll')) #2
print(s.find('L'))  #-1

#similarly, rfind() method returns index of last occurrence of substring

#EXAMPLE 8:
s = 'abracadabra'
print(s.find('b')) #1
print(s.rfind('b')) #8

#if find() is called with three arguments s.find(substring, left, right), search is performed inside slice s[left:right]
#   if only two arguments are specified s.find(substring, left), search is performed in slice s[left:]
#       starting w/ character at index left to the end of string
#   method s.find(substring, left, right) returns absolute index, relative to whole string "s", and not to the slice

#EXAMPLE 9:
s = 'my name is bond, james bond, okay?'
print(s.find('bond'))   #11
print(s.find('bond', 12))   #23

#STRING METHOD: replace()
#   method replace() replaces all occurrences of a given substring with another
#       SYNTAX: s.replace(old, new)
#       takes string "s" and replaces all occurrences of substring old with substring new

#EXAMPLE 10:
print('a bar is a bar, essentially'.replace('bar', 'pub'))  #a pub is a pub, essentially

#a third argument counter can be passed: s.replace(old, new, count)
#   makes replace() to replace only first count occurrences then stops

#EXAMPLE 11:
print('a bar is a bar, essentially'.replace('bar', 'pub', 1))  #a pub is a bar, essentially

#STRING METHOD: count()
#   method counts num of occurrences of one string within another
#       simplest form: s.count(substring)
#       only non-overlapping occurrences are taken into account

#EXAMPLE 12:
print('Abracadabra'.count('a'))    # 4
print(('aaaaaaaaaa').count('aa'))  # 5

#if three parameters are specified s.count(substring, left, right), count is performed within slice s[left:right]

#REMOVING LEADING AND TRAILING BLANKS: to remove blanks from a string, use strip() method
#   syntax: mystring = mystring.strip(" ")

#UPPER CASE: to convert string to uppercase, use upper() method
#   syntax: mystring = mystring.upper()

#LOWER CASE: to convert string to lowercase, use lower() method
#   syntax: mystring = mystring.lower()

#REMOVE A LINE FEED (WHEN READING A FILE): to remove a line feed character at end of string during a readline.. 
#   syntax: mystring = mystring.replace("\n", "")

#SUMMARY OF STRING METHODS:
#'capitalize()`	Converts the first character to upper case
#'casefold()`	Converts string into lower case
#'center()`	Returns a centered string
#'count()`	Returns the number of times a specified value occurs in a string
#'encode()`	Returns an encoded version of the string
#'endswith()`	Returns true if the string ends with the specified value
#'expandtabs()`	Sets the tab size of the string
#'find()`	Searches the string for a specified value and returns the position of where it was found
#'format()`	Formats specified values in a string
#'index()`	Searches the string for a specified
#'isalnum()`	Returns True if all characters in the string are alphanumeric
#'isalpha()`	Returns True if all characters in the string are in the alphabet
#'isdecimal()`	Returns True if all characters in the string are decimals
#'isdigit()`	Returns True if all characters in the string are digits
#'isidentifier()`	Returns True if the string is an identifier
#'islower()`	Returns True if all characters in the string are lower case
#'isnumeric()`	Returns True if all characters in the string are numeric
#'isprintable()`	Returns True if all characters in the string are printable
#'isspace()`	Returns True if all characters in the string are whitespaces
#'istitle()`	Returns True if the string follows the rules of a title
#'isupper()`	Returns True if all characters in the string are upper case
#'join()`	Joins the elements of an iterable to the end of the string
#'ljust()`	Returns a left justified version of the string
#'lower()`	Converts a string into lower case
#'lstrip()`	Returns a left trim version of the string - removes whitespace (blanks, tabs, conrol characters)
#'maketrans()`	Returns a translation table to be used in translations
#'partition()`	Returns a tuple where the string is parted into three parts
#'replace()`	Returns a string where a specified value is replaced with a specified value
#'rfind()`	Searches the string for a specified value and returns the last position of where it was found
#'rindex()`	Searches the string for a specified value and returns the last position of where it was found
#'rjust()`	Returns a right justified version of the string
#'rpartition()`	Returns a tuple where the string is parted into three parts
#'rsplit()`	Splits the string at the specified separator, and returns a list
#'rstrip()`	Returns a right trim version of the string - removes whitespace (blanks, tabs, conrol characters)
#'split()`	Splits the string at the specified separator, and returns a list
#'splitlines()`	Splits the string at line breaks and returns a list
#'startswith()`	Returns true if the string starts with the specified value
#'strip()`	Returns a trimmed version of the string - removes whitespace (blanks, tabs, conrol characters)
#'swapcase()`	Swaps cases, lower case becomes upper case and vice versa
#'title()`	Converts the first character of each word to upper case
#'translate()`	Returns a translated string
#'upper()`	Converts a string into upper case
#'zfill()`	Fills the string with a specified number of 0 values at the beginning