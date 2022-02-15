#if an empty sequence is passed to range(), for block won't execute
#examples: range(-5) or range(7,3)
for i in range(-5):
    print("This won't be printed")
for k in range(8, 6):
    print('Nothing will be printed')
print("End of Loop")    #prints this line, skips prior
