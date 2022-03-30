#create program that creates a checkerboard pattern
#prompt for size of the board minus the frame
#create checkerboard with 2D array and print
#HINTS:
#   prompt to size of board (n)
#   create empty 2D array
#   append top of the board w/ plus sign, n dashes, and plus sign
#   for n times, append interior rows, consisting of vertical bar, n spaces, and vertical bar
#   append bottom of board, consisting of plus sign, n dashes, and plus sign
#   loop through interior rows and columns
#       set element to astrisk if column and row index are even/odd or odd/even
#   loop through entire board and print values

#EXAMPLE OUTPUT:

#Enter Size: 5
#+-----+
#| * * |
#|* * *|
#| * * |
#|* * *|
#| * * |
#+-----+

#Enter Size: 10
#+----------+
#| * * * * *|
#|* * * * * |
#| * * * * *|
#|* * * * * |
#| * * * * *|
#|* * * * * |
#| * * * * *|
#|* * * * * |
#| * * * * *|
#|* * * * * |
#+----------+