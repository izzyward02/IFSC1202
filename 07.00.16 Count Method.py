#count() method counts num of occurrences of one string within another string
#   simplest form: s.count(substring)
#   non-overlapping occurrences are taken into account
#if three parameters are specified: s.count(substring, left, right)
#   count is performed within slice s[left:right]

print('Abracadabra'.count('a'))   # this will print '4'
print(('aaaaaaaaaa').count('aa')) # and this will print '5'
print('A sailor went to sea to see what he could see, but all he could have see, was sea, sea, sea'.count('se', 25, -3))
