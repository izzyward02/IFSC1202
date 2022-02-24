#variables declared outside the function can be used inside it
#   such variables are called GLOBAL

a = 1
def myFunction():
    print(a)
a = "A is a global variable"
myFunction()
