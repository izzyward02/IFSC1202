#txt file that has temps in Fahrenheit, one per line

#program should perform the following:
#   opens file "06.03 FTemps.txt" for reading
#   opens file "06.03 CTemps.txt" for writing
#   defines function "FahrToCel"
#       accept a Fahrenheit temperature (float) as a parameter
#       calculate temperature in Celsius (C = (F - 32) * 5/9)
#   reads a line from "06.03 FTemps.txt"
#   calculates the Celsius temperature
#   writes Celsius temperature to "06.03 CTemps.txt"
#       Celsius values should be 5 characters wide w/ 1 decimal digit
#   prints number of records processed

#EXPECTED OUTPUT:

# 4 records written

#EXPECTED OVERWRITE TO "06.03 CTemps.txt":
#28.4
#24.3
#-1.6
#-19.4