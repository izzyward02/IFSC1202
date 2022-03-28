#"08.11 USPopulation.txt" file contains midyear pops of US in thousands between 1950 and 1990
#   first line contains pop for 1950, second for 1951, etc
#   ------------------------
#create a program that reads file contents into a list
#program should perform the following:
#   read file into list of ints (multiply by 1000)
popList = []

inFileTxt = "08.11 USPopulation.txt"
inFile = open(inFileTxt, "r")
txtLine = inFile.readline()
#   iterate through array and display:
#       year
#       population
#       change from previous year
#       percent change in population over last year (change in pop / previous year pop) * 100
while txtLine != " ":
    popNum = txtLine
    popNum *= 1000
    popList.append(popNum)
    txtLine = inFile.readline()
inFile.close()

print("Year     Population      Change      Percent Change".format())
print("{:4d}    {:9d}       N/A         N/A".format(1950, (popList[0])))
#   display following based on changes in population (not changes in percent):
#       Average Population Change
#       Minimum Population Change & Year
#       Maximum Population Change & Year
sumPopDiff = 0
maxPopDiff = popList[1] - popList[0]
minPopDiff = popList[1] - popList[0]
maxYear = 1951
minYear = 1951
#don't use list or string functions or methods
#don't use "for x in y" iterator; use "for x in range(n)"
for i in range(1, len(popList)):
    popDiff = popList[i] - popList[i - 1]
    pChange = float(popDiff) / float(popList[i - 1]) * 100.0
    print("{:4d}    {:9d}   {:9d}   {:1.2f}%".format(1950 + i, popList[i], popDiff, pChange))
    if popDiff > maxPopDiff:
        maxPopDiff = popDiff
        maxYear = 1950 + i
    if popDiff < minPopDiff:
        minPopDiff = popDiff
        minYear = 1950 + i
    sumPopDiff += popDiff

print("")
print("Average Change = {}".format(float(sumPopDiff) / float(len(popList) - 1.0)))
print("Minimum Change = {}  ({})".format(minPopDiff, minYear))
print("Maximum Change = {}  ({})".format(maxPopDiff, maxYear))
