#Student Name: Tan Jun Wei
#Student ID: S10266704C

import random

num1 = random.randint(0,100)
num2 = random.randint(0,100)

correct = num1 + num2
check = int(input(f"Enter the sum of {num1} and {num2}: "))

if check == correct:
    print("Your answer is correct!")

else:
    print("Your answer is wrong\n"
          f"The correct answer is {correct}")