#create class Student
class Student():
#   define initializer & any default values (self, firstName, lastName, tNumber)
    def __init__(self, FName = "", LName = "", TNum = "", CourseList = []):
#   define object attributes for a student
#      firstName
#       lastName
#       tNumber
#       courseList = an empty list of courses
        self.FName = FName
        self.LName = LName
        self.TNum = TNum
        self.CourseList = CourseList
    def reg(self, course):
        self.CourseList.append(course)
#   no methods for this class
#create class StudentList
class StudentList():
#   define initializer & defaults (self)
    def __init__(self, sList = []):
#   define attributes for a student object
#       studentList = an empty list of Student objects
        self.sList = sList
#   define methods of StudentList
#       create add_student (self, firstName, lastName, tNumber)
    def add_student(self, Student):
#           new student object using parameters
#           append new object to studentList
        self.sList.append(Student)
#       create find_student (self, "student to find")
    def find_student(self, sFind):
#           loop through studentList
#           if tNumber = input parameter then return index in studentList
        for a in range(len(self.sList)):
            if self.sList[a].TNum == sFind:
                return a
        return -1
#       create print_student_list (self)
    def print_student_list(self):
#           prints headings
        print("{:<10}{:<10}{:^10}{:<12}{:<20}{:^10}{:^15}".format("First Name", "Last Name", "T-Number", "Course", "Name", "Room", "Meeting Times"))
#           loops through each student & prints name & tNumber
        for a in range(len(self.sList)):
            print("{:<10}{:<10}{:^10}".format(sList[a].FName, sList[a].LName, sList[a].TNum))
#           for each student, loops through courses registered
            for b in range(len(self.sList[a].CourseList)):
                print("{:10}{:10}{:20}{:10}{:10}".format(self.sList[a].CourseList[b].dept, self.sList[a].CourseList[b].num, self.sList[a].CourseList[b].name, self.sList[a].CourseList[b].room, self.sList[a].CourseList[b].times))
#       create add_student_from_file (self, "fileName")
    def add_student_from_file(self, fileTxt):
#           reads file & appends to studentList
#           opens & reads 11.03 Students.txt
        with open(fileTxt) as gData:
            genList = []
#           calls add_student w/ data to create student object & appends to studentList
            for g in gData:
                data = g.split(",")
                for a in range(len(data)):
                    data[a] = data[a].strip()
                genList.append(data)
            for a in range(len(genList)):
                newS = Student(genList[a][0], genList[a][1], genList[a][2])
                self.add_student(newS)
#create class Course
class Course():
#   define initializer & defaults (self, department, number, name, room, meetingTimes)
    def __init__(self, dept = "", num = "", name = "", room = "", meetingTimes = ""):
#   define attributes for a student object
#       department = 4 character abbreviation
#       number = 4 digit course number
#       name = proper string name for course
#       room = building & room number for course
#       meetingTimes = day & times for course
        self.dept = dept
        self.num = num
        self.name = name
        self.room = room
        self.meetingTimes = meetingTimes
#   no methods for this class
#create class CourseList
class CourseList():
#   define initializer & defaults (self)
    def __init__(self, CourseList = []):
#   define attributes for a student object
#       courseList = empty list of course objects
        self.CourseList = CourseList
#   define methods of CourseList
#       create add_course (self, department, number, name, room, meetingTimes)
    def add_course(self, Course):
#           new course object using parameters
#           append new course object to courseList
        self.CourseList.append(Course)
#       create find_course (self, "department name", course number)
    def find_course(self, dFind, numFind):
#           loop courseList for match; if department = input & number = input, return index in courseList
        for a in range(len(self.CourseList)):
            if self.CourseList[a].num == numFind and self.CourseList[a].dept == dFind:
                return a
        return -1
#       create add_course_from_file (self, "filename")
    def add_course_from_file(self, fileTxt):
#           opens & reads 11.03 Courses.txt
        with open(fileTxt) as gData:
            genList = []
#           calls add_course w/ data to create course object & append to courseList
            for g in gData:
                data = g.split(",")
                for a in range(len(data)):
                    data[a] = data[a].strip()
                genList.append(data)
            for a in range(len(genList)):
                newC = Course(genList[a][0], genList[a][1], genList[a][2], genList[a][3], genList[a][4])
                self.add_course(newC)
#create empty CourseList object
myCourses = CourseList()
#read 11.03 Courses.txt & append courseList object w/ add_course_from_file
myCourses.add_course_from_file("11.03 Courses.txt")
#create empty StudentList object
student1 = StudentList()
#read 11.03 Students.txt & append studentList object w/ add_student_from_file
student1.add_student_from_file("11.03 Students.txt")
#open & read 11.03 Registration.txt
with open("11.03 Registration.txt") as gData:
    genList = []
#   for department & course number, find index of course in courseList w/ find_course
#   create new course object w/ selected course data
    for g in gData:
        data = g.split(",")
        for a in range(len(data)):
            data[a] = data[a].strip()
        genList.append(data)
#   for tNumber, find index of student in studentList w/ find_student
#   append new course object to courseList in selected student courseList w/ .append() 
#       HINT: mystudentList.StudentList[studentIndex].courseList.append(myCourse)
    for a in range(len(genList)):
        if student1.find_course(CourseList[a][0]) != -1:
            if myCourses.find_course(genList[a][1], genList[a][2]):
                student1.sList[student1.find_student(genList[a][0])].reg(myCourses.CourseList[myCourses.find_course(genList[a][1], genList[a][2])])
#print student registration w/ print_student_list
    student1.print_student_list()
print()
