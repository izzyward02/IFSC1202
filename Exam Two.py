#Car Sales   Izzy Ward    IFSC1202   03.30.22

#open CarSales.txt and read a line from file
inFileTxt = "CarSales.txt"
inFile = open(inFileTxt, "r")
txtLine = inFile.readline()
#split car make and sales price w/ comma
values = txtLine.split()
#append car make and sales price to a list; NOTE: zeroth column will be car make and first column is price sold
carList = []
allTotalCars = 0
price = 0.0
allPriceAvg = 0.0
makeTotalCars = 0
makePriceAvg = 0.0
#loop through list, calculate, and print
#   total num all cars (dont use function)
#   avg sale price of all cars (dont use function)
while txtLine != " ":
    carNum = txtLine
    carList.append(carNum)
    allTotalCars += 1
    price += price
    allPriceAvg = price / allTotalCars
    txtLine = inFile.readline()
inFile.close()

print("{} Total Cars - Average Price: ${}".format(totalCars, allPriceAvg))
#prompt user for car make and convert to propercase
user = input("Enter Car Make: ")
#search zeroth column of list for car make entered (dont use list methods-manually perform search)
#   if car make is found, keep running total of sale price and count of cars found to calc an avg
#   if name not found, print "Car Make Not Found"
if user in values[[0]]:
    def properCase(user):
        return user[0:1].upper() + user[1].lower()
    print("Enter Car Make: {}".format(user))
    makeTotalCars += 1
    makePriceAvg = price / makeTotalCars
    percentPrice = ((makePriceAvg - allPriceAvg) / makePriceAvg) * 100.0
else:
    print("Car Make Not Found")
#when list is searched, print... 
#   num cars of entered car make
#   avg sales price of cars of entered make (dont use a function)
#   percent that avg sales price for entered make is above or below avg sales price for all cars
print("{} Cars Sold".format(makeTotalCars))
print("${} Average Price".format(makePriceAvg))
print("{}% Above/Below Average".format(percentPrice))