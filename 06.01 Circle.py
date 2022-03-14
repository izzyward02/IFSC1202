#txt file w/ radius of a circle, one per line (06.01 Radius.txt)
fileTxt = open("06.01 Radius.txt")
x = fileTxt.readline()
print("{:>15s} {:>15s} {:>15s} {:>15s}".format("Radius", "Diameter", "Circumference", "Area"))

def radius(radius):
    x = fileTxt.readline()
    return x
def diameter(radius):
    diameter = x * 2
    return diameter
def circumference(radius):
    circumference = 2 * x * 3.14
    return circumference
def area(radius):
    area = 3.14 * x * x
    return area

while x != " ":
    x = float(x)
    diameter = x * 2
    circumference = 2 * 3.14 * x
    area = 3.14 * x * x
    print("{:15.5f} {:15.5f} {:15.5f} {:15.5f}".format(x, diameter, circumference, area))
    x = fileTxt.readline()

fileTxt.close()
#EXPECTED OUTPUT:

#         Radius        Diameter   Circumference            Area
#        1.60000         3.20000        10.05310         8.04248
#        2.93000         5.86000        18.40973        26.97026
#      200.99000       401.98000      1262.85741    126910.85591
#     1048.73200      2097.46400      6589.37749   3455245.51879
