#Izzy Ward		Exam Three		IFSC 1202		04.27.22

#create House class
class House():
#	attributes:
	def __init__(self, Address, SqFt, Price):
		self.Address = Address
		self.SqFt = SqFt
		self.Price = Price
#	methods:
	def CostPerSqFt(self):
#		returns cost per SqFt (HINT: Price / SqFt)
        CostPerSqFt = self.Price / self.SqFt
        return CostPerSqFt

	def Payment(self, APR, nY):
#		APR = annual percentage rate (HINT: monthly payment, so APR / 12)
		MPR = APR / 12
#		nY = num years (HINT: 12 months in year, so numY * 12)
		nM = nY * 12
#		NOTE: price of House is needed; grab from a House attribute
		P = self.Price
#		NOTE: formula is M = P * (r(1 + r)^n) / ((1 + r)^n - 1)
#			where M = monthly payment, P = principal (Price of House), r = monthly int rate, n = num payments (# months loan is paid)
		Payment = P * ((MPR * (1 + MPR) ** nM) / ((1 + MPR) ** nM - 1))
		return Payment
#-----------
#		WORST CASE: return $100 for partial credit (must set up the method)
#		Payment = 100
#		return Payment
#-----------
#open "Exam Three Houses.txt" for reading
fileTxt = open("Exam Three Houses.txt", "r")
HouseList = []
#readline and split into list
fileRead = fileTxt.readline()
#create House object from list and append House obj to list HouseList
#repeat for all House objs in file
while fileRead != "":
    Address, SqFt, Price = fileRead.split(",")
    houseData = House(str(Address), int(SqFt), float(Price))
    HouseList.append(houseData)
    fileRead = fileTxt.readline()
#prompt user for interest rate (NOTE: divide by 100 so x% becomes decimal)
userIntRate = int(input("Enter Interest Rate: "))
#prompt user for num years of mortgage
userNumYears = int(input("Enter Years for Mortgage: "))
#loop through HouseList & print Address, SqFt Cost, Price, and Payment for each House obj
print("{:<20}{:<20}{:<20}{:<20}{:<20}".format("Address", "Sq Ft", "SqFt Cost", "Price", "Payment"))

for a in range(len(HouseList)):
	 print("{:<20}{:<20}{:<20}{:<20}".format(HouseList[a].Address, HouseList[a].SqFt, HouseList[a].CostPerSqFt, HouseList[a].Price, HouseList[a].Payment()))
print()

#print("{:<20}{:<20}{:<20}{:<20}{:<20}".format(house1.Address, house1.SqFt, house1.CostPerSqFt, house1.Price, house1.Payment))
#print("{:<20}{:<20}{:<20}{:<20}{:<20}".format(house2.Address, house2.SqFt, house2.CostPerSqFt, house2.Price, house2.Payment))
#print("{:<20}{:<20}{:<20}{:<20}{:<20}".format(house3.Address, house3.SqFt, house3.CostPerSqFt, house3.Price, house3.Payment))
