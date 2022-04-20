#create class Student
#   define initializer & any default values (self, firstName, lastName, tNumber)
#   define object attributes for a student
#      firstName
#       lastName
#       tNumber
#       courseList = an empty list of courses
#   no methods for this class

#create class StudentList
#   define initializer & defaults (self)
#   define attributes for a student object
#       studentList = an empty list of Student objects
#   define methods of StudentList
#       create add_student (self, firstName, lastName, tNumber)
#           new student object using parameters
#           append new object to studentList
#       create find_student (self, "student to find")
#           loop through studentList
#           if tNumber = input parameter then return index in studentList
#       create print_student_list (self)
#           prints headings
#           loops through each student & prints name & tNumber
#           for each student, loops through courses registered
#       create add_student_from_file (self, "fileName")
#           reads file & appends to studentList
#           opens & reads 11.03 Students.txt
#           calls add_student w/ data to create student object & appends to studentList

#create class Course
#   define initializer & defaults (self, department, number, name, room, meetingTimes)
#   define attributes for a student object
#       department = 4 character abbreviation
#       number = 4 digit course number
#       name = proper string name for course
#       room = building & room number for course
#       meetingTimes = day & times for course
#   no methods for this class

#create class CourseList
#   define initializer & defaults (self)
#   define attributes for a student object
#       courseList = empty list of course objects
#   define methods of CourseList
#       create add_course (self, department, number, name, room, meetingTimes)
#           new course object using parameters
#           append new course object to courseList
#       create find_course (self, "department name", course number)
#           loop courseList for match; if department = input & number = input, return index in courseList
#       create add_course_from_file (self, "filename")
#           opens & reads 11.03 Courses.txt
#           calls add_course w/ data to create course object & append to courseList

#create empty CourseList object
#read 11.03 Courses.txt & append courseList object w/ add_course_from_file
#create empty StudentList object
#read 11.03 Students.txt & append studentList object w/ add_student_from_file
#open & read 11.03 Registration.txt
#   for department & course number, find index of course in courseList w/ find_course
#   create new course object w/ selected course data
#   for tNumber, find index of student in studentList w/ find_student
#   append new course object to courseList in selected student courseList w/ .append() 
#       HINT: mystudentList.StudentList[studentIndex].courseList.append(myCourse)
#print student registration w/ print_student_list



#EXPECTED OUTPUT:

#First Name    Last Name     T-Number      Course         Name                                              Room          Meeting Times
#Jim           Evans         T123456       
#                                          IFSC 1202      Introduction to Object-oriented Technology        EIT 212       M-W 11:00-12:00
#                                          IFSC 1310      Web Technologies                                  EIT 213       M-W 12:00-1:00
#                                          IFSC 2200      Ethics in the Profession                          EIT 214       M-W 1:00-2:00
#                                          IFSC 2300      Object-oriented Technology                        EIT 211       M-W 3:00-4:00
#                                          IFSC 3300      Web Client Applications                           EIT 211       T-T 1:00-2:00
#Joe           Smith         T654321       
#                                          IFSC 2305      Computer Systems                                  EIT 212       T-T 9:00-10:50
#                                          IFSC 2315      Information Systems Software                      EIT 213       T-T 11:00-12:00
#                                          IFSC 2340      Human Computer Interface                          EIT 214       T-T 12:00-1:00
#                                          IFSC 3300      Web Client Applications                           EIT 211       T-T 1:00-2:00
#                                          IFSC 3315      Applied Networking                                EIT 212       T-T 2:00-3:00
#Jane          Doe           T121212       
#                                          IFSC 3320      Database Concepts                                 EIT 213       T-T 3:00-4:00
#                                          IFSC 3342      Mobile Web Development                            EIT 211       M-W 11:00-12:00
#                                          IFSC 3360      System Analysis and Design                        EIT 212       M-W 12:00-1:00
#                                          IFSC 4325      Data Mining Concepts and Techniques               EIT 211       M-W 3:00-4:00
#                                          IFSC 4330      Database Security                                 EIT 212       T-T 9:00-10:50