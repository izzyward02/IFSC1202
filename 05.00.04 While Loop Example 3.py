#else: statements can be written after a loop body
#   this is executed once after the end of the loop body
#else statement after a loop only makes sense when used in combination with instruction 'break' 
#   if Python encounters 'break' it immediately stops loop execution and exits
#   'break' is used to abort loop execution during any iteration
i = 1
while i <= 10:
    print(i)
    i += 1
else:
    print('Loop ended, i =', i)
#in this case, else: branch isn't executed
