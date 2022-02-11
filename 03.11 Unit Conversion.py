#input float num (FromValue)
fromValue = float(input("Enter From Value: "))
unitList = ['ins', 'ft', 'yds', 'mi']
#input unit of float num (FromUnit)
fromUnit = str(input("Enter From Unit (ins, ft, yds, mi): "))
#input unit to convert float num to (ToUnit)
toUnit = str(input("Enter To Unit (ins, ft, yds, mi): "))
#if unit is valid, continue
#if not, print "ToUnit is not valid" & exit program
if fromUnit in unitList and toUnit in unitList:
    if fromUnit == unitList[0] and toUnit == unitList[1]:
        conv = fromValue * (1.0/12.0)
    elif fromUnit == unitList[0] and toUnit == unitList[2]:
        conv = fromValue * (1.0/36.0)
    elif fromUnit == unitList[0] and toUnit == unitList[3]:
        conv = fromValue * (1.0/63360.0)
    elif fromUnit == unitList[1] and toUnit == unitList[0]:
        conv = fromValue * 12.0
    elif fromUnit == unitList[1] and toUnit == unitList[2]:
        conv = fromValue * (1.0/3.0)
    elif fromUnit == unitList[1] and toUnit == unitList[3]:
        conv = fromValue * (1.0/5280.0)
    elif fromUnit == unitList[2] and toUnit == unitList[0]:
        conv = fromValue * 36.0
    elif fromUnit == unitList[2] and toUnit == unitList[1]:
        conv = fromValue * 3.0
    elif fromUnit == unitList[2] and toUnit == unitList[3]:
        conv = fromValue * (1.0/1760.0)
    elif fromUnit == unitList[3] and toUnit == unitList[0]:
        conv = fromValue * 63360.0
    elif fromUnit == unitList[3] and toUnit == unitList[1]:
        conv = fromValue * 5280.0
    elif fromUnit == unitList[3] and toUnit == unitList[2]:
        conv = fromValue * 1760.0
    else:
        conv = fromValue * 1.0      #if user enters same FromUnit and ToUnit, then multiplier is 1.0
else:
    print("From Unit is not valid.")
    quit("03.03.11 Unit Conversion.py")
#multiplier * FromValue = conv (use toValue and round to 7 digits)
toValue = round(conv, 7)
#display FromValue, FromUnit, ToValue, ToUnit
print("From Value: {}".format(fromValue))
print("From Unit: {}".format(fromUnit))
print("To Value: {}".format(toValue))
print("To Unit: {}".format(toUnit))