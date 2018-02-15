data = range(100,10000,7)
hash = {"min":10000, "max":100, "avg":0}
# hash = {"min": for i in data: if hash["min"]<=i }



min = data[-1]
max = data[0]
count = 0
sum = 0
# Method 1 "for if"
for i in data:
    count += 1
    sum += int(i)
    if min >= int(i):
        min = int(i)
    elif max <= int(i):
        max = int(i)
avg = sum/count

hash = {"min":min, "max":max, "avg": avg}

print "Sum of digits: {}".format(sum)
print "Minimum valuet: {}".format(min)
print "Maximum value: {}".format (max)
print "Average of input: {}".format(avg)
print hash
