number = input("Input four-digit number:")
number = int(number)
sum_of_number = 0
sum_of_number += number % 10
sum_of_number += number // 10 % 10
sum_of_number += number // 100 % 10
sum_of_number += number // 1000 % 10
print("Sum of numbers: {}".format(sum_of_number))
number = str(number)
print("Revers order: {}".format((number[::-1])))
print("Sorting: {}").format((sorted(number)))