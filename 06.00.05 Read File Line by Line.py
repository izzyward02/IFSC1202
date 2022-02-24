#most often advantageous to read file line by line

#use open() statement as normal
demofile = open("06.00.02 Demo Text.txt")

#USING .readline() METHOD:
x = demotextfile.readline()
#   this method is used to read each line of a file deliniated by a linefeed
#   single line of data (including the linefeed) is placed in a string

#CHECKING FOR END OF FILE (EOF):
#   while x != ""
#use this while statement to show when Python indicates an empty string & stop the reading
print(x)
#display file contents as normal
#   an extra blank line is created b\c there is a linefeed
#   AND print statement automatically generates new line
demotextfile.close()
#close file as normal

#FLOWING PROGRAM:
# Open a file for reading
demotextfile = open("06.00.00 DemoText.txt")
# Read the first line of the file
x = demotextfile.readline()
# End of file is indicated when the input is empty
while x != "":
# Print the contents - Note the embedded linefeeds
	print(x)
# Read the next line of the file
	x = demotextfile.readline()
# Close the file
demotextfile.close()
