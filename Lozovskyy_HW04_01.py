# -*- coding: utf8 -*-
# Визначення чи є рік високосним
year = (int(input ("Будь ласка, введіть рік:\n")))
# Визначаємо чи ділиться значення на 4 без остачі
if (year % 4) != 0:
    print "{} This is not a leap year!".format(year)
# Визначаємо чи ділиться на 100 без остачі
elif (year % 100) == 0:
        # Визначаємо чи ділиться на 400
        if (year % 400) == 0:
            print "{} It's a leap year!".format(year)
        else:
            print "{} This is not a leap year!".format(year)
# За інших обставин, рік є високосним
else:
    print "{} It's a leap year!".format(year)
