from random import randint
w, h = 5, 5;
Matrix1 = [[randint(10,150) for x in range(w)] for y in range(h)]
Matrix2=[[randint(10,150) for x in range(w)] for y in range(h)]
print(Matrix1)
print(Matrix2)

def max(n):
    for j in range (len(n)):
        for x in range(j):
            if n[x] < n[x+1]:
                return n[x + 1]


print(max(Matrix1), max(Matrix2))

# def maximum(mas):
#     a=[]
#     for x in mas:
#         a.append(mas(x))
#         a.append(x)
#         b=max(a)
#     return (b)
# d1=max(Matrix1)
# d2=max(Matrix2)
# fin=max([d1,d2])
# print(fin)
