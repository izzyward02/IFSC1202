# first heading
print("First Timestamp")
# h,m,s prompts
h1 = int(input("Enter Hours: "))
m1 = int(input("Enter Minutes: "))
s1 = int(input("Enter Seconds: "))
# total seconds
secH1 = h1**3600 #problem is here, but why?
secM1 = m1**60
secS1 = s1
totalSec1 = secH1 + secM1 + secS1
# second heading
print("Second Timestamp")
# h,m,s prompts
h2 = int(input("Enter Hours: "))
m2 = int(input("Enter Minutes: "))
s2 = int(input("Enter Seconds: "))
# total seconds again
secH2 = h2**3600 #why do I get a very unreasonable result?
secM2 = m2**60
secS2 = s2
totalSec2 = secH2 + secM2 + secS2
print(totalSec2 - totalSec1)