#program prints squares of all ints from 1-10
#   this replaces the while loop w/ 'for...in range()' loop
i = 1
while i <= 10:
    print(i ** 2)
    i += 1
#the variable 'i' inside loop iterates from 1-10
#   value of 'i' changes w/ each new loop iteration (this is called a counter)
#   note after executing this fragment, the value of 'i' is defined and is equal to 11
#   b/c when i==11, condition i<=10 is FALSE for first time
