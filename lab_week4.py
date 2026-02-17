total = 0

for _ in range(10):
    number = int(input("Enter a number: "))

    if number == 0:
        break

    if number < 0:
        continue

    total += number

print("Final sum:", total)

#################################
number = int(input("Enter a number: "))

for i in range(1, 13):
    result = number * i

    if result % 3 == 0:
        continue

    if result > 50:
        break

    print(number, "x", i, "=", result)
#######################################
import random

secret_number = random.randint(1, 20)
attempts = 0

while True:
    guess = int(input("Guess a number between 1 and 20: "))

    if guess < 1 or guess > 20:
        continue

    attempts += 1

    if guess == secret_number:
        print("Correct! Number of attempts:", attempts)
        break

#####################################################
n = int(input("Enter n: "))
count = 0

for i in range(1, n + 1):
    if i > 50:
        break

    if i % 8 == 0:
        continue

    if i % 4 == 0:
        count += 1

print("Count:", count)
#####################################################
for i in range(1, 6):
    for j in range(1, i + 1):

        if j == 3:
            continue

        if i + j > 6:
            break

        print(j, end=" ")

    print()
