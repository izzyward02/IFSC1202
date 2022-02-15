#sum the ints from 1 to 'n' inclusively
#remember that 'max_value' in range(min_value, max_value) ISN'T INCLUDED
#for 'i' to run from 1 to 'n' inclusively, 'max_value' must be 'n+1' 
result = 0
n = 5
for i in range(1, n + 1):
    result += i
    # this ^^ is the shorthand for
    # result = result + i
print(result)
