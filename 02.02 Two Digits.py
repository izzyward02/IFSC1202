# input digit
num = int(input("Enter a Number: "))
# use .format() to find tens and ones nums
ones = num % 10
tens = (num//10)%10
print("Ones Digit: {}".format(ones))
print("Tens Digit: {}".format(tens)) 