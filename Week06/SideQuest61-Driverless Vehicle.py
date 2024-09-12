#Programming I

###########################
#     Side Quest 6.1      #
#   Driverless Vehicle    #
###########################

#Background
#==========
#Tom decided to start his own company to create a driverless vehicle. He is programming
#the collision avoidance system of the vehicle. The vehicle uses sonar sensor to measure
#distance between objects. It measures distance by sending out a sound wave and listening
#for that sound wave to bounce back. By recording the round trip time (seconds) from the
#sound wave being generated, to the sound wave bouncing back, it is possible to calculate
#the distance between the vehicle and the object.

#Given that sound travels through the air at 344 m/s, write a Python program that will
#find the closest object to the vehicle and return a list containing the index and the
#distance of the object.
#1. Prompt the user to enter minimum 5 round trip times, each value separated by comma
#   (e.g. user should input in the format of 0.5, 2.1, 0.3, 1.8, 2.3)
#2. If the user enters lesser than 5 timings, the program should display an error and return
#   a list with the value [-1,-1]
#3. Calculate the distance and find the closest object.
#4. Print and return the index of the object in the user input, and the distance of this object.


#Important Notes
#===============
#1) Comment out ALL input prompts before submitting.
#2) You MUST use the following variables
#   - roundTrips
#   - closestObject



#START CODING FROM HERE
#======================


#Function to check closest object
def closest_object(roundTrips):
    #Perform the parsing of roundTrips input here
    roundTripsList = roundTrips.split(",")
    objects = []

    if len(roundTripsList) < 5:
        print("Error")
        closestObject = [-1,-1]
    
    else:
       i = 0
       while i < len(roundTripsList):
        distance = float(roundTripsList[i]) /2 * 344
        objects.append(distance)
        i += 1
    if len(objects) >= 5:
        closestObjectdist = min(objects)
        closestObjectindex = objects.index(closestObjectdist)
        closestObject = [closestObjectindex,closestObjectdist]


    return closestObject#Do not remove this line

#Prompt user to enter a minimum of 5 round trip times separated with commas
# roundTrips = input("no of round trips")

#Do not remove the next line that calls the function to get the result
result = closest_object(roundTrips)



#Modify to display the closest object


#input 0.5,2.1,0.3,1.8,2.3  output [2, 51.6]
#input 0.1,2.0,1.6,0.05     output [-1,-1]
#input 0.1,2.0,1.6,.5,1     output [0, 17.2]
