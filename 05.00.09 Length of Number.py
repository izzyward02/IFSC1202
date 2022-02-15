#another example of how 'break' and 'continue' only affect innermost execution
#   when these commands are nested
n = int(input())
length = 0
while True:
    length += 1
    n //= 10
    if n == 0:
        break
print('Length is', length)
#note that this is very inefficient & can be replaced with a cleaner loop condition...
n = int(input())
length = 0
while n != 0:
    length += 1
    n //= 10
print('Length is', length)
#does the same job as previous