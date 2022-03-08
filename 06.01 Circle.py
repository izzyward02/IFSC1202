#txt file w/ radius of a circle, one per line (06.01 Radius.txt)
from math import pi

def radius(radius):
    radius = x
def diameter(radius):
    dCircle = rCircle * 2
    return dCircle
def circumference(radius):
    cCircle = 2 * radius * pi
    return cCircle
def area(radius):
    aCircle = pi * radius * radius
    return aCircle

fileTxt = open("06.01 Radius.txt")
rCircle = fileTxt.readline()
print("{:>15s} {:>15s} {:>15s} {:>15s}".format("Radius", "Diameter", "Circumference", "Area"))
while rCircle != "":
    rCirclefp = float(radius)
    print("{:15.5f} {:15.5f} {:15.5f} {:15.5f}".format(rCirclefp, diameter(rCirclefp), circumference(rCirclefp), area(rCirclefp)))
    radius = circlefile.readline()
fileTxt.close()
#   open & read 06.01 Radius.txt file
#   calculate & print radius, diameter, circumference, and area on a line
#       each value is 15 characters wide, 5 decimal digits, space separating each column
#   print headings right-aligned w/ data

#EXPECTED OUTPUT:

#         Radius        Diameter   Circumference            Area
#        1.60000         3.20000        10.05310         8.04248
#        2.93000         5.86000        18.40973        26.97026
#      200.99000       401.98000      1262.85741    126910.85591
#     1048.73200      2097.46400      6589.37749   3455245.51879
