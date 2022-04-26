#create class Car w/ following attributes:
class Car():
#   year
#   make
#   speed
    def __init__(self, Year, Make):
#constructor should accept car's make and year & speed should be set to zero
        self.Year = Year
        self.Make = Make
        self.Speed = 0
#methods:
    def Change(Speed, car1):
        for a in Speed:
            print(a, end = "\t")
            if a > 0:
                car1.Accelerate(a)
            else:
                a *= -1
                car1.Brake(a)
        return Change
#   accelerate adds value to car's speed
    def Accelerate(self, change):
        self.Speed += change
        return Accelerate
#   brake subtracts value from car's speed (don't go below zero)
    def Brake(self, change):
        if self.Speed < change:
            change -= self.Speed
        else:
            self.Speed -= change
        return Brake
#first record in 10.03 Cars.txt file contains year and make
fileTxt = open("10.03 Cars.txt", "r")
carList = []
carSpeed = []

with open("10.03 Cars.txt", "r") as file:
    fileRead = fileTxt.readline()
    carData = fileRead.split("\n")
    carInfo = carData[0].split(",")
    for b in carInfo:
        carList.append(b)
    yr = carList[0]
    m = carList[1]
    for b in range(1, len(carData)):
        carSpeed.append(carData[b])
#   instantiate one car object w/ this data
car1 = Car(yr, m)
print("Make: {}" + "\n" + "Year: {}".format(car1.Make, car1.Year))
print("{:>10}{:>10}".format("Change", "Speed"))
#       if num is greater than zero, call Accelerate
#       if num is less than zero, call Brake
#print change of speed value and current speed
print("{:>10}{:>10}".format())
#EXAMPLE OUTPUT:

#Make: Jeep
#Year: 2014

#Change    Speed
#    60       60
#    -5       55
#   -10       45
#     3       48