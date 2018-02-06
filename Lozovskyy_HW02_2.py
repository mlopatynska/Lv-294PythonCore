x = input ("Введіть 4-значне число, будь ласка: ")
// приводимо число в текст
y = str(x)
// Пошук суми цифр числа
sum = int (y[0]) + int (y[1]) + int (y[2]) + int (y[3])
print ("Сума цифр цього числа складе: ")
print sum
// Пошук добутку цифр
mult = int (y[0]) * int (y[1]) * int (y[2]) * int (y[3])
print ("Result of multiplication: " + mult )
// Відображення в реверсному подярку
print y[::-1]

