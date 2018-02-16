# #Task for removal of symbols and split of text to words
#
# text = 'Just a few words here, just for test. Right'
# for i in (',','.','!'):
#     text2 = text.replace(i, '')
#     text = text2
# words = text2.split()
# print words

# #Some stupid tests
#
# x = 'bullshit'
# x = list(x)
# x.reverse()
# x = ''.join(x)
# print x

# y = 'ololo'
# x = list(y)
# x.reverse()
# x = ''.join(x)
# print x == y

# #Creation of the list
#
# pow2 = []
# for x in range(10):
#    pow2.append(2 ** x)
# print pow2

# pow2 = [2 ** x for x in range(10)]
# print(pow2)

# pow2 = [2 ** x for x in range(10) if x > 5]
# print(pow2)

# I can't believe I did this shit by myself, motherfucker!
#
# even_cubes = [x ** 3 for x in range (40) if x % 2 == 0]
# print(even_cubes)

# #You will receive joined 4 elements:
# print [x+y for x in ['Python ','C '] for y in ['Language','Programming']]

# #To pizda.
#
# dict = {'name': 'Serhii','surname': 'Stepanchuk','age': 26,'englishlevel': 'Fluent'}
# for i in dict:
#     print i,'=', dict[i]

# #One that makes dict from simple loop:
#
# squares = {}
# for x in range(6):
#    squares[x] = x*x
# print squares

#Even and odd counter:

num = 12345678
dict = {'even': 0,'odd': 0}
for i in str(num):
    if int(i) % 2:
        dict['odd'] += 1
    else:
        dict['even'] += 1
print dict