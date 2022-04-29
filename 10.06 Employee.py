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
    def WeeklyPay():
        if self.HoursWorked > 40:
            WeeklyPay = self.Wage * 1.5
        else:
            WeeklyPay = self.Wage * 1
#   WeeklyPay is defined as 1 x wage for 0-40 hrs and 1.5 x wage for hours > 40
        return WeeklyPay
#for each line in Payroll.txt file, create one Employee obj & reuse to read the next Employee
fileTxt = open("10.06 Payroll.txt", "r")
eList = []
for payData in fileTxt:
    payData = fileRead.split(",")
    eData = Employee(payData[0], payData[1], payData[2], payData[3], payData[4:])
    eList.append(eData)
#print FirstName, LastName, IDNumber, HoursWorked, HourlyWage, and WeeklyPay for each employee
print("{:>20}{:>20}{:>20}{:>20}{:>20}{:>20}".format("First", "Last", "ID", "Hours", "Hourly", "Weekly"))
print("{:>20}{:>20}{:>20}{:>20}{:>20}{:>20}".format("Name", "Name", "Number", "Worked", "Wage", "Pay"))

for e in eList:
    print("{:>20}{:>20}{:>20}{:>20}{:>20}{:>20}".format(e.FName, e.LName, e.IDNum, e.HoursWorked, e.Wage, e.WeeklyPay()))
print()

#EXPECTED OUTPUT:

#   First    Last      ID   Hours  Hourly  Weekly
#    Name    Name  Number  Worked    Wage     Pay
#   Susan  Meyers   47899   41.00   15.64  649.06
#    Mark   Jones   39119   37.00   14.46  535.02
#     Joy  Rogers   41774   43.00   15.28  679.96