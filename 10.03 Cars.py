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
    def Accelerate(self, fileRead):
        Accelerate = self.Speed + fileRead
        return self.Speed
#   brake subtracts value from car's speed (don't go below zero)
    def Brake(self, fileRead):
        Brake = self.Speed + fileRead
        if self.Speed < 0:
            self.Speed = 0
        return self.Speed
#first record in 10.03 Cars.txt file contains year and make
fileTxt = open("10.03 Cars.txt", "r")
carList = []
fileRead = fileTxt.readline()
while fileRead != "":
    carData = fileRead.split(", ")
    carList.append(carData)
    fileRead = fileTxt.readline()
#   instantiate one car object w/ this data
for a in range(1):
    for b in range(len(carList)):
        car1 = Car(carData[a][0], carData[a][1])
        car1.Make = int(carList[a][0])
        car1.Year = str(carList[a][1])
print("Make: {}".format(car1.Make))
print("Year: {}".format(car1.Year))
#track speed and calculate change of speed
print("{:<15}{:<15}".format("Change", "Speed"))
for a in range(1, len(carList)):
    for b in range(1):
        speedData = float(carList[a][b])
#       if num is greater than zero, call Accelerate
    if speedData > 0:
        print("{:<20}{:<20}".format(carList[a][b], car1.Accelerate(speedData)))
#       if num is less than zero, call Brake
    if speedData < 0:
        print("{:<20}{:<20}".format(carList[a][b], car1.Brake(speedData)))
#print change of speed value and current speed
print()
