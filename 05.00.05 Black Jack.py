#Black Jack style program reads nums and sums them together until total is >=21
#   input sequence ends w/ 0 for the program to be able to stop even if total sum is less than 21
total_sum = 0
a = int(input("Enter a Number:"))
while a != 0:
    total_sum += a
    if total_sum >= 21:
        print('Total sum is', total_sum)
        break
    a = int(input("Enter a Number:"))
else:
    print('Total sum is less than 21 and is equal to ' + str(total_sum) + '.')
#TEST STRINGS:
#   input 2, 4, 7, 0
#   input 9, 9, 5