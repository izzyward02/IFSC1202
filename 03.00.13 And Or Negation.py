#and is TRUE if both are TRUE
#or is TRUE of at least one is TRUE
#not is TRUE if input is FALSE and vice versa
a = int(input())
b = int(input())
if a % 10 == 0 and b % 10 == 0:
    print('Both Numbers are a Multiple of 10')
else:
    print('One of the Numbers is Not a Multiple of 10')