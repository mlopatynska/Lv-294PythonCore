a = raw_input ("enter word")
a = list(a)
Dictionary = {i: a.count(i) for i in a};
print Dictionary