# -*- coding: utf-8 -*-
# # print ("What is your name?")
# # print "{},{}format".("Sviat","igor")
# # print ("How old are you?")
# # print ("i am 25 years old")
# # print (age)
# # print("Where do you live?")
#
#
# name=raw_input("What is your name?\n")
# age=raw_input("How old are you?\n")
# live=raw_input("Where do you live?\n")
# salary=input("what is your salary?\n")
# print "My name is{}\n,I am{}\n,i live in{}\n,My salary is{:.3f}".format(name,age,live,salary)

# f=len (raw_input("passwofld:"))
# if f < 25:
#     print( "ти доступаєшся до google com" )
# elif   len("passworld") >6:
#     print("sdasd")
# else:
#     print( "Exam was finished.")

# f=int(raw_input("Ведіть ціну"))
# if f > 100:
#     print (10*0.2)
# elif f > 50:
#         print (50*0.1)
# elif f > 10:
#     print (100*0.01)
# else:
#     print("ну і баран")

# f=str(raw_input("Погода"))
# if f == "Дощ":
#     print("Візьміть парасолю")
# elif f ==("Сніг"):
#     print("Візьміть снігоступи")
# else:
#     print("Нехай проблеми та незгоди не роблять вам в житті погоди")

# print len("Візьміть парасолю" if f == "Дощ" else "Нехай проблеми та незгоди не роблять вам в житті погоди")

# a = []
# if not a:
#   print("List is empty")

#
# keyword = "lambda"
# if keyword in ["and", "del", "from", "lambda"]:
#     print("{} is a keyword").format(keyword)



# r=range(50,61)
# if r in range:
#     print("sada")
# else:
#     print("asdasda")


# a =raw_input("напиши мені тут циферку ")
# if a < 0:
#     print "negative"
# elif a > 0:
#     print "positive"
# else:
#     print "zero"

# print len("напиши мені тут циферку" if a > 0 else "zero")





# k=int(input("day:"))
# day={1:"Mondey",2:"Tuesday",3:"Wednesday",4:"Thursday",5:"Friday",6:"Saturday",0:"Sunday"}
# if k>365:
#     print("exceeded days limit")
# else:
#     k=(k%7)
#     print(day[k])




# import calendar
# # y=int(input("year:\n"))
# m=int(input("month:\n"))
# d=int(input("day:\n"))
#
# month={1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",
#        7:"July",8:"August",9:"September",10:"October",11:"November",12:"December"}
#
# if m>12:
#     print("year has only 12 months")
# elif d>32:
#     print("month have less than 32 days")
# else:
#     print(d,month[m],y,"year")
#     print (calendar.monthrange(7,12)[1])




# start = 0
# finish = 10
# while start < finish:
#     print start
#     start += 0.2
# else:    print ("The end")




# for j in [0, 1, 2, 3, 4]:
#     print j
# else:
#     print j, "- is the last"

# x=list(raw_input{ 1:"banana", 2:"pineappel",3:"appel",4:"orange"})
# print (x)


# x=list(raw_input("I love banana, apple,  mango"))

# fruits=raw_input("What your favorite fruits?")
# food = []
# i=0
# d=0
# while i<5:
#     food.append(raw_input("enter your favorite food"))
#     i+=1
# for d in food:
#     d+=1
# print (i,"like",d)




# for d in range[0,10,2]:
#     print d

# for ftuits in range(len(fruits_1)):
#    print 'I like :', fruits_1
# print "Good bye!"


# fruits = ['banana', 'apple',  'mango']
# for fruit in fruits:
#    print 'I like :', fruit



# lst=[adasfafafasas]
# for i in range(len(lst)):
#     print i ,"=", str[i]

# for i in list:
#     print i

# str=[10,5,8,9]
# min=str[0]
# for el in str:
#     if min>el:
#         min=el
# print min


# str=[10,5,8,9]
# sum=0
# for el in str:
#    sum=sum+el
#    print sum



# str=[10,5,8,9]
# a=1
# i=0
# while i<len(str):
#     a=a*str[i]
#     i+=1
# print a



# lst=[2,4,54,6,7,67,54,5]
# for val in lst:
#     if val &2:
#         continue
#     print(val)
# print("The end")




#
# matrix[[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4]]
# i,j=0,0
# for row in matrix:
#     j=o
#     for col in row:



#
# x=("SpaceX, believes a fully, and, rapidly, reusable, rocket; is the pivotal, breakthrough needed")
# x1=x.split(" ")
# for j in x1:
#         print (x.replace(",",""))
#         break
# print("The end")


 # chr-sumvolu



# 2 variant
# for j in range(33,40):
#     x=x.replace(chr(j,""))
#     print (x)




# x=str("beeb")
# x.upper()
# x1=x[::-1]
# if x==x1:
#     print("good")
# else:
#     print("not good")


# pow2 = [2 ** x for x in range(10) if x > 5]




# pow2 = []
# for x in range(10):
#    pow2.append(2 ** x)
# print (pow2)



# analog kody za 1 riadok
# pow2 = [2 ** x for x in range(10)]
# print(pow2)


# odd = [x for x in range(20) if x % 2 == 1]
# print(odd)


# pow2 = [x ** 3 for x in range(40)if x%2==0]
# print(pow2)


# d = {'name': 'Vasyl', 'surname': 'Bilan', 'what is you english level': 'student',}
# for key in d:
#     print "student {} = {}".format(key, d[key])
    # for key, val in d.iteritems():
    #     print "{} = {} .".format(key, val)
    #     for key in d.iterkeys():
    #         print "student {} = {}".format(key, d[key])
    #         for val in d.itervalues():
    #             print "student {} = {}".format("?", val)

# for x in d:
#     print"{}={}".format(x,d[x])


# squares = {}
# for x in range(6):
#    squares[x] = x*x
# print squares [3]



# odd_squares = {x: x*x for x in range(11) if x%2 == 1}
# print(odd_squares)


# x=str(1234)
# dict={"even":0,"odd":0}
# for i in x:
#     if not int(i)%2:
#         dict["even"]+=1
#     else:
#         dict["odd"] += 1
# print dict
#
# def my_print():
#    pass
# print my_print()


# def my_print(name,surname):
#     return ("Hello! {} {}" .format(name,surname))
# my_print  ("Vasul","Petrov")
# my_print  ("ST ","RS")
# my_print  ("Vas","Pet")


# print sum.__doc__






# def my_print(name,surname,*score):
#     print ("Hello! {} {}," .format(name,surname))
#     print("Your score is:{}".format(sum(score))
# my_print ("Vasul","Petrov",1,1,1)
#
#     # print my_print("Vasul", a = 1, aa = 1, aaa = 1, )






# total = 0  # This is global variable.
#
# def my_sum(arg1, arg2):
#     total = arg1 + arg2  # Here total is local variable.
#     print "Inside the function local total : ", total
#     return total
# print my_sum(10, 20)
# print "Outside the function global total : ", total


#
# def calc_factorial (x):
#     if x == 1:
#         return 1
#     else:
#         return (x * calc_factorial(x-1))






