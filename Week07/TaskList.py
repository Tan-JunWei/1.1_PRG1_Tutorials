#Student Name: Tan Jun Wei
#Student ID: S10266704C

number_of_days = int(input("Enter number of days: "))
print("Day | Task(s)")

for days in range(1,number_of_days+1):
    print(f"{days:3} | ")

    if days % 7 == 0 and days != number_of_days:
        print("Day | Task(s)")