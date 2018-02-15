word=raw_input(" Enter a word ")
word=list(word)
dic={i:word.count(i) for i in word}
print dic 