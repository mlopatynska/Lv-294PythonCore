a=[20,21,22,23,24,25,19,45,56,60]
b=[31,35,32,38,39,42,46,45,98,91]

def my_sort(n):
    for j in range (len(n)-1,0,-1):
        for x in range(j):
            if n[x] > n[x+1]:
                n[x] , n[x+1] = n[x+1] ,n[x]
    return n
print( my_sort(a), my_sort(b))
