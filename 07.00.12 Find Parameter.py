#method is a function bound to an object
#   when a method is called, method is applied to object and does computations related to it
#   methods invoked as object_name.method_name(arguments)
#method find() takes a substring as argument & searches for it inside string
#   function returns index of first occurrence of a substring
#   if instance isn't found, method returns -1

s = 'Hello'
print(s.find('e'))   # 1
print(s.find('ll'))  # 2
print(s.find('L'))   # -1 (not found)
