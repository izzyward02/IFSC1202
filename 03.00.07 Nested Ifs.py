#can put an IF inside of an IF
x = int(input())
y = int(input())
if x > 0:
    if y > 0:
        #x>0, y>0
        print("Quadrant I")
    else:
        #x>0, y<=0
        print("Quadrant IV")
#can put an IF inside of an ELSE
else:
    if y > 0:
        #x<=0, y>0
        print("Quadrant II")
    else:
        #x<=0, y<=0
        print("Quadrant III")