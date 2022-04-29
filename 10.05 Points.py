#use Cartesian coordinate system (x and y axes)
# each data point has and x- and y-value
#use the following code to create a datapoint obj... 
from math import sqrt, pi, atan
# Step 1 - Define the class object "Point"
class Point:
# Step 2 - Define the initializer and any default values
    def __init__(self, Xvalue, Yvalue):
# Step 3 - Define the object attributes
        self.x = Xvalue
        self.y = Yvalue
# Step 4 - Define the methods for the object
#   ToString returns a nicely formated string to represent the data point
    def ToString(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"
#create following functions to make calcs about datapoints:
#   Distance: calcs distance between two points
#       has parameters Point A and Point B (both are Point objs)
    def Distance(self, misc):
        Distance = sqrt((misc.x - self.x) ** 2 + (misc.y - self.y) ** 2)
#       returns distance as a float 
#       for points A and B, formula is sqrt((Xb - Xa)^2 + (Yb - Ya)^2)
#       NOTE: import sqrt function from math library
        return Distance
#   MidPoint: calcs midpoint between two datapoints
#       has parameters Point A and Point B (both are Point objs)
    def MidPoint(self, misc):
        MPX = (misc.x + self.x) / 2
        MPY = (misc.y + self.y) / 2
        MidPoint = f"({MPX}, {MPY})"
#       returns midpoint as a Point obj w/ midpoint values
#       for points A and B, formula is x = (Xb + Xa) / 2 & y = (Yb + Ya) / 2
        return MidPoint
#   XAngle: calcs angle of line between two datapoints
#       has parameters Point A and Point B (both are Point objs)
    def XAngle(self, misc):
        slope = (misc.y - self.y) / (misc.x - self.x)
        XAngle = atan(slope) * 180 / pi
#       returns angle as a float (formatted in degrees)
#       for points A and B, formula is slope = (Yb - Ya) / (Xb - Xa) & XAngle = atan(slope) * 180 / pi
#       NOTE: import atan (arc tangent) function from math library  
        return XAngle
#process each line of data in 10.05 Points.txt file
fileTxt = open("10.05 Points.txt", "r")
with fileTxt as data:
    plot = []
    for a in data:
        if a != "\n":
            r = a.split(",")
            plot.append(r)
    print(f'{"Point A":^20}{"Point B":^20}{"Distance":^20}{"Midpoint":^20}{"Angle":^20}')
    print()
#   as each line reads, create two Point objs & reuse them with next datapoint
#   first two values are (x,y) for Point A and second two values are (x,y) for Point B
    for a in range(len(plot)):
        pA = Point(float(plot[a][0]), float(plot[a][1]))
        pB = Point(float(plot[a][2]), float(plot[a][3]))
#read each datapoint pair and display datapoint values, distance, midpoint, and XAngle
        print(f'{pA.ToString():^20}{pB.ToString():^20}{pA.Distance(pB):>20}{pA.MidPoint(pB):>20}{pA.XAngle(pB):>20}')
print()
