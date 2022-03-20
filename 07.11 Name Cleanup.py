#read in a full name (first, middle initial, last name) from "07.11 Names.txt"
#program should separate fullname into a first, middle, and last name
#remove any extraneous spaces & properly capitalize names

#create "properCase"
#   returns a properly cased string "s" by uppercasing the first character & lowercasing the rest
#   hint: upper() and lower() methods
def properCase(s):
    return s[0:1].upper() + s[1].lower()
#create "removeNewLine" 
#   returns a string w/ new line character "\n" removed from string "s"
#hint: replace() method
def RemoveNewLine(s):
    return s.replace("\n", "")
#create "trim"
#   returns a string w/ leading and trailing spaces removed from string "s"
#   hint: strip() method
def trim(s):
    return s.strip(" ")
#create "firstName"
#   returns first name of string "s"
#   hint: find first space in "s" using find() & create a substring from beginning of "s" up to first space
#       and call properCase() function
def firstName(s):
    fNameIndex = s.find(" ")
    firstName = s[:fNameIndex]
    firstName = properCase(firstName)
    return firstName
#create "lastName"
#   returns the last name of string "s"
#   hint: find last space in "s" using find() & create a substring from last space to end of string "s"
#       and call properCase() function
def lastName(s):
    lNameIndex = s.rfind(" ") + 1
    lastName = s[lNameIndex:]
    lastName = properCase(lastName)
    return lastName
#create "middleName"
#   returns the middle name of string "s"
#   hint: find first space in "s" using find() and last space in "s" using rfind()
#       and create a substring from first space to last space in "s"
#       call trim() function and properCase() function
#       and if the length of middleName is 1, append a period
def middleName(s):
    fNameIndex = s.find(" ")
    lNameIndex = s.rfind(" ") + 1
    middleName = s[fNameIndex:lNameIndex]
    middleName = trim(middleName)
    middleName = properCase(middleName)
    if len(middleName) == 1:
        middleName += "."
    return middleName

print("{:10s} {:10s} {:10s}".format("First", "Middle", "Last"))
print("{:10s} {:10s} {:10s}".format("-"*10, "-"*10, "-"*10))

fileInput = open("07.11 Names.txt", "r")
fullName = trim(RemoveNewLine(fileInput.readline()))

while fullName != "":
    print("{:10s} {:10s} {:10s}".format(firstName(fullName), middleName(fullName), lastName(fullName)))
    fullName = trim(RemoveNewLine(fileInput.readline()))
