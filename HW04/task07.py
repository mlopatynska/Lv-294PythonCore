word = raw_input('Enter the word for counting letters:\n')
dict = {}
for i in word:
  dict[i] = word.count(i)
print ('Here\'s the result:\n')
print dict
