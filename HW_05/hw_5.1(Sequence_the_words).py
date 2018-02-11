# Sequence the words
while True:
    sentence = raw_input("Enter the sentence:\n")
    if sentence == '':
        print("Empty line, try again!")
    else:
        break

while True:
    seq = raw_input("Enter the word sequence:\n")
    if seq == '':
        print("Empty line, try again!")
    else:
        break

if seq in sentence:
    print("All words that begin with a '{}'".format(seq))
    for i in (sentence.split()):
        if seq == i[0:len(seq)]:
            print(i)
else:
    print("Not found.")