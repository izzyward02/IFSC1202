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
