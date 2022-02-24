#steps to write a file line by line

#use open() statement & specify "w" for file writing
newfile = open("60.00.02 Demo Text.txt", "w")
#prepare output by concatenating data into single string
output = "The number is" + str(i)
#use .write() method to write file contents of string into a file
#   when writing an entire line of data, append a linefeed character to indicate end of data
demofile.write(output + "\n")
#close file as normal
demofile.close()

#FLOWING PROGRAM:
# Open the file for writing
newfile = open("06.00.00 OutputText.txt", "w")
# Output 10 numbers
for i in range(1,11):
# Note output does not contain a linefeed character,
# so we will have to add a linefeed when we write it it.
	output = "The number is " + str(i)
	newfile.write(output + "\n")
# Close the file
newfile.close()
print("File Created")
