#read in a full name (first, middle initial, last name) from "07.11 Names.txt"
#program should separate fullname into a first, middle, and last name
#remove any extraneous spaces & properly capitalize names

#create "properCase"
#   returns a properly cased string "s" by uppercasing the first character & lowercasing the rest
#   hint: upper() and lower() methods
#create "removeNewLine" 
#   returns a string w/ new line character "\n" removed from string "s"
#hint: replace() method
#create "trim"
#   returns a string w/ leading and trailing spaces removed from string "s"
#   hint: strip() method
#create "firstName"
#   returns first name of string "s"
#   hint: find first space in "s" using find() & create a substring from beginning of "s" up to first space
#       and call properCase() function
#create "lastName"
#   returns the last name of string "s"
#   hint: find last space in "s" using find() & create a substring from last space to end of string "s"
#       and call properCase() function
#create "middleName"
#   returns the middle name of string "s"
#   hint: find first space in "s" using find() and last space in "s" using rfind()
#       and create a substring from first space to last space in "s"
#       call trim() function and properCase() function
#       and if the length of middleName is 1, append a period

#EXPECTED OUTPUT:

#First       Middle    Last
#---------- ---------- ----------
#John       Q.         Public    
#Bruce      L.         Bauer     
#Jane       P.         Doe       
#Fred                  Smith     
#Mary       Beth       Jones