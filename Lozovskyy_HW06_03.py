data = range(100,10000,7)
hash = {"min":data[-1], "max":data[0], "avg":(sum(data)/len(data))}
x = 100000
# hash ["min"] = (i for i in data if hash["min"]>i)

#Version 2
for i in data:
    if hash["min"]>i:
        hash["min"]=i
    elif hash["max"]<i:
        hash["max"]=i

#Version 1
# min = data[-1]
# max = data[0]
# count = 0
# sum = 0
# # Method 1 "for if"
# for i in data:
#     count += 1
#     sum += int(i)
#     if min >= int(i):
#         min = int(i)
#     elif max <= int(i):
#         max = int(i)
# avg = sum/count

# hash = {"min":min, "max":max, "avg": avg}

# print "Sum of digits: {}".format(sum)
# print "Minimum valuet: {}".format(min)
# print "Maximum value: {}".format (max)
# print "Average of input: {}".format(avg)
print "Hash info: {}".format(hash)
print "Minimum value is: {}\nMaximum value is: {}\nAverage value is: {}"\
    .format(hash["min"],hash["max"],hash["avg"])
