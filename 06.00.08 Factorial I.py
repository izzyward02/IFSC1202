#functions are code sections isolated from rest of program & executed only when called
#   i.e., sqrt(), len(), and print()
#   they all take parameters (none to several) & can return a value (or can return nothing)

#the factorial() function takes a single parameter-- the number-- & returns a value-- the number's factorial
#the "def" statement defines the name of the function & name of value passed to it
#the "return" statement returns value calculated by function

#PROGRAM TO PRINT FACTORIAL OF A NUMBER:
def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res
print(factorial(3))
