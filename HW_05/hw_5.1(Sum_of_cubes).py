# Sum of cubes
n = input("Enter prime number:\n")

sum_of_cubes = 0

for i in str(n):
    sum_of_cubes += pow(int(i),3)

print("Sum = {}".format(sum_of_cubes))