# Student name: Tan Jun Wei
# Student ID: S10266704C

print(f"{"Name":13}{"Mark"}\n"
      f"{"----":13}{"----"}")
total = 0
with open("Marks.txt","r") as datafile:
    i = 0
    data = datafile.readlines()
    datalist = []
    while i < len(data):
        dataline = data[i].strip().split(";")
        datalist.append(dataline)

        datalist_2nd = int(datalist[i][1])
        total += datalist_2nd

        print(f"{datalist[i][0]:13}{datalist_2nd:.1f}")
        i += 1  
    average = total / len(datalist)
    print(f"\nAverage Mark: {average:.2f}")
