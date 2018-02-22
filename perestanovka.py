lis = ["ababa","ababa","abbab","aabbb","abbbb","aaaaa"]
def perestanovka(x,y):
    if len(x)!=len(y):
        return False
    if {x[i]:x.count(x[i])for i in range(len(x))}=={y[i]:y.count(y[i])for i in range(len(y))}:
        return True

for i in range(1,len(lis),1):
    print (('{}' if perestanovka(lis[0],lis[i])==True else 'No').format(lis[i]))