winning_lottery_numbers = [8, 4, 3, 2, 3, 1, -3, -4]
# fake_lottery_numbers = map(lambda n: 2*n, winning_lottery_numbers)
#
# print fake_lottery_numbers
#
# int_to_str = map(lambda n: str(n) + '!' , winning_lottery_numbers)
#
# def cubelist(list):
#     newlist = [i ** 3 for i in list]
#     return newlist
#
# print cubelist(winning_lottery_numbers)
#
# def cube(n):
#     n = n ** 3
#     return n
#
# print map(cube,winning_lottery_numbers)
#
# print int_to_str

# def even(num): return num % 2 == 0
#
# print filter(even,winning_lottery_numbers)
# print map(even,winning_lottery_numbers)

# print reduce(lambda x,y: x*y, range(1,5))

# g = [x*x for x in range(1,10)]
# print sum(g)

# def my_generator(text):
#     print("Inside my generator")
#     yield text
#     yield len(text)
#     yield text * 4
#
# for i in my_generator('Crap! '):
#     print i
#
# def rev_str(my_str):
#     length = len(my_str)
#     for i in range(length - 1,-1,-1):
#         yield my_str[i]
#
# for char in rev_str("hello"):
#      print(char)


# def smart_divide(func):
#    def inner(a,b):
#       print("I am going to divide",a,"and",b)
#       if b == 0:
#          print("Whoops! cannot divide")
#          return
#
#       return func(a,b)
#    return inner
#
# @smart_divide
# def divide(a,b):
#     return a/b
#
# print divide(2,0)