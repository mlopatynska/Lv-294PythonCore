input = 'apple'
output = {}
for i in input:
    output [i] = input.count(i)
print output
for key, count in output.items():
    print '{} : {}'.format(key, count)