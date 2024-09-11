#Student name: Tan Jun Wei
#Student ID: S10266704C

path = 'C:\\Users\Admin\Downloads\\'
file = open(path+'StudentData.txt', 'r')
file2 = file.read()
lines = []

file3 = file2.split("\n")
for i in file3:
    i = i.split(", ")
    lines.append(i)
# print(lines)

print(f"{'Name':<15}{'Mobile Contact':<10}\n"
      f"{lines[0][0]:<15}{lines[0][1]}\n"
      f"{lines[1][0]:<15}{lines[1][1]}")
