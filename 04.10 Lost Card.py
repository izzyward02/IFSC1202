#given a set of cards w/ nums from 1 to N
#   one card is now lost
#determine the number on lost card given the nums for the remaining cards
#hint: solution has three parts. Suppose there are 10 cards.
#   first, sum values from 1 to 10 (this is total value of cards)
#   second, read each card (there will be 9) & sum their values
#   third, subtract the two nums (difference is value of missing card)

#   "Enter Number of Cards: "
#   "Enter Card: " <--prompted num of times equal to num of cards
#   "Missing Card: " <-- generate value of missing card

#example num of cards is 5 & the four given cards are 1, 2, 4, 5
#   missing card = 3