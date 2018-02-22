a = raw_input ("enter word \n")
a = list(a)
Dictionary = {i: a.count(i) for i in a}
print Dictionary