#create Python program that calculates running avg, semester avg, and letter grade for students based on variables
#create class Student
class Student():
#define initializer, accepting the following class values:
    def __init__(self, FName, LName, TNum, Scores):
        self.FName = FName
        self.LName = LName
        self.TNum = TNum
        self.Scores = Scores
#define methods for obj
#   RunAvg(self) = calculates running avg (non-blank) of score data
    def RunAvg(self):
        Scores = []
        for grade in self.Scores:
            if grade != "":
                Scores.append(int(grade))
            else:
                Scores.append(0)
        RunAvg = sum(Scores) / len(Scores)
        return RunAvg
#   TotalAvg(self) = calculates avg of scores, where missing scores are zero
    def TotalAvg(self):
        Scores = []
        for grade in self.Scores:
            if grade != "":
                Scores.append(int(grade))
        TotalAvg = sum(Scores) / len(Scores)
        return TotalAvg
#   LetterGrade(self) = returns letter grade based on TotalAvg, where... 
#       >=90 = A
#       >=80 and <90 = B
#       >=70 and <80 = C
#       >=60 and <70 = D
#       <60 = F
    def LetterGrade(self):
        avg = self.RunAvg()
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"
#as the program reads each line from StudentScores.txt, create ONE Student obj
#   reuse obj as the next student data is read
fileTxt = open("10.04 StudentScores.txt", "r")
studentList = []
for a in fileTxt:
    a = a.strip().split(",")
    students = Student(a[0], a[1], a[2], a[3:])
    studentList.append(students)
#NOTE: Jim E. has 3 scores, second is missing, Joe S. has 4 scores, Jane D. has 2 scores, first is missing
print("{:>10}{:>10}{:>15}{:>15}{:>15}{:>10}".format("First", "Last", "ID", "Running", "Semester", "Letter"))
print("{:>10}{:>10}{:>15}{:>15}{:>15}{:>10}".format("Name", "Name", "Number", "Average", "Average", "Grade"))
print()
for s in studentList:
    print("{:>10}{:>10}{:>15}{:>15.2f}{:>15.2f}{:>10}".format(s.FName, s.LName, s.TNum, s.TotalAvg(), s.RunAvg(), s.LetterGrade()))
print()

