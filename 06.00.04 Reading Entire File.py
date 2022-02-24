#before accessing a txt file, use open() statement
#   to open "06.00.02 Demo Text.txt", computer assumes the file is the root of the file system
#   if file is in a folder "IFSC1202", specify to open "IFSC1202/06.00.02 Demo Text.txt" 

#USING open() STATEMENT:
demofile = open("06.00.02 Demo Text.txt")

#^^this code is same as...
demofile = open("06.00.02 Demo Text.txt", "rt")
#   b/c "r"=read and "t"=text are default values, they do not need to be specified
#   ensure file name is correctly typed to avoid errors

#USING .read() METHOD:
x = demotextfile.read()
#   method is used to read entire file
#   lines of all contents (including linefeeds) are placed in a string
print(x)
#   file contents are displayed by simply printing it
#   when a linefeed w/i a file is printed, output is advanced to a new line
demotextfile.close()
#   using .close() method closes the file and releases all resources associated w/ file

#FLOWING PROGRAM:
# Open a file for reading
demotextfile = open("06.00.00 DemoText.txt", "r")
# Read the entire contents of the file into a single string
x = demotextfile.read()
# Print the contents - Note the embedded linefeeds
print(x)
# Close the file
demotextfile.close()