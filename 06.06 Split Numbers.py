#four txt files: display a count of nums in each
fileTxtN = open("06.06 Numbers.txt", "r")
fileTxtE = open("06.06 EvenNumbers.txt", "w")
fileTxtO = open("06.06 OddNumbers.txt", "w")
fileTxtP = open("06.06 PrimeNumbers.txt", "w")
#program should perform the following:
#   opens "06.06 Numbers.txt" file for input containing ints, one per line
#   opens "06.06 EvenNumbers.txt" file for output that will contain even numbers
#   opens "06.06 OddNumbers.txt" file for output that will contain odd numbers
#   opens "06.06 PrimeNumbers.txt" file for output that will contain prime numbers
num = int(fileTxtN.readline())
countE = 0
countO = 0
countP = 0
totalRead = 0
#   creates function "isEven"
#       accepts an int & returns True if even & False if odd
def isEven(num):
    if num % 2 == 0:
        return True
    else:
        return False
#   creates function "isOdd"
#       accepts an int & returns True if odd & False if even
def isOdd(num):
    if num % 2 != 0:
        return True
    else:
        return False 
#   creates function "isPrime"
#       accepts an int & returns True if prime & false if composite
#       prime nums are greater than 1
def isPrime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
                break
            else:
                return True 
#   reads each line of "06.06 Numbers.txt" & converts to an int
#   uses "isEven" & writes even ints to "06.06 EvenNumbers.txt" (one int per line)
#   uses "isOdd" & writes odd ints to "06.06 OddNumbers.txt" (one int per line)
#   uses "isPrime" & writes prime ints to "06.06 PrimeNumbers.txt" (one int per line)
while num != " ":
    if isEven == True:
        move = fileTxtE.write(num)
        num = fileTxtN.readline()
        countE += 1
        totalRead += 1
    elif isOdd == True:
        move = fileTxtO.write(num)
        num = fileTxtN.readline()
        countO += 1
        totalRead += 1
    elif isPrime == True:
        move = fileTxtP.write(num)
        num = fileTxtN.readline()
        countP += 1
        totalRead += 1
    else:
        num = fileTxtN.readline()
        totalRead += 1
#   closes all files when finished
fileTxtN.close()
fileTxtE.close()
fileTxtO.close()
fileTxtP.close()
#   displays a count of nums in each txt file
print("{} even numbers".format(countE))
print("{} odd numbers".format(countO))
print("{} prime numbers".format(countP))
print("{} numbers read".format(totalRead))

#EXPECTED OUTPUT:

#54 even numbers
#45 odd numbers
#19 prime numbers
#99 numbers read

#EXPECTED OVERWRITE TO "06.06 EvenNumbers.txt" FILE:

#262
#886
#472
#940
#306
#854
#876
#324
#454
#410
#546
#412
#414
#366
#996
#264
#194
#52
#434
#130
#244
#370
#648
#266
#996
#538
#692
#810
#784
#80
#598
#844
#986
#606
#736
#966
#104
#790
#776
#42
#152
#94
#974
#126
#110
#512
#190
#904
#70
#414
#876
#740
#938
#212

#EXPECTED OVERWRITE TO "06.06 OddNumber.txt" FILE:

#945
#969
#219
#357
#517
#81
#37
#249
#951
#287
#187
#423
#709
#193
#945
#769
#889
#101
#239
#3515
#661
#241
#157
#11
#627
#3829
#467
#427
#449
#333
#173
#609
#45
#997
#819
#635
#917
#619
#639
#885
#215
#569
#337
#929
#91

#EXPECTED OVERWRITE TO "06.06 PrimeNumbers.txt" FILE:

#37
#709
#193
#769
#101
#239
#661
#241
#157
#11
#829
#467
#449
#173
#997
#619
#569
#337
#929