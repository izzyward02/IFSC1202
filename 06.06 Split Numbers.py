#four txt files: display a count of nums in each

#program should perform the following:
#   opens "06.06 Numbers.txt" file for input containing ints, one per line
#   opens "06.06 EvenNumbers.txt" file for output that will contain even numbers
#   opens "06.06 OddNumbers.txt" file for output that will contain odd numbers
#   opens "06.06 PrimeNumbers.txt" file for output that will contain prime numbers
#   creates function "isEven"
#       accepts an int & returns True if even & False if odd
#   creates function "isOdd"
#       accepts an int & returns True if odd & False if even
#   creates function "isPrime"
#       accepts an int & returns True if prime & false if composite
#       prime nums are greater than 1
#   reads each line of "06.06 Numbers.txt" & converts to an int
#   uses "isEven" & writes even ints to "06.06 EvenNumbers.txt" (one int per line)
#   uses "isOdd" & writes odd ints to "06.06 OddNumbers.txt" (one int per line)
#   uses "isPrime" & writes prime ints to "06.06 PrimeNumbers.txt" (one int per line)
#   closes all files when finished
#   displays a count of nums in each txt file

#EXPECTED OUTPUT:

#54 even numbers
#45 odd numbers
#19 prime numbers
#99 numbers read

#EXPECTED OVERWRITE TO "06.06 EvenNumbers.txt" FILE:

262
886
472
940
306
854
876
324
454
410
546
412
414
366
996
264
194
52
434
130
244
370
648
266
996
538
692
810
784
80
598
844
986
606
736
966
104
790
776
42
152
94
974
126
110
512
190
904
70
414
876
740
938
212

#EXPECTED OVERWRITE TO "06.06 OddNumber.txt" FILE:

945
969
219
357
517
81
37
249
951
287
187
423
709
193
945
769
889
101
239
515
661
241
157
11
627
829
467
427
449
333
173
609
45
997
819
635
917
619
639
885
215
569
337
929
91

#EXPECTED OVERWRITE TO "06.06 PrimeNumbers.txt" FILE:

37
709
193
769
101
239
661
241
157
11
829
467
449
173
997
619
569
337
929