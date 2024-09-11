#Programming I

#####################################
#            Mission 2.2            #
#           Triangle Calculator     #
#####################################

#Background
#==========
#Tom has learnt that if he knows the length of the 3 sides of a triangle,
#he is able to calculate the area by using the Heron's formula (please check
#it out in internet if you cannot remember the formula).

#Requirements
#============
#Write a Python program to calculate the perimeter and area of a triangle
#whose length of the 3 sides are entered by the user. Display the results
#in a nicely formatted string, like the following:
#    For a triangle with sides 3.0, 4.0 and 5.0
#    The perimeter is 12.00
#    The area is 6.00
#Note: values shown above are just examples

#TYPE YOUR PYTHON CODE BELOW
#===========================

#Do you need to import any module?
import math

#Input
side1 = float(input("Please enter the length of side 1 of the triangle:"))
side2 = float(input("Please enter the length of side 2 of the triangle:"))
side3 = float(input("Please enter the length of side 3 of the triangle:"))

#Process
perimeter = side1 + side2 + side3
#Heron's formula
s = (perimeter/2)
area = math.sqrt(s * (s-side1) * (s-side2) * (s-side3))

#Output
print("For a triangle with sides {0:.1f}, {1:.1f} and {2:.1f}\n"
      "The perimeter is {3:.2f}\n"
      "The area is {4:.2f}".format(side1,side2,side3,perimeter,area))