#while loop repeats sequence of actions several times until some condition is FALSE
#condition is given before loop body & is checked before each execution of loop body
#while loop is used when it is impossible to determine exact number of loop iterations needed
#syntax of while loop in simplest case:

#while some condition:
    #a block of statements

#Python first checks condition. 
#   If FALSE, loop is terminated and passed to next statement after while loop body
#   If TRUE, loop body is executed, condition is checked again; this continues while condition is TRUE
#   Once condition is FALSE, loop terminates and passed to next statement after loop body

#EXAMPLE: following program fragment prints the squares of all ints from 1-10
#   here, the 'for...in range()' loop is replaced with 'while' 
i = 1
while i <= 10:
    print(i ** 2)
    i += 1
#prints 1 4 9 16 25 36 49 64 81 100

#in above case^^^ variable 'i' inside loop iterates from 1-10
#value of 'i' changes w/ each new loop iteration (this is called a counter)
#note that after executing this fragment, the value of 'i' is defined and equal to 11
#   b/c when i==11, condition i<=10 is FALSE for first time

#ANOTHER EXAMPLE: use while loop to determine num of digits of int 'n' 
n = int(input())
length = 0
while n > 0:
    n //= 10  # this is equivalent to n = n // 10
    length += 1
print(length)
#on each iteration, last digit of num is cut using int division by 10 (n//=10)
#in variable length, num of times this happened is counted
#Python provides easier way to solve this: 'length = len(str(i))' 

#LOOP CONTROL FLOW: ELSE
#an else: statement can be written after a loop body which is executed after the end of the loop
i = 1
while i <= 10:
    print(i)
    i += 1
else:
    print('Loop ended, i =', i)
#executes loop, then prints "Loop ended, i = 11" after execution is FALSE

#the else statement after a loop only makes sense when used in combination w/ instruction break
#   if during execution of loop, Python encounters a break, it immediately stops loop execution and exits
#   in this case, else branch isn't executed, so a break is used to abort the loop in middle of any iteration
#EXAMPLE: a program reads nums and sums it until total is >=21
#   input sequence ends w/ 0 for the program to be able to stop even if total sum of all nums is less than 21
total_sum = 0
a = int(input())
while a != 0:
    total_sum += a
    if total_sum >= 21:
        print('Total sum is', total_sum)
        break
    a = int(input())
else:
    print('Total sum is less than 21 and is equal to', total_sum, '.')
#loop exited normally, so else is executed
for i in range(5):
    a = int(input())
    if a < 0:
        print('Met a negative number', a)
        break
else:
    print('No negative numbers met')
#the loop is aborted by 'break' so else branch isn't executed

#LOOP CONTROL FLOW: CONTINUE
#another instruction used to control loop execution is 'continue' 
#   if Python meets 'continue' in the middle of loop iteration, it skips all remaining instructions & proceeds to next iteration
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found an odd number", num)
#prints:
#   Found an even number 2
#   Found an odd number 3
#   Found an even number 4
#   Found an odd number 5
#   Found an even number 6
#   Found an odd number 7
#   Found an even number 8
#   Found an odd number 9

#if 'break' and 'continue' are placed inside several nested loops, they affect only the execution of intermost one
for i in range(3):
    for j in range(5):
        if j > i:
            # breaks only the for on line 2
            break
        print(i, j)
#prints:
#   0 0
#   1 0
#   1 1
#   2 0
#   2 1
#   2 2

#instructions 'break' and 'continue' are discouraged unless implementation is unavoidable
#EXAMPLE OF BAD USAGE: this code counts num of digits in an int
n = int(input())
length = 0
while True:
    length += 1
    n //= 10
    if n == 0:
        break
print('Length is', length)
#it is cleaner and more efficient to rewrite loop with meaningful loop condition...
n = int(input())
length = 0
while n != 0:
    length += 1
    n //= 10
print('Length is', length)
#does the same job as previous code block, w/o use of 'break' or 'continue' 

#MULTIPLE ASSIGNMENT
#in Python it is possible for a single assignment to change the value of several variables
a, b = 0, 1
#effect of this code can be written as...
a = 0
b = 1
#difference between two versions is that multiple assignment changes value of two variables simultaneously
#   multiple assignment is useful when you need to exchange values of two variables
#   older programming languages w/o support of multiple assignment use auxiliary variable for this task:
a = 1
b = 2
tmp = a
a = b
b = tmp
print(a, b)     #prints 2 1
#in Python, same swap can be written in one line...
a = 1
b = 2
a, b = b, a
print(a, b)     #prints 2 1
#the left-hand side of '=' should have a comma-separated list of variable names
#right-hand side can be any expressions, separated by commas
#   left and right sides should be of equal length

#RANDOM NUMBERS
#often used to simulate game play
#Python uses two functions for random nums: 'randint' and 'random()' 

#RANDOM INTEGERS
#the 'randint' function can be imported from the 'random' library
#   in 'randint', provide a range for the random ints
#to simulate rolling of a dice w/ 6 sides, use:
from random import randint
x = randint(1,6)
#gives a random value between 1-6 inclusive

#RANDOM FLOATING POINT NUMBERS
#a random multiplier is a random floating point num between 0 and 1
#   generated using the 'random' function with no arguments
#   imported from the 'random' library
from random import random
x = random()
#gives a random floating point num between 0 and 1