#prompt for a string
s = input("Enter a string: ")
#determine if string contains letter "f"
#   if string contains one letter "f", print index
if s.count("f") == 0:
    print("{}".format(0))
#   if string contains more than one letter "f", print index of first and last occurrence
if s.count("f") == 1:
    f1 = s.find("f")
    print("{}".format(f1))
#   if string doesn't contain letter "f", print zero (0)
elif s.count("f") >= 2:
    f1 = s.find("f")
    fLast = s.rfind("f")
    print("{} {}".format(fLast, f1))
