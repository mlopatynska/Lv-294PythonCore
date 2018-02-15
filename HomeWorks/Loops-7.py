word=raw_input(" Enter a word ")
dic={}
word=list(word)
for i in word:
	if i in word:
		i+=1
print i 