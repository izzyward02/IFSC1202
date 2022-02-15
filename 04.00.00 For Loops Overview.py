#loops repeat sections of code
#same as with if-else statements, indentation specifies which instructions are controlled
#the range(min, max) command generates a sequence of nums (note that last num isn't included)

#FOR LOOP WITH RANGE
#for-loop is used to iterate some int variable in increasing or decreasing order
for i in range(5, 8):
    print(i, i ** 2)
print('End of Loop')

#FOR LOOP (REDUCED FORM)
#reduced form of range() is range(max_value) where min_value is implicitly set to zero
for i in range(3):
    print(i)

#FOR LOOP PARAMETERS
#parameter in for loop can be a calculation or an int variable
x = 4
for i in range(x):
    print('Hello, world!')

#FOR LOOP EMPTY SEQUENCE
#range() can define empty sequence [i.e., range(-5) or range(7, 3)]
#in above case ^^ the for-block won't execute
for i in range(-5):
    print("Hello, world!")
print("End of Loop")

#COMPLEX FOR LOOP EXAMPLE
#for loop creates the sum of ints from 1 to 'n' inclusively
#max_value in range() is 'n+1' to make 'i' equal to 'n' on last step
result = 0
n = 5
for i in range(1, n + 1):
    result += i
    # this ^^ is the shorthand for
    # result = result + i
print(result)

#DECREASING SEQUENCE
#use extended form of range() w/ three arguments --> range(start_value, end_value, step)
#when step is omitted, it implicitly equals 1, but can be any non-zero value
#loop always includes start_value and excludes end_value in iteration
for i in range(10, 0, -2):
    print(i)

#MORE ON PRINT FUNCTION
#by default, print() prints all arguments by separating them by space and new line
#behavior can be changed with keyword 'sep' and 'end'
#specify 'end=""' which does not advance to a new line
print(1, 2, 3)
print(4, 5, 6)
print(1, 2, 3, sep=", ", end=". ")
print(4, 5, 6, sep=", ", end=". ")
print()
print(1, 2, 3, sep="", end=" -- ")
print(4, 5, 6, sep=" * ", end=".")
