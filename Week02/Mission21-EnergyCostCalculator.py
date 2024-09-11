#Programming I

###############################
#       Mission 2.1           #
#    Energy Cost Calculator   #
###############################

#Background
#==========
#Ever wonder the energy cost of running an appliance or electronic device?
#Here is a simple calculation to get that figure.

#Step 1:
#Monthly electricity consumption =
#   (Power rating [Watts] of device * Number of hours used per day)/1000

#Step 2:
#Cost = Monthly electricity consumption * Electricity tariff
#                                         ($0.2743 as of April 2023 for SP group)

#Laptop computers may peak at a maximum draw of only 60 watts,
#whereas common desktops may peak around 175 watts.

#Requirements
#============
#1) Write pseudocode for the Energy Cost Calculator.
#   The solution should prompt user for the power rating of a device and the
#   number of hours used per day. After which, display the calculated cost in
#   4 decimal places.
#2) Code the Python program base on the pseudocode that you have developed.

#Important Notes
#===============
#1) Include the pseudocode that you have developed as comments at the
#   beginning of the next section.
#2) You MUST (at least) use the following variables:
#   - power_rating
#   - hours

#TYPE YOUR PSEUDOCODE BELOW AS COMMENTS
#======================================

#Get input from the user for power rating of device, as well as the number of hours the device is used per day.
#calculate monthly electricity consumption
#calculate cost
#display calculated cost, ensure that it is in 4dp


#TYPE YOUR PYTHON CODE BELOW
#===========================

#Input
power_rating = int(input("Please enter the power rating of a device in watts:"))
hours = int(input("How many hours is it used per day?"))


#Process
monthly_electricity_consumption = (power_rating * hours) /1000 #use formula
cost = monthly_electricity_consumption * 0.2743

#Output
print(f"${cost:.4f}")

