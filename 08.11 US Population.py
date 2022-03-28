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

#EXPECTED OUTPUT:

#Year    Population    Change    Percent Change
#1950    151868000     N/A       N/A
#1951    153982000     2114000   1.39%
#1952    156393000     2411000   1.57%
#1953    158956000     2563000   1.64%
#1954    161884000     2928000   1.84%
#1955    165069000     3185000   1.97%
#1956    168088000     3019000   1.83%
#1957    171187000     3099000   1.84%
#1958    174149000     2962000   1.73%
#1959    177135000     2986000   1.71%
#1960    179979000     2844000   1.61%
#1961    182992000     3013000   1.67%
#1962    185771000     2779000   1.52%
#1963    188483000     2712000   1.46%
#1964    191141000     2658000   1.41%
#1965    193526000     2385000   1.25%
#1966    195576000     2050000   1.06%
#1967    197457000     1881000   0.96%
#1968    199399000     1942000   0.98%
#1969    201385000     1986000   1.00%
#1970    203984000     2599000   1.29%
#1971    206827000     2843000   1.39%
#1972    209284000     2457000   1.19%
#1973    211357000     2073000   0.99%
#1974    213342000     1985000   0.94%
#1975    215465000     2123000   1.00%
#1976    217563000     2098000   0.97%
#1977    219760000     2197000   1.01%
#1978    222095000     2335000   1.06%
#1979    224567000     2472000   1.11%
#1980    227225000     2658000   1.18%
#1981    229466000     2241000   0.99%
#1982    231664000     2198000   0.96%
#1983    233792000     2128000   0.92%
#1984    235825000     2033000   0.87%
#1985    237924000     2099000   0.89%
#1986    240133000     2209000   0.93%
#1987    242289000     2156000   0.90%
#1988    244499000     2210000   0.91%
#1989    246819000     2320000   0.95%
#1990    249623000     2804000   1.14%

#Average Change = 2443875.0
#Minimum Change = 1881000 (1967)
#Maximum Change = 3185000 (1955)