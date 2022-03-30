#create a program that calculates avg temp by city and displays result
#   don't hard code columns; use length of list or array to loop through values
#program should perform the following:
#   open "09.06 CityTemps.txt" for reading
#   create temps list containing city name and temp values
#   read input file
#   check for end of file (line is blank)
#   split input line into its parts
#   append input as a row in a 2D array (NOTE: first element is city name)
#   read next line
#   close input file
#   calculate avg temp for each location
#       loop through each row in temps
#           loop through each column in temps
#           add temp to a total
#           divide total by num columns -1 (since first column is city name)
#           append result to end of row in temps array (HINT: convert avg to int)
#   print results
#       create & display heading
#       loop through num rows in temps array
#           loop through num columns in temp and display data in array (city, temp data, and avg)

#EXAMPLE OUTPUT:

#City     Mo       Tu       We       Th       Fr       Sa       Su       Avg     
#Benton   65       68       67       65       69       70       71       67       
#Conway   68       73       67       69       71       73       73       70       
#Lonoke   67       72       70       71       73       74       75       71       