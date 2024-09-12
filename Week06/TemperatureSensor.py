# Student name: Tan Jun Wei
# Student ID: S10266704C

with open("temperature.txt","r") as datafile:
    temperatures = datafile.readline()
    temperature_list = temperatures.split(",")
temperature_list = [float(temp) for temp in temperature_list]
#print(temperature_list)

total = 0
i = 0
while i < len(temperature_list):
    total += temperature_list[i]
    if temperature_list[i] > 29:
        print(f"{temperature_list[i]:.1f} ** higher than 29!!!")
    else:
        print(f"{temperature_list[i]:.1f}")
    i += 1

print(f"Number of readings: {i}\n"
      f"Average temperature: {total/i:.2f}")