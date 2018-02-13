a = 0
b = 1
num = int(input("Enter number: "))
while a in range (0,num+1):
    print "{}".format(a)
    a, b = b, a + b
else:
    print "that's all digints in range"
