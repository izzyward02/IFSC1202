#function "max()" accepts two nums & returns max of them
#   function is a part of Python syntax

def max(a, b):
    if a > b:
        return a
    else:
        return b

print(max(3, 5))
print(max(5, 3))
print(max(int(input("Enter First Number: ")), int(input("Enter Second Number: "))))
