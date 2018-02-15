input = [2,4,6,8,1,10]
output = 100
count = 0
sum = 0
# Method 1 "for if"
for i in input:
    count += 1
    sum += int(i)
    if output >= int(i):
        output = int(i)
avg = sum/count
print "Sum of digits: {}".format(sum)
print "Minimum value. Output: {}".format(output)
print "Average of input: {}".format(avg)

# Method 2 "min"
output = min(input)
print "Method min. Minimum value. Output: {}".format(output)

