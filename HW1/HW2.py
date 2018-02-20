a=float(input("Enter your first number:"))
b=float(input("Enter your second number:"))
operation=(input("operation"))
if operation=="+":
  print(a+b)
elif operation=="-":
  print(a-b)
elif operation=="*":
  print(a*b)
elif operation=="//":
 print(a//b)
elif operation=="%":
  print(a%b)
elif operation=="/":
    if(b)!=0:
        print(a/b)
    else:
        print("division by zero")
else:
 print("You have not typed a valid operator, please run the program again.")


