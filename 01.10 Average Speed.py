# input prompts
length = int(input("Enter Length of Race in Kilometers: "))
mins = int(input("Enter Minutes: "))
sec = int(input("Enter Seconds: "))
# avg mph [1.61 km in mi, 0.62 mi in km]
miles = length / 1.61
hours = (mins / 60) + (sec / 3600)
mph = miles / hours
print(mph)