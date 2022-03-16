#two txt files: compare them line by line & print differences
fileTxtA = open("06.05 CompareFileA.txt", "r")
fileTxtB = open("06.05 CompareFileB.txt", "w")
#program should perform the following:
#   open file "06.05 CompareFileA.txt" for reading
#   open file "06.05 CompareFileB.txt" for reading
#   read a line from both files
#       if line from both files is not the same, print line number & contents of both lines
aRead = fileTxtA.readline()
bRead = fileTxtB.readline()
lineNum = 1
diff = 0

while aRead != bRead:       #OVERALL WILL NOT RUN
    print("Line: {} - File A: {}".format(lineNum, aRead))
    print("Line: {} - File B: {}".format(lineNum, bRead))
    diff += 1
    lineNum += 1
    aRead = fileTxt.readline()
    bRead = fileTxt.readline()
else:
    lineNum += 1
    aRead = fileTxt.readline()
    bRead = fileTxt.readline()
#   print num of differences
fileTxtA.close()
fileTxtB.close()

print("{} Differences".format(diff))
#EXPECTED OUTPUT:

#Line: 4 - File A: jumpsx  

#Line: 4 - File B: jumps  

#Line: 6 - File A: over the lasy  

#Line: 6 - File B: over the lazy 

#2 differences