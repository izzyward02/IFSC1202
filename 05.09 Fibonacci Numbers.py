#Fibonacci sequence is the sum of previous two nums in a sequence
#   sequence always begins with 0 & 1
#   first ten nums in the sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55...n 
#   i.e., if you're finding the 5th number, it is 3rd + 4th in sequence
#prompt for an index in the sequence
n = int(input("Enter Fibonacci Sequence Number: "))
a = 0
b = 1
if n == 0:
    print("Fibonacci Number: 0")
else:
    for n in range(2, n + 1):
        temp = a
        a = b
        b += temp
print("Fibonacci Number: {}".format(b))

