def perestanovka(x,y):
    if sorted(x) == sorted(y):
        return True
    else:
        return False


x = [raw_input('Enter some word.') for i in range(5)]

print [i for i in x if perestanovka(x[0],i)]
