#replace() method replaces all occurrences of a given substring with another
#   syntax: s.replace(old, new)
#   takes string "s" and replaces occurrences of substring old with substring new
#can pass third argument count using replace()
#   syntax: s.replace(old, new, count)
#   if third argument is passed, only first count occurrences are replaced

print('a bar is a bar, essentially'.replace('bar', 'pub'))
print('a bar is a bar, essentially'.replace('bar', 'pub', 1))
