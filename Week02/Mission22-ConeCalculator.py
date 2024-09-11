#Programming I

#####################################
#            Mission 2.2            #
#           Cone Calculator         #
#####################################

#Background
#==========
#Tom has learnt that if he knows the radius of the base circle and height
#of a right circular cone, he is able to calculate the volume and the surface
#area of the cone (refer to the question in Coursemology for the formulae)

#Requirements
#============
#Write a Python program to calculate the volume and surface area (including
#the base circle) of a right circular cone whose base circle radius and height
#are entered by the user. Display the results in a nicely formatted string,
#like the following:
#    For a cone with base circle radius 3.0 and height 4.0:
#    Slant height is 5.00
#    Volume is 37.6991
#    Surface area (including base circle) is 75.3982
#Note: values shown above are just examples

#TYPE YOUR PYTHON CODE BELOW
#===========================

#Do you need to import any module?
import math

#Input
base_circle_radius = float(input("Please enter the base circle radius:"))
height = float(input("Please enter the height of the right circular cone:"))

#Process
slant_height = math.sqrt((math.pow(base_circle_radius,2) + math.pow(height,2)))
pi = math.pi
volume = (1/3) * pi * math.pow(base_circle_radius,2) * height
surface_area = (pi * (base_circle_radius**2)) + pi * base_circle_radius * slant_height

#Output
print("For a cone with base circle radius {0:.1f} and height {1:.1f}:\n"
      "Slant height is {2:.2f}\n"
      "Volume is {3:.4f}\n"
      "Surface area(including base circle) is {4:.4f}"
      .format(base_circle_radius,height,slant_height,volume,surface_area))

