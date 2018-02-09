k=int(input("day:"))
day={1:"Mondey",2:"Tuesday",3:"Wednesday",4:"Thursday",5:"Friday",6:"Saturday",7:"Sunday"}
if k>365:
    print("exceeded days limit")
else:
    k=(k%7)
    print(day[k])