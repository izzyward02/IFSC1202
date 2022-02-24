#if a variable is initialized inside a function, it cannot be used outside the function

def myFunction():
	a = "A is a local variable"
	return a
	
b = myFunction()
print(a)    #changing to "print(b)" corrects error

#generates error
#   NameError: name 'a' is not defined
#such variables are called LOCAL
#   these become unavailable after exiting function
#   to access variable 'a', program will have to return the value to the calling program
#   to correct error: change "print(a)" to "print(b)"
