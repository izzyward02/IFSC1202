#prompt for a string
s = input("Enter a string: ")
#determine if string contains letter "f"
#   print index of second instance of letter "f"
#   if string contains "f" only once, print "One f"
if s.count("f") == 1:
    print("One f")
#   if string doesn't contain "f", print "Zero f"
elif s.count("f") < 1:
    print("Zero f")
else:
    f1 = s.find("f")
    print(s.find("f", f1 + 1))
