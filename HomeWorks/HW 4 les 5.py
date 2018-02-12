n = int(raw_input ("enter number \n"))
s = 0
for i in str(n):
    s += pow(int(i),3)
print("Sum of cubes of the number {} is {}".format(n, s))