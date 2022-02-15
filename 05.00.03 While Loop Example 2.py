#case of the while loop to determine the num of digits of an int 'n' 
n = int(input("Enter a Number:"))
length = 0
while n > 0:
    n //= 10  # this is equivalent to n = n // 10
    length += 1
print(length)
#on each iteration, the last digit if num is cut using int division by 10 (n//=10)
#   in variable length, the num of times this is done is counted
