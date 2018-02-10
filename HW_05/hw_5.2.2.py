word = raw_input("Write you love to fruits:\n")
count_dict = {}

for i in word:
    if i not in count_dict:
        count_dict[i] = 0
    count_dict[i] +=1

print(count_dict)


