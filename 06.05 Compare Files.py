#two txt files: compare them line by line & print differences
fileTxtA = open("06.05 CompareFileA.txt", "r")
fileTxtB = open("06.05 CompareFileB.txt", "r")
#program should perform the following:
#   open file "06.05 CompareFileA.txt" for reading
#   open file "06.05 CompareFileB.txt" for reading
#   read a line from both files
#       if line from both files is not the same, print line number & contents of both lines
aRead = fileTxtA.readline()
bRead = fileTxtB.readline()
lineNum = 1
diff = 0

while aRead != "" or bRead != "":
    aRead = aRead.rstrip()
    bRead = bRead.rstrip()
    if aRead != bRead:
        diff += 1
        print("Line: {} - File A: {}".format(lineNum, aRead))
        print()
        print("Line: {} - File B: {}".format(lineNum, bRead))
        print()
    aRead = fileTxtA.readline()
    bRead = fileTxtB.readline()
    lineNum += 1

#   print num of differences
fileTxtA.close()
fileTxtB.close()

print("{} Differences".format(diff))
