#Week 2 Activity 5: finding length of c(pythagoras theorem) and area of circle
#Name: Tan Jun Wei
#Student ID: S10266704C

import math
a = float(input("Enter the length of a:"))
b = float(input("Enter the length of b:"))
#By the converse of pythagoras' theorem, a^2 + b^2 = c^2
#Therefore c = square root of (a^2 + b^2)
c_squared = a**2 + b**2
c = math.sqrt(c_squared)
print(c)

#radius = diameter(c)/2
#area of circle = pi * (r^2)
pi = math.pi
radius = c/2
area_of_circle = pi * (radius**2)
print(area_of_circle)