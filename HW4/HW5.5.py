x=("""SpaceX believes a fully and rapidly reusable rocket is the pivotal breakthrough needed to substantially reduce the cost of space access.  The majority of the launch cost comes from building the rocket, which flies only once. Compare that to a commercial airliner – each new plane costs about the same as Falcon 9, but can fly multiple times per day, and conduct tens of thousands of flights over its lifetime. Following the commercial model, a rapidly reusable space launch vehicle could reduce the cost of traveling to space by a hundredfold.""")
x1=x.split(" ")
for j in x1:
    if j[0:1]=="S":
        print (j)
        continue
print("The end")
