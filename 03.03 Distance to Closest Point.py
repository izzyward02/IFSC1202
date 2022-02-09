#input three points on a line
pA = int(input("Enter Point A: "))
pB = int(input("Enter Point B: "))
pC = int(input("Enter Point C: "))
#find the distance between the points & print smallest
if (pB - pA) < (pC - pA):
    print(pB - pA)
else:
    print(pC - pA)