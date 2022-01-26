# input prompts
roomA = int(input("Enter Classroom A: "))
roomB = int(input("Enter Classroom B: "))
roomC = int(input("Enter Classroom C: "))
# find least number w/ two per desk
numFullDeskA = roomA // 2
numFullDeskB = roomB // 2
numFullDeskC = roomC // 2
# find remainders for extra desks
numExtraA = roomA % 2
numExtraB = roomB % 2
numExtraC = roomC % 2
# total desks needed
totalDesk = (numFullDeskA + numExtraA) + (numFullDeskB + numExtraB) + (numFullDeskC + numExtraC)
print(totalDesk)