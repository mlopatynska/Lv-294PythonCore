                     #Task #1
year = input("Input year:\n")

print ("It's a leap year!" if(not year % 4 and year % 100) or not year % 400 else "This is not a leap year!")


