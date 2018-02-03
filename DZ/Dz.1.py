name = raw_input("Your nsame?\n")
age = raw_input("Your age?\n")
address = raw_input("Where you stay?\n")
salary = input("Whats yours budget?\n")

print ('Hello, {}!\nYour age is {}.\nYou live in {}.\nYour salary {:.2f}'.format(name, age, address, salary))