#Week 2 Activity 6: display table
#Name: Tan Jun Wei
#Student ID: S10266704C

import math 

def square(n):       #square function
    return math.pow(n,2)

def squareroot(n):   #sqrt function
    return math.sqrt(n)

numbers = [1,2,3,4,5]
english = ["One", "Two", "Three", "Four", "Five"]

number1 = numbers[0]
square1 = square(number1)
sqrt1 = squareroot(number1)
english1 = english[0]

number2 = numbers[1]
square2 = square(number2)
sqrt2 = squareroot(number2)
english2 = english[1]

number3 = numbers[2]
square3 = square(number3)
sqrt3 = squareroot(number3)
english3 = english[2]

number4 = numbers[3]
square4 = square(number4)
sqrt4 = squareroot(number4)
english4 = english[3]

number5 = numbers[4]
square5 = square(number5)
sqrt5 = squareroot(number5)
english5 = english[4]


print(f"{'Number':6} {'Square':5} {'Square root':10} {'English':7}")
print(f"{number1:>6} {square1:^4.0f} {sqrt1:^10.2f} {english1:>9}")
print(f"{number2:>6} {square2:^4.0f} {sqrt2:^10.2f} {english2:>9}")
print(f"{number3:>6} {square3:^4.0f} {sqrt3:^10.2f} {english3:>9}")
print(f"{number4:>6} {square4:^4.0f} {sqrt4:^10.2f} {english4:>9}")
print(f"{number5:>6} {square5:^4.0f} {sqrt5:^10.2f} {english5:>9}")
