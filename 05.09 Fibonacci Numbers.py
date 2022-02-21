#Fibonacci sequence is the sum of previous two nums in a sequence
#   sequence always begins with 0 & 1
#   first ten nums in the sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55...n 
#   i.e., if you're finding the 5th number, it is 3rd + 4th in sequence
#prompt for an index in the sequence
n = int(input("Enter Fibonacci Sequence Number: "))
a = 1
b = 1
c = 2
count = 1
while(count <= n):
    count += 1
    a + b
    b = c
    c = a + b
print("Fibonacci Number: {}".format(count))
#   "Fibonacci Number: "

#example input of sequence index 7 generates Fibonacci number of 13
#example input of sequence index 10 generates Fibonacci number of 55
