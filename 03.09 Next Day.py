#input int 1-12 for a month
month = int(input("Enter Month: "))
#input int 1-31 for a day in a common year
day = int(input("Enter Day: "))
#print month and day & next day after it
#EXAMPLE: 3/31, then NEXT DAY is 4/1
list31s = [1,3,5,7,8,10,12]
list30s = [4,6,9,11]
feb = 2

if day <= 31 and month in list31s:
    if day == 31:
        mDate = month + 1
        dDate = 1
    else:
        mDate = month
        dDate = day + 1
elif day <= 30 and month in list30s:
    if day == 30:
        mDate = month + 1
        dDate = 1
    else:
        mDate = month
        dDate = day + 1
elif day <= 28 and month == feb:
    if day == 28:
        mDate = month + 1
        dDate = 1
    else:
        mDate = month
        dDate = day + 1
else:
    print("Input(s) Not Valid")

print("Next Day: {}/{}".format(mDate, dDate))