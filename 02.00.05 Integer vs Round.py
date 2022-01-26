#cast float to int w/ int()
x = 12.455
print(round(x, 2))
#automatically rounds towards zero
print(int(1.3))		# gives 1
print(int(1.7))		# gives 1
print(int(-1.3))	# gives -1
print(int(-1.7))	# gives -1
#more convenient to use round()
print(round(1.3))	# gives 1
print(round(1.7))	# gives 2
print(round(-1.3))	# gives -1
print(round(-1.7))	# gives -2
#can specify num of digits past decimal point
print(round(12.455, 2))