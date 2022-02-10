#input four digit year
year = int(input("Enter Year: "))
#print LEAP YEAR or COMMON YEAR
#gregorian calendar rules: 
#leap year if exactly divisible by 4
#and not exactly divisible by 100
if year % 4 == 0:
    print("LEAP YEAR")
else:
    print("COMMON YEAR")