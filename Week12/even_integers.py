# Tan Jun Wei
# S10266704C

import random

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

for i in range(5):
    number = random.randint(1,100)
    is_even(number)
    
    if is_even(number):
        print(f"{number} is even")
    else:
        print(f"{number} is odd")

