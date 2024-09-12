# Student name: Tan Jun Wei
# Student ID: S10266704C

import random

print("Welcome to Number Guessing Game")
num = random.randint(1,100)

i = 0
print(num)

while i < 5:
    trial = int(input(f"Try {i+1}: Enter a number between 1 and 100 (or -1 to end): "))
    if trial == -1:
        break
    i += 1

    if trial > num:
        print(f"{trial} is too high.")
    elif trial < num:
        print(f"{trial} is too low.")
    else:
        print("Bingo! you've got it right")
        break

print("\nBye-bye!")