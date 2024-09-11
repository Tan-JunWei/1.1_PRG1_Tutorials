# BMI_BMR_Calculator.py (Activity 7 Week 2)
# This program calculates the body mass index and basal metabolic rate

#Name: Tan Jun Wei
#Student ID: S10266704C

# Calculate BMI
weight = float(input('Enter weight(kg): '))
height = float(input('Enter height(m): '))

bmi = weight / (height **2)

print('BMI: ', bmi)

# Calculate BMR
age = int(input('Enter age(years): '))

bmr_for_men =  10 * weight + 6.25 * (height*100) - 5 * age + 5
print('BMR: ', bmr_for_men)

