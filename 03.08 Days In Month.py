#input int 1-12 for a month
month = int(input("Enter Month: "))
#days in a month
list31s = [1,3,5,7,8,10,12]
list30s = [4,6,9,11]
#print num of days in month
#assume non-leap year
if month in list31s:
    print(31)
elif month in list30s:
    print(30)
else:
    print(28)