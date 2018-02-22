from random import randint
w, h = 5, 5;
Matrix1 = [[randint(10,150) for x in range(w)] for y in range(h)]
Matrix2=[[randint(10,150) for x in range(w)] for y in range(h)]
print(Matrix1)
print(Matrix2)

def max(n):
    for j in range (len(n)):
        for x in rangesplit(j):
            if n[x] < n[x+1]:
                return n[x + 1]


print(max(Matrix1), max(Matrix2))