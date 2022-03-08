#txt file w/ radius of a circle, one per line (06.01 Radius.txt)

def diameter(rCircle):
    dCircle = rCircle * 2
    return dCircle
def circumference(rCicle):
    cCircle = rCircle * 3.14 * 2
    return cCircle
def area(rCircle):
    aCircle = rCircle * rCircle * 3.14
    return aCircle
#   open & read 06.01 Radius.txt file
#   calculate & print radius, diameter, circumference, and area on a line
#       each value is 15 characters wide, 5 decimal digits, space separating each column
#   print headings right-aligned w/ data
print("{:>15s} {:>15s} {:>15s} {:>15s}".format("Radius", "Diameter", "Circumference", "Area"))
fileTxt = open("06.01 Radius.txt")

rCircle = fileTxt.readline()
while rCircle != "":
    dataOut = rCircle
    print("{:15.5f} {:15.5f} {:15.5f} {:15.5f}".format(dataOut,diameter(dataOut),circumference(dataOut),area(dataOut)))
    rCircle = fileTxt.readline()
fileTxt.close()

#EXPECTED OUTPUT:

#         Radius        Diameter   Circumference            Area
#        1.60000         3.20000        10.05310         8.04248
#        2.93000         5.86000        18.40973        26.97026
#      200.99000       401.98000      1262.85741    126910.85591
#     1048.73200      2097.46400      6589.37749   3455245.51879
