#Programming I

###########################
#      Mission 10.1       #
#   Distance Based Fare   #   
###########################

#Background
#==========
#Distance-Based Fares (DBF) is a fare payment scheme currently used across public buses and MRT/LRT trains in Singapore.
#Fares are charged based on the total distance travelled (regardless if it is on a bus or train).
#The distance-based fare calculation is available in the distance-based-fare.csv file provided.
#Based on the route details of bus service 174 (bus_174.csv), write a program to meet the following requirements:

#a) Calculate the distance travelled based on the boarding and alighting bus stop
#b) Calculate the payable fare

#Return the result of the above answers in a list of two items (e.g., [29.0,1.90])

#Important Notes
#===============
#1) Comment out ALL input prompts before submitting.
#2) You MUST use the following variables
#   board, alight, distance, fare

board = input('Enter boarding busstop: ')
alight = input('Enter alighting busstop: ')

#board CODING FROM HERE
#======================

#Create your function here
def calculate_fare(board,alight):
    data = []
    fare = 0
    with open("distance-based-fare.csv","r") as file:
        file.readline()
        for line in file:
            line_list = [float(num) for num  in line.strip().split(",")]
            data.append(line_list)

    with open("bus_174.csv","r") as bus_file:
        bus_file.readline() 
        for line in bus_file:
            bus_line = line.strip().split(",")
            stop_km = float(bus_line[0])
            stop_id = int(bus_line[1])
            if stop_id == int(board):
                board_km = stop_km
            if stop_id == int(alight):
                alight_km = stop_km

    distance_travelled = alight_km - board_km

    for list_item in data:
        if list_item[0] >= distance_travelled:
            fare = list_item[1]/100
            break

    print(distance_travelled,fare)
    return [distance_travelled, fare]

    
#Statement to call the function and print the result
#Remove the statement when submitting in Coursemology 
calculate_fare(board,alight)
# print(calculate_fare(board, alight))

#input 22009,10499 output [29.0, 1.9]
#input 28169,42059 output [9.2, 1.29]
#input 42089,10041 output [16.9, 1.61]

