#ability to read and write files is one of the most powerful features of a computer
#main function for using files in Python is "open()" statement
#   open() takes two parameters: filename and mode
#       four modes for opening a file:
#           "r" = Read. Default value. Opens file for reading. Error if file doesn't exist
#           "a" = Append. Opens file for appending. Creates the file if doesn't exist. 
#           "w" = Write. Opens file for writing. Creates file if doesn't exist & overwrites all existing data. 
#           "x" = Create. Creates specified file. Returns error if file doesn't exist. 
#       user can specify if file should be handled as binary or text:
#           "t" = Text. Default value. File has letters & nums; each line terminated w/ linefeed
#           "b" = Binary. File has unprintable characters (e.g. images, videos, sound files)
