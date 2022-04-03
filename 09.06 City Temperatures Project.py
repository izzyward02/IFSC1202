#create a program that calculates avg temp by city and displays result
#   don't hard code columns; use length of list or array to loop through values
#program should perform the following:
#   open "09.06 CityTemps.txt" for reading
fileTxt = open("09.06 CityTemps.txt", "r")
#   create temps list containing city name and temp values
temps = []
#   read input file
#   check for end of file (line is blank)
while True:
    txtLine = fileTxt.readline()
    if not txtLine:
        break
#   split input line into its parts
    txtLine = txtLine.split()
    place = txtLine[0]
    temp = txtLine[1:]
#   append input as a row in a 2D array (NOTE: first element is city name)
    temps.append([place, temp])
#   read next line
txtLine = fileTxt.readline()
#   close input file
fileTxt.close()
#   calculate avg temp for each location
#       loop through each row in temps
#           loop through each column in temps
#           add temp to a total
#           divide total by num columns -1 (since first column is city name)
#           append result to end of row in temps array (HINT: convert avg to int)
for row in temps:
    totalRead = 0
    for b in range(len(row[1])):
        totalRead += int(row[1][b])
    avgTemp = totalRead // len(row[1])
    row[1].append(avgTemp)
#   print results
#       create & display heading
print("City\tMo\tTu\tWe\tTh\tFr\tSa\tSu\tAvg")
#       loop through num rows in temps array
for row in temps:
    print(row[0], end = "")
    for b in row[1]:
        print("\t{}".format(b), end = "")
    print()
#           loop through num columns in temp and display data in array (city, temp data, and avg)
