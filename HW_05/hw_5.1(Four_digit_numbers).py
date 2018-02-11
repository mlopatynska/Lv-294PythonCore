#Four-digit numbers
while True:
    num = input("Enter the number between 1 and 36:\n")
    if num > 36 or num < 1:
        print("Wrong number! Try again.")
    else:
       break

print("\nAll four-digit numbers:\n")
for i in range(1000,10000):
    i = str(i)
    x = int(i[0]) + int(i[1]) + int(i[2]) + int(i[3])
    if x == num:
        print(i)

