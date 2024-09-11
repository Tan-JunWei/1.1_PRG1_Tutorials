#Student name: Tan Jun Wei
#Student ID: S10266704C
import math

a = float(input("Enter the length of a: "))
b = float(input("Enter the length of b: "))

def calculate_circle(a,b):
    radius = math.sqrt(a**2 + b**2) /2
    area = math.pi * radius **2
    
    print(f"The area of the circle is {area}")

calculate_circle(a,b)