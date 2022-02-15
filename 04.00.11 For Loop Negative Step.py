#to iterate over decreasing sequence, use extended form of range()
#extended form is 'range(start_value, end_value, step)' 
#when 'step' is omitted, step implicitly equals 1, but can be set to any non-zero num
#loop always includes 'start_value' and excludes 'end_value' during iteration
for i in range(10, 0, -2):
    print(i)
#prints 10 8 6 4 2 (excludes 0, but includes 10)
