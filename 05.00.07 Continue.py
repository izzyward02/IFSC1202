#another instruction that controls loop execution is 'continue' 
#   if Python meets 'continue' in the middle of loop iteration, it skips all remaining instructions
#   and proceeds to next iteration
for num in range(2, 10):
   if num % 2 == 0:
       print("Found an even number", num)
       continue
   print("Found an odd number", num)
