                     #Task #2
year = input("Input year:\n")
month = input("Input month:\n")
day = input("Input day:\n")

print "Year entered correctly!" if year > 0 else "Year entered not  correctly!"
print "Month entered correctly!" if  1 <= month <= 12 else "Month  entered not correctly!"
print "Day entered correctly!" if 1 <= day <=31 else "Day  entered not correctly!"
