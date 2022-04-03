#txt file that has temps in Fahrenheit, one per line
fFileTxt = open("06.03 FTemps.txt", "r")
cFileTxt = open("06.03 CTemps.txt", "w")

count = 0
#program should perform the following:
#   opens file "06.03 FTemps.txt" for reading
#   opens file "06.03 CTemps.txt" for writing
#   defines function "FahrToCel"
#       accept a Fahrenheit temperature (float) as a parameter
#       calculate temperature in Celsius (C = (F - 32) * 5/9)
def FahrToCel(fTemp):
    cTemp = (fTemp - 32) * (5 / 9) 
    return cTemp
#   reads a line from "06.03 FTemps.txt"
#   calculates the Celsius temperature
for line in fFileTxt.readlines():
    temp = float(line.strip())
    cTemp = FahrToCel(temp)
    cFileTxt.write(f"{cTemp:.1f}\n")
    count += 1
#   writes Celsius temperature to "06.03 CTemps.txt"
#       Celsius values should be 5 characters wide w/ 1 decimal digit
#   prints number of records processed
print(count, " records written")

cFileTxt.close()
fFileTxt.close()
