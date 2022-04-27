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
		CostPerSqFt = self.Price/self.SqFt
		CostPerSqFt = round(CostPerSqFt, 2)
		return CostPerSqFt
	def Payment(self):
#		APR = annual percentage rate (HINT: monthly payment, so APR / 12)
		MPR = APR / 12
#		nY = num years (HINT: 12 months in year, so numY * 12)
		nM = nY * 12
#		NOTE: price of House is needed; grab from a House attribute
		P = self.Price
#		NOTE: formula is M = P * (r(1 + r)^n) / ((1 + r)^n - 1)
#			where M = monthly payment, P = principal (Price of House), r = monthly int rate, n = num payments (# months loan is paid)
		Payment = P * ((MPR * (1 + MPR) ** nM) / ((1 + MPR) ** nM - 1))
		Payment = round(Payment, 2)
		return Payment				#WONT PRINT PAYMENT BUT VALUE IS CORRECT IN DEBUG
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
APR = int(input("Enter Interest Rate: "))
APR = APR / 100
#prompt user for num years of mortgage
nY = int(input("Enter Years for Mortgage: "))
print("\n")
#loop through HouseList & print Address, SqFt Cost, Price, and Payment for each House obj
print("{:<20}{:<20}{:<20}{:<20}{:<20}".format("Address", "Sq Ft", "SqFt Cost", "Price", "Payment"))

for a in range(len(HouseList)):
	 print("{:<20}{:<20}{:<20}{:<20}".format(HouseList[a].Address, HouseList[a].SqFt, HouseList[a].CostPerSqFt(), HouseList[a].Price, HouseList[a].Payment))
print()

#EXPECTED OUTPUT:

#Enter Interest Rate:  6
#Enter Years for Mortgage: 15

#      Address        Sq Ft      SqFt Cost        Price        Payment
#    101 Main          1500          66.67       100000         843.86
#    432 Maple         1750          62.86       110000         928.24
#    8000 Chenal       3200          87.50       280000        2362.80