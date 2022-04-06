#create Python program that calculates running avg, semester avg, and letter grade for students based on variables

#create class Student
#define initializer, accepting the following class values:
#   firstName (str)
#   lastName (str)
#   tNum (str)
#   scores (list of string scores) NOTE: this list is variable in length
#in initializer, create following obj attributes:
#   FirstName (str)
#   LastName (str)
#   TNumber (str)
#   Grades (list of str grades)
#define methods for obj
#   RunAvg(self) = calculates running avg (non-blank) of score data
#   TotalAvg(self) = calculates avg of scores, where missing scores are zero
#   LetterGrade(self) = returns letter grade based on TotalAvg, where... 
#       >=90 = A
#       >=80 and <90 = B
#       >=70 and <80 = C
#       >=60 and <70 = D
#       <60 = F
#as the program reads each line from StudentScores.txt, create ONE Student obj
#   reuse obj as the next student data is read
#NOTE: Jim E. has 3 scores, second is missing, Joe S. has 4 scores, Jane D. has 2 scores, first is missing

#EXAMPLE OUTPUT:

#      First         Last           ID      Running     Semester       Letter
#        Name         Name       Number      Average      Average        Grade
#------------ ------------ ------------ ------------ ------------ ------------
#         Jim        Evans      T123456        83.00        55.33            F 
#         Joe        Smith      T654321        88.00        88.00            B 
#        Jane          Doe      T121212        99.50        66.33            D