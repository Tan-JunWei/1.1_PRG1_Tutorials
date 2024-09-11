# Tan Jun Wei (S10266704) – CSF02 
# Revision Test

# What is your desired loan amount? 10000
# What is your annual income? 24000
# What is the total value of your current loans? 20000
# What is the total of your savings? 20000
# How many years do you want to pay back this loan? 5

desired_loan_amount = int(input("What is your desired loan amount? "))
annual_income = int(input("What is your annual income? "))
current_loans = int(input("What is the total value of your current loans? "))
savings = int(input("What is the total of your savings? "))
years = int(input("How many years do you want to pay back this loan? "))

interest_rate = ((desired_loan_amount + current_loans) / (savings + annual_income * years)) * 100 
#use the formula but multiply by 100 to get the percentage

print(f"Your interest rate is {interest_rate:.1f}%")