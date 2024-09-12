# Tan Jun Wei
# S10266704C

mark_list = [['Mary', 90.5], ['Charles', 60.4], ['John', 70.5], ['Javier', 32.0], ['Luke', 46.7]]

def obtain_grade(mark):
    
    if mark >= 84.5:
        grade = "A+"
    elif mark >= 79.5:
        grade = "A"
    elif mark >= 75.5:
        grade = "B+"
    elif mark >= 69.5:
        grade = "B"
    elif mark >= 64.5:
        grade = "C+"
    elif mark >= 59.5:
        grade = "C"
    elif mark >= 54.5:
        grade = "D+"
    elif mark >= 49.5:
        grade = "D"
    else:
        grade = "F"

    return grade

print(f"{'Student Name':<15}{'Marks':<10}{'Grade':<10}")

for i in range(len(mark_list)):
    print(f"{mark_list[i][0]:<15}{mark_list[i][1]:<10}{obtain_grade(mark_list[i][1]):<10}")