# Multiples of ten - Ask the user for a number, and then report whether the number is a multiple of 10 or not.

num = input("Please give me a number and I can tell you if it is a multiple of 10: ")
num = int(num)

if num % 10 == 0:
    print(f"The number {num} is a multiple of 10")
else:
    print(f"This number is not a multiple of 10")
