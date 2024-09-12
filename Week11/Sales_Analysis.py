# Name: Tan Jun Wei
# Student ID: S10266704C

file = input("Please enter the name of the data file: ")

months = []
sales = []

with open(file,"r") as data:
    first_line = data.readline()
    index_colon = first_line.index(":")
    for line in data:
        sum = 0
        new_line = line.strip()
        values = new_line.split(",")
        months.append(values[0])
        for n in values[1:]:
            sum += int(n)
        sales.append(sum)
    print("Branch Location:",f"{first_line[index_colon+1:]}",end="")
    print(f"{'Month':<15}{'Sales':>6}")
    for i in range(len(months)):
        print(f"{months[i]:<15}{sales[i]:>6}")