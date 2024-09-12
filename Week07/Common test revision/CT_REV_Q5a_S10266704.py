# Tan Jun Wei (S10266704) - CSF02

test_marks = []
with open("CT_marks.txt","r") as file:
    file.readline()
    for line in file:
        details = line.strip().split(";")
        test_marks.append(details)

averagelist = []

print(f"{'Name':<15}{'Test 1':<10}{'Test 2':<10}{'Test 3':<10}{'Average':<10}\n"
      f"{'----':<15}{'------':<10}{'------':<10}{'------':<10}{'-------':<10}")

i = 0
for student in test_marks:
    total = int(student[1]) + int(student[2]) + int(student[3])
    average = total / 3
    averagelist.append(average)
    print(f"{student[0]:<15}{student[1]:<10}{student[2]:<10}{student[3]:<10}{averagelist[i]:<10.2f}")
    i += 1
    
    
total_average = sum(averagelist) / len(averagelist)
print(f"\nAverage Mark: {total_average:.2f}")