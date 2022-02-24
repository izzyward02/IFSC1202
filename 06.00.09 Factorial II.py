#a function should be placed @ beginning of the program (before the place where the function needs to be used)

#FIRST LINE OF FUNCTION:

#the "def" line is a description of the function
#word "factorial" is an identifier (name of the function)
#after identifier is the list of parameters that the function receives
#   list consists of comma-separated identifiers of parameters
#colon is needed @ end of first line

#FUNCTION BODY:

#body must be indented (use TAB or four spaces)
#"factorial" function calculates value of "n!" and stores it in variable "res" (for result)
#last line of function returns "res" & exits function, returning value of variable "res"
#   "return" statement can appear in any place in a function
#   execution exits the function & returns specified value
#   if function returns no value, "return" won't return a value
#some functions don't need "return" & can be omitted

#PROGRAM RETURNING MULTIPLE FACTORIALS:

def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

print(factorial(3))
print(factorial(5))
