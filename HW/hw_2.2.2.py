number = input("Input four-digit number:\n")

#Task - 2.a
number = str(number)

#The firs way, work for all integer number above zero.
sum_of_number = 0

sum_of_number += number.count("1") * 1
sum_of_number += number.count("2") * 2
sum_of_number += number.count("3") * 3
sum_of_number += number.count("4") * 4
sum_of_number += number.count("5") * 5
sum_of_number += number.count("6") * 6
sum_of_number += number.count("7") * 7
sum_of_number += number.count("8") * 8
sum_of_number += number.count("9") * 9

print("Sum of number.\nThe first way: {}".format(sum_of_number))

#Second way, only in four-digit integer number.
number = int(number)
sum_of_number = 0

sum_of_number += number % 10
sum_of_number += number // 10 % 10
sum_of_number += number // 100 % 10
sum_of_number += number // 1000 % 10

print("The second way: {}\n".format(sum_of_number))

#Test - 2.b

number = str(number)
print("Revers of number: {}\n".format((number[::-1])))

#Test - 2.c

print("Sorting the number: {}").format((sorted(number)))