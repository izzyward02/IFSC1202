#Children's Game    IFSC 1202   Izzy Ward       02.16.22 

#write a program that generates a rand num from 1-20 and asks user to guess num
#   computer will say if guess is too high or too low
#   user wins if guess is correct within five tries

#import randint from random library
import random
#prompt for user's name
userID = str(input("Hello! What is your name? "))
#display greeting w/ user's name & num of guesses
#generate rand num between 1-20
print(str("Hello " + userID + ", I am thinking of a number between 1 and 20."))
randNum = random.randrange(1, 21)
print("You have 5 guesses.")
#play game five rounds
numGuess = 0
userGuess = int(input("Take a guess: "))
while numGuess <= 5:
    if userGuess < randNum:
        numGuess += 1
        print("Your guess is too low.")
        userGuess = int(input("Try again: "))
    elif userGuess > randNum:
        numGuess += 1
        print("Your guess is too high.")
        userGuess = int(input("Try again: "))
    elif userGuess == randNum:
        print("Good job, " + userID + "! Your guessed my number in {} guesses!".format(numGuess))
        break
else: 
    print("You're out of guesses. The number I was thinking of was {}.".format(randNum))
#PROBLEM: prompts user for a different guess more than 5 times. Counter doesn't work.
