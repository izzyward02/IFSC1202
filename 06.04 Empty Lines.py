#txt file w/ data & some lines are empty
iFileTxt = open("06.04 EmptyLinesInput.txt", "r")
oFileTxt = open("06.04 EmptyLinesOutput.txt", "w")
#program should perform the following:
#   opens file "06.04 EmptyLinesInput.txt" for reading
#   opens file "06.04 EmptyLinesOutput.txt" for writing
#   reads a line from "06.04 EmptyLinesInput.txt" file
#       if line is not empty, write line to "06.04 EmptyLinesOutput.txt" file
#       if line is empty, do not write line to output file
iRead = iFileTxt.readline()
read = 0
written = 0

while iRead != " ":
    read += 1
    if iRead != "\n":
        oFileTxt.write(iRead)
        written += 1
    iRead = iFileTxt.readline()
#   print num of lines read & num of lines written
print("{} Records Read".format(r))
print("{} Records Written".format(w))

iFileTxt.close()
oFileTxt.close()
#EXPECTED OUTPUT:

#8 records read
#6 records written

#EXPECTED OVERWRITE TO "06.04 EmptyLinesOutput.txt":

#The quick
#brown fox
#jumps
#over the lazy
#dog's
#back