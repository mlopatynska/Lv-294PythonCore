# name=input ("What is your name?"/n)
# name=raw_input("Hello, my name is Sviatoslav")
# print (name)
# print ("How old are you?")
# age=raw_input ("i am 25 years old")
# print (age)
# print("Where do you live?")
# live=raw_input("I live in Lviv")
# print (live)



name=input("What is your name?\n")
age=input("How old are you?\n")
live=input("Where do you live?\n")
salary=input("What is your salary?\n")
# print("{},{},{},2:.f{}".format("x\n","y\n","z\n","f\n"))
# ptint("My name is{}\n,I am{}\n,I live in{}\n,{}".format("sviatoslav","25years old","Lviv","12"))
print("{},{},{},{:.2}".format(name,age,live,salary))

