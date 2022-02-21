#given a set of cards w/ nums from 1 to N
#   one card is now lost
#determine the number on lost card given the nums for the remaining cards
#hint: solution has three parts. Suppose there are 10 cards.
#   first, sum values from 1 to 10 (this is total value of cards)
#   second, read each card (there will be 9) & sum their values
#   third, subtract the two nums (difference is value of missing card)
n = int(input("Enter Number of Cards: "))
firstSum = 0
secondSum = 0

for i in range(1, n + 1):
    firstSum += i
for j in range (n - 1):
    secondSum += int(input("Enter Card: "))

print("Missing Card: {}".format(firstSum - secondSum))
