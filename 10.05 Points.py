#use Cartesian coordinate system (x and y axes)
# each data point has and x- and y-value
#use the following code to create a datapoint obj... 
# Step 1 - Define the class object "Point"
class Point:
# Step 2 - Define the initializer and any default values
    def __init__(self, Xvalue, Yvalue):
# Step 3 - Define the object attributes
        self.x = Xvalue
        self.y = Yvalue
# Step 4 - Define the methods for the object
# ToString returns a nicely formated string to represent the data point
    def ToString(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"
#create following functions to make calcs about datapoints:
#   Distance: calcs distance between two points
#       has parameters Point A and Point B (both are Point objs)
#       returns distance as a float 
#       for points A and B, formula is sqrt((Xb - Xa)^2 + (Yb - Ya)^2)
#       NOTE: import sqrt function from math library
#   MidPoint: calcs midpoint between two datapoints
#       has parameters Point A and Point B (both are Point objs)
#       returns midpoint as a Point obj w/ midpoint values
#       for points A and B, formula is x = (Xb + Xa) / 2 & y = (Yb + Ya) / 2
#   XAngle: calcs angle of line between two datapoints
#       has parameters Point A and Point B (both are Point objs)
#       returns angle as a float (formatted in degrees)
#       for points A and B, formula is slope = (Yb - Ya) / (Xb - Xa) & XAngle = atan(slope) * 180 / pi
#       NOTE: import atan (arc tangent) function from math library  
#process each line of data in 10.05 Points.txt file
#   as each line reads, create two Point objs & reuse them with next datapoint
#   first two values are (x,y) for Point A and second two values are (x,y) for Point B
#read each datapoint pair and display datapoint values, distance, midpoint, and XAngle

#EXPECTED OUTPUT:

#            Point A              Point B             Distance             Midpoint                Angle
#     ---------------      ---------------      ---------------      ---------------      --------------- 
#          (0.0, 0.0)           (1.0, 1.0)            1.4142136           (0.5, 0.5)           45.0000000
#          (0.0, 0.0)           (4.0, 3.0)            5.0000000           (2.0, 1.5)           36.8698976
#        (-1.0, -1.0)           (3.0, 2.0)            5.0000000           (1.0, 0.5)           36.8698976
#          (0.0, 0.0)     (1.7320508, 1.0)            2.0000000     (0.8660254, 0.5)           30.0000001