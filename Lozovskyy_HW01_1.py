answer = raw_input ("Hello, Could I ask you few questions?\n")
if answer == "yes":
    print "Question one:"
    name = raw_input ("What is your name?\n")
    age = raw_input ("How old are you?\n")
    city = raw_input ("Where are you live? (City)\n")
    salary = input ("What is your salary?\n")
    print "Check the information below, please:"
    print "Hello, {} !\nYour age in {}\nYou live in {}\nYour salary\
 in {:.2f}\n".format(name, age, city, salary)
    print "Thank you for your attention and cooperation!"
else:
print "Excuse me please..."