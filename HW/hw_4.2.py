                     #Task #2
from calendar import monthrange
from time import localtime

year = input("Input year:\n")
month = input("Input month:\n")
day = input("Input day:\n")

t = (year, month, day)
t_loc = localtime()
t_loc = (t_loc[0], t_loc[1], t_loc[2])

if (year > 0 and 1 <= month <= 12
    and (1 <= day <= monthrange(year,month)[1])):
    print("Date entered correctly!\n")
    if t == t_loc:
        print("The specified date is the same as the date on the PC")
else:
    print("Date entered incorrectly!")


