unsortedlist = [76, 12, 34, 11, 89, 100, 3, 67, 14, 49, 25, 99, 100]
 
def bubblesort(list):
  sorted = False
  while not sorted:
    sorted = True
    for i in range(len(list)-1):
      if list[i] < list[i+1]:
        sorted = False
        list[i],list[i+1] = list[i+1],list[i]
  return list
 
print bubblesort(unsortedlist)
