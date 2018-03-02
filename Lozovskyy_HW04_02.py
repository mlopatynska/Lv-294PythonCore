# -*- coding: utf8 -*-
# Отримуємо значення рік
year = (int(input ("Будь ласка, введіть рік:\n")))
# Визначаємо чи ділиться значення на 4 без остачі
if (year % 4) != 0:
    # leap = 0 - значить, що рік НЕ високосний
    leap = 0
# Визначаємо чи ділиться на 100 без остачі
elif (year % 100) == 0:
        # Визначаємо чи ділиться на 400
        if (year % 400) == 0:
            #  Рік є високосним
            leap = 1
        else:
            # Рік не є високосним
            leap = 0
# За інших обставин, рік є високосним
else:
    # Рік є високосним
    leap = 1

# Отримуємо значення "місяць"
month = (int(input ("Будь ласка, введіть номер місяця:\n")))
if month not in range(1,13):
    print "{} не може відповідати номеру місяця!".format (month)

# Отримуємо значення "день місяця"
day = (int(input("Будь ласка, введіть дату:\n")))

#  Перевірка: рік високосний, місяць лютий, день в діапазоні 1-29
if leap == 1 and month == 2 and day not in range (1,30):
        print "{} не може відповідати значенню дня {}-го місяця {} року".format(day, month, year)
#  Перевірка: рік НЕвисокосний, місяць лютий, день в діапазоні 1-28
elif leap == 0 and month == 2 and day not in range (1,29):
        print "{} не може відповідати значенню дня {}-го місяця {} року".format(day, month, year)
#  Перевірка: місяці з 31 днем і день в діапазоні 1-31
elif month in [1, 3, 5, 7, 8, 10, 12] and day not in range (1,32):
        print "{} не може відповідати значенню дня {}-го місяця {} року".format(day, month, year)
#  Перевірка: місяці з 30 днями і день в діапазоні 1-30
elif month in [4, 6, 9, 11] and day not in range(1, 31):
    print "{} не може відповідати значенню дня {}-го місяця {} року".format(day, month, year)
# Підтвердження та вивід коректної дати
else:
    print "Дякую! Дата {}/{}/{} р. є коректною.".format(day, month, year)