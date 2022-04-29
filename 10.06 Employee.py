#create class Employee w/ following attributes:
class Employee():
#   FirstName
#   LastName
#   IDNumber
#   HoursWorked
#   Wage
    def __init__(self, FName, LName, IDNum, HoursWorked, Wage):
#create initializer that accepts FirstName, LastName, IDNumber, HoursWorked, and Wage
#   assign them to appropriate attribute
        self.FName = FName
        self.LName = LName
        self.IDNum = IDNum
        self.HoursWorked = HoursWorked
        self.Wage = Wage
#Employee class should have method WeeklyPay that calcs weekly pay
    def WeeklyPay(self):
        hrs = float(self.HoursWorked)
        wg = float(self.Wage)
        if hrs > 40:
            WeeklyPay = (wg * 40) + ((hrs - 40) * (wg * 1.5))
            WeeklyPay = round(WeeklyPay, 2)
        else:
            WeeklyPay = wg * hrs
            WeeklyPay = round(WeeklyPay, 2)
#   WeeklyPay is defined as 1 x wage for 0-40 hrs and 1.5 x wage for hours > 40
        return WeeklyPay
#for each line in Payroll.txt file, create one Employee obj & reuse to read the next Employee
fileTxt = open("10.06 Payroll.txt", "r")
eList = []
for payData in fileTxt:
    if payData != "\n":
        payData = payData.replace(" ", "")
        payData = payData.replace("\n", "")
        eData = payData.split(",")
        eList.append(eData)
#print FirstName, LastName, IDNumber, HoursWorked, HourlyWage, and WeeklyPay for each employee
print("{:<20}{:<20}{:<20}{:<20}{:<20}{:<20}".format("First", "Last", "ID", "Hours", "Hourly", "Weekly"))
print("{:<20}{:<20}{:<20}{:<20}{:<20}{:<20}".format("Name", "Name", "Number", "Worked", "Wage", "Pay"))

for a in range(len(eList)):
    e = Employee(eList[a][0], eList[a][1], eList[a][2], eList[a][3], eList[a][4])
    print("{:<20}{:<20}{:<20}{:<20}{:<20}{:<20}".format(e.FName, e.LName, e.IDNum, e.HoursWorked, e.Wage, e.WeeklyPay()))
print()
