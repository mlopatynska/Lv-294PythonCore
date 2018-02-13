x=int(input("Enter some number:"))
i,j=0,[]
for n in range(1000,9999+1):
    for m in str(n):
        i=i+int(m)
    if x==i:
        j.append(n)
    i=0
print (j)