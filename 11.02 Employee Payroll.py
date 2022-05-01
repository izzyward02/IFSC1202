#create class Employee
class Employee():
#   create the following attributes:
#       FirstName
#       LastName
#       IDNumber
#       HoursWorked
#       Wage
    def __init__(self, FName, LName, IDNum, HoursWorked, Wage):
#   create initializer accepting FirstName, LastName, IDNumber, & Wage and assigns them to the attribute
        self.FName = FName
        self.LName = LName
        self.IDNum = IDNum
#       set HoursWorked to (0)
        self.HoursWorked = 0
        self.Wage = Wage
#   create method WeeklyPay
    def WeeklyPay(self):
        hrs = float(self.HoursWorked)
        wg = float(self.Wage)
#       1 * Wage for HoursWorked <= 40 & 1.5 * Wage for HoursWorked > 40
        if hrs > 40:
            WeeklyPay = (wg * 40) + ((hrs - 40) * (wg * 1.5))
        else:
            WeeklyPay = wg * hrs
        return WeeklyPay
#   create find_employee w/ employee list and IDNumber as arguments
def find_employee(listA, IDNum):
    ind = -1
    for a in range(len(listA)):
        if listA[a][0] == IDNum:
            ind = i
    return ind
#   read 11.02 Employees.txt & create a list of objects
with open("11.02 Employees.txt") as gData:
    genList = []
    for g in gData:
        if g != "\n":
            g = g.replace(" ", "")
            g = g.replace("\n", "")
            data = g.split(",")
            genList.append(data)
    print("{:15}{:15}{:15}{:15}{:15}{:15}".format("First Name", "Last Name", "ID Number", "Hours Worked", "Hourly Wage", "Weekly Pay"))
#   read 11.02 Hours.txt & update hours worked for appropriate employee
    eList = []
    for a in range(len(genList)):
        newE = Employee(genList[a][0], genList[a][1], genList[a][2], genList[a][3])
        eList.append(newE)
    with open("11.02 Hours.txt") as new:
        newH = []
        for n in new:
            if n != "\n":
                n = n.replace(",", "")
                data = n.split(",")
                newH.append(data)
        for a in range(len(eList)):
            ind = find_employee(newH, eList[a].IDNum)
            if ind != -1:
                eList[a].HoursWorked = int(newH[ind][1])
#   print results
            print("{:15}{:15}{:15}{:15}{:15}{:15}".format(eList[a].FName, eList[a].LName, eList[a].IDNum, eList[a].HoursWorked, eList[a].Wage, eList[a].WeeklyPay()))
