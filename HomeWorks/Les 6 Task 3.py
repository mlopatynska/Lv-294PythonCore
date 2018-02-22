x = [raw_input("Enter word") for i in xrange(5)]
def func_p(x,y):
    if sorted(x) == sorted(y):
        return True
    else:
        return False
for i in x:
    if func_p(x[0],i):
        print i