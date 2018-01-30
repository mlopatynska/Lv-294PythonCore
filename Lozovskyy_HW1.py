
answer = raw_input ("Hello, Could I ask you few questions?\n")
if answer == "yes":
    print ("Question one:")
    name = raw_input ("What is your name?\n")
    age = raw_input ("How old are you?\n")
    city = raw_input ("Where are you live? (City)\n")

    print ("Check the information please")
    print "Hello, " + name + "!"
    print "Your age in " + age + " years"
    print "You live in " + city
    print "Thank you for your attention and cooperation!"
else:
    print "Excuse me please..."
