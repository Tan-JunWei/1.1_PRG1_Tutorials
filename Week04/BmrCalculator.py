#Student Name: Tan Jun Wei
#Student ID: S10266704C

path = r"removed"
file = open(path+"data.txt")
list = file.read().split(",")
weight = list[0]
height = list[1]
gender = list[2]
age = list[3]

#Formula to calculate BMR for woman:	10 * weight in kg + 6.25 * height in cm – 5 * age -161
BMR = 10 * float(weight) + 6.25 * float(height) * 100 - 5 * int(age) -161

print(f"Weight: {weight}kg\n"
      f"Height: {height}m\n"
      f"Age: {age}\n"
      f"Gender: {gender}\n"
      f"BMR: {BMR:.1f} kcal/day\n") #output is wrong. formula/test case given may be wrong