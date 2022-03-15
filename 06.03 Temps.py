#txt file that has temps in Fahrenheit, one per line
fFileTxt = open("06.03 FTemps.txt", "r")
cFileTxt = open("06.03 CTemps.txt", "w")

fTemp = fFileTxt.readline()
count = 0
#program should perform the following:
#   opens file "06.03 FTemps.txt" for reading
#   opens file "06.03 CTemps.txt" for writing
#   defines function "FahrToCel"
#       accept a Fahrenheit temperature (float) as a parameter
#       calculate temperature in Celsius (C = (F - 32) * 5/9)
def FahrToCel(fTemp):
    fTemp = (fTemp - 32) * (5 / 9) 
    return fTemp
#   reads a line from "06.03 FTemps.txt"
#   calculates the Celsius temperature
while fTemp != " ":
    fTemp = (fTemp - 32) * (5 / 9)  #PROBLEM IS HERE: unsupported opperand type(s) 'str' and 'int'
    count += 1
    out = FahrToCel(fTemp)
    out = round(out, 1)
    out = str(out)
    cFileTxt.write(out + "\n")
    fTemp = fFileTxt.readline()
else:
    print("{}".format(count) + "Records Written:")
#   writes Celsius temperature to "06.03 CTemps.txt"
#       Celsius values should be 5 characters wide w/ 1 decimal digit
#   prints number of records processed
cFileTxt.close()
fFileTxt.close()

#EXPECTED OUTPUT:

# 4 records written

#EXPECTED OVERWRITE TO "06.03 CTemps.txt":
#28.4
#24.3
#-1.6
#-19.4