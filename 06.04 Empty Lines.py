#txt file w/ data & some lines are empty
iFileTxt = "06.04 EmptyLinesInput.txt"
oFileTxt = "06.04 EmptyLinesOutput.txt"
output = open(oFileTxt, "w")
#program should perform the following:
#   opens file "06.04 EmptyLinesInput.txt" for reading
#   opens file "06.04 EmptyLinesOutput.txt" for writing
#   reads a line from "06.04 EmptyLinesInput.txt" file
#       if line is not empty, write line to "06.04 EmptyLinesOutput.txt" file
#       if line is empty, do not write line to output file
read = 0
written = 0

with open(iFileTxt, "r") as f:
    for line in f:
        read += 1
        if line.strip():
            written += 1
            output.write(line)
output.close()
#   print num of lines read & num of lines written
print("{} Records Read".format(read))
print("{} Records Written".format(written))
