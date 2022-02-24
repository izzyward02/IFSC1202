#NOTES for copying one file to another:
#   file names are strings; strings can be used in the program & can prompt user for file name
#   must open the output file for writing
#   when reading a line from input file, end of the string already has a linefeed; you don't have to append another linefeed in writing
#   be sure to close all open files

#PROGRAM THAT COPIES ONE FILE TO ANOTHER:

# The name of the file can be a string
inputfilename = "06.00.00 DemoText.txt"
outputfilename = "06.00.07 NewDemoText.txt"
recordcount = 0
# Open the input file for reading
inputfile = open(inputfilename, 'r')
# Open the output file for writing
outputfile = open(outputfilename, 'w')  
# Read the first line of the input file
line = inputfile.readline()
# Read until the input is empty
while line != '':
# Write to the output file
# Note that line already contains a linefeed character,
# so we don't have to add one when we write it.
     outputfile.write(line)
     recordcount += 1
# Read the next line of the input file
     line = inputfile.readline()
# End of File on input file
# Close both files
inputfile.close()
outputfile.close()
print("{} records written".format(recordcount))
