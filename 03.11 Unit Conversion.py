#input float num (FromValue)
fromValue = float(input("Enter From Value: "))
#input unit of float num (FromUnit)
fromUnit = str(input("Enter From Unit (in, ft, yd, mi): "))
#if unit is "in, ft, yd, mi" then continue

#if not, print "FromUnit is not valid" & exit program

#input unit to convert float num to (ToUnit)
toUnit = str(input("Enter To Unit (in, ft, yd, mi): "))
#if unit is valid, continue

#if not, print "ToUnit is not valid" & exit program

#use series of if statements to find value of multiplier (16 needed)

#if user enters same FromUnit and ToUnit, then multiplier is 1.0

#multiplier * FromValue = ToValue (use round and round to 7 digits)

#display FromValue, FromUnit, ToValue, ToUnit
