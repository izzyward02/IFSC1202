#logical operators "and" & "or" check many conditions at once
n = int(input())
m = int(input())

if n % 2 == 0 and m % 2 == 0:
    print("Both Numbers are Even")
else:
    print("One of the Numbers is not Even")