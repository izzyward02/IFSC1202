#create class Car w/ following attributes:
class Car():
#   year
#   make
#   speed
    def __init__(self, Year, Make, Speed = 0):
#constructor should accept car's make and year & speed should be set to zero
        self.Year = Year
        self.Make = Make
        self.Speed = Speed
#methods:
#   accelerate adds value to car's speed
    def Accelerate(self):
        zoom = Speed + 10
        return zoom
#   brake subtracts value from car's speed (don't go below zero)
    def Brake(self):
        slow = Speed - 10
        return slow
#first record in 10.03 Cars.txt file contains year and make
fileTxt = open("10.03 Cars.txt", "r")
fileRead = fileTxt.readline()
carElement = fileRead.split(",")
#   instantiate one car object w/ this data
car1 = Car(carElement[0], carElement[1])

fileRead = fileTxt.readline()
num = fileRead.split("\n")
speed = num[0]
#       if num is greater than zero, call Accelerate
if speed > 0:
    car1.zoom
    fileRead = fileTxt.readline()
#       if num is less than zero, call Brake
else:
    car1.slow
    fileRead = fileTxt.readline()
#print change of speed value and current speed
print("Make: {}" + "\n" + "Year: {}" + "\n\n".format(car1.Make, car1.Year))
#EXAMPLE OUTPUT:

#Make: Jeep
#Year: 2014

#Change    Speed
#    60       60
#    -5       55
#   -10       45
#     3       48