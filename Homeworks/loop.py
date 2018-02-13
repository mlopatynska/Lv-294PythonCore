#start = 0
#finish = 10
#while start < finish:
  #  print start
   # start +=1
#else:
  #  print 'the end'

#for j in [0, 1, 2, 3, 4]:
   # print j
#else:
 #   print j, "- is the last"


#food = []
#i = 0
#a = 0
#while i < 5:
   # food.append(raw_input("Please enter your favorite food \n"))
   # i += 1
#for el in food:
 #   a +=1
 #   print  a, "You like ", el

#lst = "45218441316541321"
#for el in range(0,10,2):
 #   print el
#for i in range(len(lst)):
#    print lst[i]
#i = 0
#while i < len(lst):
 #   i += 1
 #   print lst[i]

#lst = [1, 5, 2, 0, 10]
#min = lst[0]
#for el in lst:
 #    if min > el:
  #       min = el
#print min

#lst = [1, 5, 2, 0, 10]
#max = lst[0]
#for el in lst:
 #    if max < el:
  #       max = el
#print max

#lst = [1, 5, 2, 0, 10]
#sum = 0
#for i in lst:
#    sum = sum + i
#print sum

#lst = [1, 5, 2, 5, 10]
#a = 1
#i = 0
#while i < len(lst):
  #  a = a * lst[i]
  #  i+= 1
#print a


#lst = [1, 5, 2, 5, 10]
#for er in lst:
  #  if not er % 2:
  #      continue
 #   print er
#print("The end")

matrix = [[0,1,2,3,4], [0,1,2,3,4], [0,1,2,3,4], [0,1,2,3,4]]
i,j = 0, 0
for row in matrix:
    j = 0
    for col in row:
        print "[", i, ",", j, "]=", col
        j += 1
    i += 1
