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
    print(f"{"Point A":^17}{"Point B":^17}{"Distance":^17}{"Midpoint":^17}{"Angle":^17}")
    print()
#   as each line reads, create two Point objs & reuse them with next datapoint
#   first two values are (x,y) for Point A and second two values are (x,y) for Point B
    for a in range(len(plot)):
        pA = Point(float(plot[a][0]), float(plot[a][1]))
        pB = Point(float(plot[a][2]), float(plot[a][3]))
#read each datapoint pair and display datapoint values, distance, midpoint, and XAngle
        print(f"{pA.ToString():17}{pB.ToString():17}{pA.Distance(pB):17.7f}{pA.MidPoint(pB):17}{pA.XAngle(pB):<17.7f}")
print()

#EXPECTED OUTPUT:

#            Point A              Point B             Distance             Midpoint                Angle
#     ---------------      ---------------      ---------------      ---------------      --------------- 
#          (0.0, 0.0)           (1.0, 1.0)            1.4142136           (0.5, 0.5)           45.0000000
#          (0.0, 0.0)           (4.0, 3.0)            5.0000000           (2.0, 1.5)           36.8698976
#        (-1.0, -1.0)           (3.0, 2.0)            5.0000000           (1.0, 0.5)           36.8698976
#          (0.0, 0.0)     (1.7320508, 1.0)            2.0000000     (0.8660254, 0.5)           30.0000001