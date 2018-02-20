y=int(input("year:\n"))
m=int(input("month:\n"))
d=int(input("day:\n"))

month={1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",
       7:"July",8:"August",9:"September",10:"October",11:"November",12:"December"}

if m>12:
    print("year has only 12 months")
elif d>32:
    print("month have less than 32 days")
else:
    print(d,month[m],y,"year")

