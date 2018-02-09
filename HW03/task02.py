import datetime
day = input("Enter the day:\n")
month = input("Enter the month:\n")
year = input("Enter the year:\n")
isValidDate = True
try :
    datetime.datetime(int(year),int(month),int(day))
except ValueError :
    isValidDate = False
if(isValidDate) :
    print ("Input date is valid")
else :
    print ("Input date is not valid")