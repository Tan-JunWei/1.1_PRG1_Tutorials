# Tan Jun Wei (S10266704) - CSF02
import math

name_list = ["Sharon","Mic","Josh","Hannah","Hanzel"]
height_list = [172, 166, 187, 200, 166]
weight_list = [59.5, 65.6, 49.8, 64.2, 47.5]
size_list = ["M","L","S","M","S"]

bmi_list = []

print(f"{'Name':<10}{'Weight':<10}{'Height':<10}{'BMI':<10}{'Size':<10}")
for i in range(0,len(weight_list)):
    bmi = weight_list[i]/math.pow((height_list[i]/100),2)
    bmi_list.append(bmi)
    print(f"{name_list[i]:<10}{weight_list[i]:<10.2f}{height_list[i]:<10}{bmi_list[i]:<10.2f}{size_list[i]:<10}")


accuracy = 0
predicted_list = []

print(f"\n{'Name':<10}{'BMI':<10}{'Size':<10}{'Predicted':<10}")
      
for i in range(len(bmi_list)):
    if bmi_list[i] <= 18:
        prediction = "S"
    elif bmi_list[i] <= 21:
        prediction = "M"
    else:
        prediction = "L"
    predicted_list.append(prediction)
    
    if size_list[i] == predicted_list[i]:
        accuracy += 1
    print(f"{name_list[i]:<10}{bmi_list[i]:<10.2f}{size_list[i]:<10}{predicted_list[i]:<10}")

total_accuracy = (accuracy / len(predicted_list))*100

print(f"Accuracy rate is {total_accuracy:.2f}")

print(f"\n{'Name':<10}{'Weight':<10}{'Height':<10}{'BMI':<10}{'Gender':<10}{'Age':<10}{'BMR':<10}")
      
details_list = [['Sharon','F',33],['Mic','M',24],['Josh','M',25],['Hannah','F',30],['Hanzel','M',26]]
BMR_list = []

for student_info in details_list:
    #identify the index
    name = student_info[0]
    index = name_list.index(name)

    if student_info[1] == 'F':
        BMR = 655.1 + (9.6*weight_list[index]) + (1.8*height_list[index]) - (4.7*student_info[2])
    else:
        BMR = 66.47 + (13.7*weight_list[index]) + (5*height_list[index]) - (6.8*student_info[2])

    BMR_list.append(BMR)

for i in range(len(name_list)):
    print(f"{name_list[i]:<10}{weight_list[i]:<10.2f}{height_list[i]:<10}{bmi_list[i]:<10.2f}{details_list[i][1]:<10}{details_list[i][2]:<10}{BMR_list[i]:<10.2f}")
