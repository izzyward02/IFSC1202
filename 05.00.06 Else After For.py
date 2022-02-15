#else: branch can be used for 'for' loop
#EXAMPLE: program reads exactly five ints but stops when first negative int is met
for i in range(5):
    a = int(input("Enter a Number:"))
    if a < 0:
        print('Met a negative number', a)
        break
else:
    print('No negative numbers met')
#TEST STRINGS:
#   3, 6, 2, 4, 5
#   3, 6, -2, 4, 5
