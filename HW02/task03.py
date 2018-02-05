x = raw_input("Please enter the first value:\n")
y = raw_input("Please enter the second one:\n")
x,y = y,x
print("""First value, you've enterd was "{}" and "{}" was the second, right?""".format(x, y))