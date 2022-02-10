#input int 1-12 for a month
month = int(input("Enter Month: "))
#print num of days in month
#assume non-leap year
if month == {1, 3, 5, 7, 8, 10, 12}:    #range isn't working...different format?
    print(31)
elif month == {4, 6, 9, 11}:    #range isn't working
    print(30)
else:
    print(28)
# NOT DONE