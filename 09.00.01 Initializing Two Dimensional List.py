#suppose two nums are given: num of rows n and num of columns m
#   create a list size nxm filled w/ zeros
#   do this by appending a list w/ length m

n = 3
m = 4
a = []
for i in range(n):
    a.append([0] * m)
print(a)
