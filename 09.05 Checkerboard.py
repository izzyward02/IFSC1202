#create program that creates a checkerboard pattern
#   prompt to size of board, minus frame (n)
n = int(input("Enter Size: "))
frame = "+" + " " + ("-" * n) + " " + "+"
#   create empty 2D array
def create_board(board):
    for b in range(len(board)):
        print(" ".join((str(c) for c in board[b])))

board = []
#   append top of the board w/ plus sign, n dashes, and plus sign
#   for n times, append interior rows, consisting of vertical bar, n spaces, and vertical bar
for b in range(n):
    board.append([0] * n)
    if b % 2:
        for i in range(n):
            if i % 2:
                board[b][i] = "*"
            else:
                board[b][i] = " "
    else:
        for i in range(n):
            if i % 2:
                board[b][i - 1] = "*"
            else:
                board[b][i - 1] = " "
else:
    print(frame)
    print(create_board(board))
    print(frame)
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