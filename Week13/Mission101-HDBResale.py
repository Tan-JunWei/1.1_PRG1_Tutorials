#Programming I

#########################
#      Mission 10.1     #
#   HDB Resale Prices   #   
#########################

#Background
#==========
#Tom is conducting some research into HDB resale prices as part of his part-time work for a real estate agency.
#Write a program to find out the following:
#
#a) The 2022 average price for the 4-room flat type (in 2 decimal places)
#b) The number of transactions above the average resale prices in part (a)
#c) The town with the highest resale price for the 5-room flat type in 2022
#
#Return the result of the three parts in a list of 3 items (e.g., [34535.35,20,'Hougang']

#Important Notes
#===============
#1) Comment out ALL input prompts before submitting.
#2) You MUST use the following variables
#   four_room_average, above_average, town_highest

#Set the filename
#Remove this statement when submitting in Coursemology

filename = "HDB-Resale-Price.csv"

#START CODING FROM HERE
#======================
#Create your function here
def ReadCSV(filename):
    total_data = []
    sum = 0
    counter = 0
    above_average = 0
    town_highest_price = 0

    with open(filename,"r") as file:
        for line in file:
            line_list = line.strip().split(",")
            total_data.append(line_list)

    #Part a
    for entry in total_data[1:]:
        if "2022" in entry[0] and entry[2] == "4-room":
            try:
                price = float(entry[3])
                sum += price
                counter += 1
            except ValueError:
                # Handle cases where the price is not a number
                continue

    four_room_average = round(sum / counter, 2)

    #Part b
    for list in total_data[1:]:
        try:
            price = float(list[3])
            if "2022" in list[0] and list[2] == "4-room" and price > four_room_average:
                above_average += 1
        except ValueError:
            continue

    #Part c
    for list in total_data[1:]:
        if "2022" in list[0] and list[2] == "5-room":
            try:
                price = float(list[3])
                if price > town_highest_price:
                    town_highest_price = price
                    town_highest = list[1]
            except ValueError:
                # Handle cases where the price is not a number
                continue
    return [four_room_average, above_average, town_highest]

    
#Statements to call the function, save result in variable result and print out
#to double-check your result returned from function
#Remove these statements when submitting in Coursemology
result = ReadCSV(filename)
print(result)

#output [566969.47, 29, 'QUEENSTOWN']




