#Izzy Ward      Final Project       IFSC 1202       05.02.22

#Simulate the operation of the turtle & create a computerized sketchpad
#create a 2D list "canvas" where each element is initialized into a single space
#   read commands from a file containing instructions for the shape
#       NOTE: first value of Cshape.txt is the value of the canvas
#   turtle should start at (0,0), direction up, pen up

#TURTLE COMMANDS:
#   1 = pen up
#   2 = pen down
#   3 = turn right
#   4 = turn left
#   5,# = move forward # spaces
#   6 = print canvas

#create object Sketch that holds value & actions for sketchpad
#   define attributes... 
#       size = size of square canvas (determined when obj is initialized)
#       xpos = current x position of turtle (default = 0)
#       ypos = current y position of turtle (default = 0)
#       direction = current direction of turtle (default = U)
#       pen = pen is up or down (default = U)
#       canvas = 2D list containing spaces or "*" (default = " ")
#   initialize methods... 
#       init (self, size)
#           sets attributes to values
#       printSketch (no arguments)
#           prints canvas line by line
#           HINT: print canvas from last line to zeroth line w/ 1-step (puts origin at bottom)
#           print current xpos, ypos, and direction under canvas
#       penUp (no arguments)
#           sets penUp to U
#       penDown (no arguments)
#           sets penDown to D
#       turnLeft (no arguments)
#           sets direction to new CCW direction (HINT: check current direction to determine new direction)
#       turnRight (no arguments)
#           sets direction to new CW direction (HINT: check current direction to determine new direction)
#       move (self, distance)
#           moves turtle from current xpos, ypos along current direction
#           if pen is D, put * along the path
#           HINT: different code snippet for each direction; if turtle reaches canvas border, stop

#EXPECTED OUTPUT:

#+--------------------+
#|                    |
#|                    |
#|                    |
#|                    |
#|     ***********    |
#|     *         *    |
#|     *  ********    |
#|     *  *           |
#|     *  *           |
#|     *  *           |
#|     *  *           |
#|     *  *           |
#|     *  *           |
#|     *  ********    |
#|     *         *    |
#|     ***********    |
#|                    |
#|                    |
#|                    |
#|                    |
#+--------------------+
#X = 16  Y = 5  Direction = U