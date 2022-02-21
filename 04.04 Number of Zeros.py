#given 'n' numbers, first num in input is 'n', after that 'n' ints are given
n = int(input("Enter N: "))
count = 0
for num in range(n):
    if int(input("Enter a Number: ")) == 0:
        count += 1
#count num of zeros among given ints and print it (nums equal to zero, not num of zero digits)
print("Number of Zeros: {}".format(count))