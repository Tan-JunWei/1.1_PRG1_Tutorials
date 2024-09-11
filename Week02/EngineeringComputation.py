#Optional Activities in Week02 PRG1 tutorial
#Question 2: EngineeringComputation.py: calculation of volume of cylinder, surface area of sphere, and the force of
#gravity between 2 objects
#Name: Tan Jun Wei
#Student ID: S10266704C

import math
#user inputs
radius_of_cylinder = float(input("Enter the radius of the cylinder (in m) : "))
height_of_cylinder = float(input("Enter the height of the cylinder (in m) : "))
radius_of_sphere = float(input("Enter the radius of the sphere (in m) : "))
mass_of_object1 = float(input("Enter the mass of object 1 (in kg) : "))
mass_of_object2 = float(input("Enter the mass of object 2(in kg) : "))
distance = float(input("Enter the distance between the objects (in m) : "))

#calculate volume of cylinder using volume=πr^2 h
pi = math.pi
volume = pi * math.pow(radius_of_cylinder,2) * height_of_cylinder

#calculate surface area of sphere using surface area=4πr^2
surface_area = 4 * pi * math.pow(radius_of_sphere,2)

#calculate force of gravity 
G = 6.6743 * 10**-11
force = (G * mass_of_object1 * mass_of_object2)/(distance**2)


#display
print("Results:\n"
      f"Volume of the cylinder: {volume:.2f} cubic meters\n"
      f"Surface area of the sphere: {surface_area:.2f} square meters\n"
      f"Force of gravity between the objects: {force:.2e} Newtons")
