#txt file w/ radius of a circle, one per line (06.01 Radius.txt)

#program should perform the following:
#   open & read 06.01 Radius.txt file
fileTxt = open("06.01 Radius.txt")
rCircle = fileTxt.read()
#   define function "diameter"
#       accept radius (float) as a parameter
#       calculate & return diameter of a circle (d = 2r)
def diameter(rCircle):
    dCircle = rCircle * 2
    return dCircle
#   define function "circumference"
#       accept radius (float) as a parameter
#       calculate & return circumference of circle (c = 2(pi)r)
def circumference(rCicle):
    cCircle = 2 * 3.14 * rCircle
    return cCircle
#   defines function "area"
#       accept radius (float) as a parameter
#       calculate & return area of circle (a = pi(r^2))
def area(rCircle):
    aCircle = (rCircle * rCircle) * 3.14
    return aCircle
#   calculate & print radius, diameter, circumference, and area on a line
#       each value is 15 characters wide, 5 decimal digits, space separating each column
#   print headings right-aligned w/ data
print("Radius:")

#EXPECTED OUTPUT:

#         Radius        Diameter   Circumference            Area
#        1.60000         3.20000        10.05310         8.04248
#        2.93000         5.86000        18.40973        26.97026
#      200.99000       401.98000      1262.85741    126910.85591
#     1048.73200      2097.46400      6589.37749   3455245.51879