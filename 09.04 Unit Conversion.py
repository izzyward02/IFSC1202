#create program that performs the following unit conversions:
#   prompt for float (FromValue)
#   prompt "Enter From Value: "
#   prompt for unit conversion (FromUnit)
#   prompt "Enter From Unit (mm, cm, m, km, in, yd, mi): "
#   prompt unit to convert to (ToUnit)
#   prompt "Enter To Unit (mm, cm, m, km, in, yd, mi): "
#   open "09.04 Conversion.txt" & read into two dimensional list
#       first row contains names of valid ToUnit
#       first column contains names of valid FromUnit
#   use FOR loop to search for match between entered FromUnit and first column
#       save index of row that match is found
#   if no match for FromUnit, print "FromUnit is not valid" & exit program
#   use FOR loop to search for match between entered ToUnit and first row
#       save index of column that match is found
#   if no match for ToUnit, print "ToUnit is not valid" & exit program
#   use index to get multiplier from 2D list
#       multiply it by FromValue, round 7 digits, display results

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