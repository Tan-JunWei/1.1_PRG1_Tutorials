# Tan Jun Wei
# S10266704C

colors_dict = {}
new_colors = {}
colors = []
color_name = []
list_of_names = []

with open("colors.csv","r") as file:
    for line in file:
        line = line.strip().split(",")
        colors_dict[line[0]] = line[1]

for key,value in colors_dict.items():
    if value in new_colors:
        new_colors[value].append(key)
    else:
        new_colors[value] = [key]

print(new_colors)