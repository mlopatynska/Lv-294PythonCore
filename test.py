# def test_map(i):
#     return i**3
# def ifOdd(number):
#     return number%2 ==0
#
# winning_lottery_numbers = [0, 4, 3, 2, 3, 1]
#
# print winning_lottery_numbers
#
# fake_lottery_numbers = [2*n for n in winning_lottery_numbers]
#
# print fake_lottery_numbers
#
# fake_lottery_numbers_l = map(lambda n: 2*n, winning_lottery_numbers)
# print fake_lottery_numbers_l
#
# fake_lottery_numbers_2 = map(lambda n: (str(n)+"!"), winning_lottery_numbers)
# print fake_lottery_numbers_2
#
# cube_num = map (test_map, winning_lottery_numbers)
# print cube_num
#
#
# cube_num = map (ifOdd, winning_lottery_numbers)
# print cube_num
#
# print reduce(lambda x,y: str(x)+"+"+str(y), cube_num)
# print cube_num

# a = sum(x*x for x in range(1,10))
# print a
#
# g = [x*x for x in range(1,10)]
# print sum(g)

# def my_generator(text):
#     print("Inside my generator")
#     yield text
#     yield text+text
#     yield text+text
#
#
# for all in my_generator("Hello!"):
#     print all
#
#
# def rev_str(my_str):
#     length = len(my_str)
#     for i in range(length - 1,-1,-1):
#         yield my_str[i]
#
# for char in rev_str("hello"):
#      print(char)
#
#
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
# def divide(c,d):
#     return c/d
#
# print divide(5,4)

def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner

def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)

        print("%" * 30)
    return inner

@star
@percent
def printer(msg):
    print(msg)
printer("Hello")
