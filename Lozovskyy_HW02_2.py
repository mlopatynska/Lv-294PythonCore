# -*- coding: utf8 -*-
x = raw_input ("Введіть 4-значне число, будь ласка: ")
# Пошук суми цифр числа
y = str(x)
# Пошук добутку цифр числа
sum = int (y[0]) + int (y[1]) + int (y[2]) + int (y[3])
print "Сума цифр числа = {}".format(sum)
# Пошук добутку цифр числа
mult = int (y[0]) * int (y[1]) * int (y[2]) * int (y[3])
print "Result of multiplication: {}".format (mult)
# Відображення цифр числа в зворотньому порядку
print "Число у зворотньому порядку - {}".format(y[::-1])
# Сотрування цифр числа
print "Посортовані цифри числа -{}".format(''.join(sorted(y)))