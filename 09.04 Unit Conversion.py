#create program that performs the following unit conversions:
#   prompt for float (FromValue)
fromValue = float(input("Enter From Value: "))
#   prompt for unit conversion (FromUnit)
fromUnit = input("Enter From Unit (mm, cm, m, km, in, yd, mi): ")
#   prompt unit to convert to (ToUnit)
toUnit = input("Enter To Unit (mm, cm, m, km, in, yd, mi): ")
#   open "09.04 Conversion.txt" & read into two dimensional list
convTxtFile = open("09.04 Conversion.txt", "r")
read = convTxtFile.readline()
convList = []
row = 0
col = 0
#       first row contains names of valid ToUnit
#       first column contains names of valid FromUnit
while read != "":
    split = read.split(" ")
    convList.append(split)
    read = convTxtFile.readline()
convTxtFile.close()
#   use FOR loop to search for match between entered FromUnit and first column
#       save index of row that match is found
for b in range(1, len(convList)):
    for c in range(1, len(convList[b])):
        if convList[b][0] == fromUnit:
            row = b
#   if no match for FromUnit, print "FromUnit is not valid" & exit program
if row == 0:
    print("FromUnit is not valid")
    exit()
#   use FOR loop to search for match between entered ToUnit and first row
#       save index of column that match is found
for b in range(1, len(convList)):
    for c in range(1, len(convList[b])):
        if convList[0][c] == toUnit:
            col = c
#   if no match for ToUnit, print "ToUnit is not valid" & exit program
if col == 0:
    print("ToUnit is not valid")
    exit()
#   use index to get multiplier from 2D list
#       multiply it by FromValue, round 7 digits, display results
toValue = fromValue * float(convList[b][c])
toValue = round(toValue, 7)

print("{} {} => {} {}".format(fromValue, fromUnit, toValue, toUnit))

#EXAMPLE OUTPUT:

#Enter From Value: 36
#Enter From Unit (mm, cm, m, km, in, yd, mi): in
#Enter To Unit (mm, cm, m, km, in, yd, mi): yd
#36.0 in => 1.0 yd

#Enter From Value: 10000
#Enter From Unit (mm, cm, m, km, in, yd, mi): ft
#Enter To Unit (mm, cm, m, km, in, yd, mi): mi
#10000.0 ft => 1.8939394 mi

#Enter From Value: 100
#Enter From Unit (mm, cm, m, km, in, yd, mi): yd
#Enter To Unit (mm, cm, m, km, in, yd, mi): ft
#100.0 yd => 300.0 ft

#Enter From Value: 250
#Enter From Unit (mm, cm, m, km, in, yd, mi): yd
#Enter To Unit (mm, cm, m, km, in, yd, mi): ft
#250.0 yd => 750.0 ft