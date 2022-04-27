#create class Car w/ following attributes:
class Car():
#   year
#   make
#   speed
    def __init__(self, Make, Year, Speed = 0):
#constructor should accept car's make and year & speed should be set to zero
        self.Make = Make
        self.Year = Year
        self.Speed = Speed
#methods:
#   accelerate adds value to car's speed
    def Accelerate(self):
        Accelerate = self.Speed + speedData
        return Accelerate
#   brake subtracts value from car's speed (don't go below zero)
    def Brake(self):
        Brake = self.Speed - speedData
        return Brake
#first record in 10.03 Cars.txt file contains year and make
fileTxt = open("10.03 Cars.txt", "r")
carList = []
carSpeed = []
speedChange = 0
#   instantiate one car object w/ this data
fileRead = fileTxt.readline()
carData = fileRead.split(", ")
car1 = Car(carData[0], carData[1])
print("Make: {}".format(car1.Make))
print("Year: {}".format(car1.Year))

fileRead = fileTxt.readline()
print("{:<15}{:<15}".format("Change", "Speed"))
while fileRead != "":
    
    carSpeed.append(fileRead)
#       if num is greater than zero, call Accelerate
    if fileRead >= 0:
        car1.Accelerate()
        speedChange += fileRead
#       if num is less than zero, call Brake
    else:
        car1.Brake()
        speedChange -= fileRead
    fileRead = fileTxt.readline()
#print change of speed value and current speed
print(carSpeed)
#EXAMPLE OUTPUT:

#Make: Jeep
#Year: 2014

#Change    Speed
#    60       60
#    -5       55
#   -10       45
#     3       48