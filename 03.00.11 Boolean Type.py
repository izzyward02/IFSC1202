#booleans have two values: TRUE or FALSE
#Python treats 0=FALSE and 1=TRUE b/c binary rules
#bool() casts input data to TRUE or FALSE
print(bool(-10))    # True
print(bool(0))      # False - zero is the only false number
print(bool(10))     # True

print(bool(''))     # False - empty string is the only false string
print(bool('abc'))  # True