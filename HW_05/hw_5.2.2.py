import collections
word = raw_input("Write you love to fruits:\n")

def count_d(word):
    count_dict = {}
    for i in word:
        if i not in count_dict:
            count_dict[i] = 0
        count_dict[i] += 1
    print(count_dict)


count_d(word)

print(collections.Counter(word))

count_dict = {i:word.count(i) for i in word}
print(count_dict)
