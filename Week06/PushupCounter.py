# Student name: Tan Jun Wei
# Student ID: S10266704C

target = int(input("Enter target number of pushups: "))
day1 = int(input("Day 1: How many pushups did you do today>? "))
total = day1
i = 1

while not(total >= target):
    i += 1
    daytotal = int(input(f"Day {i}: How many push ups did you do today? "))
    total += daytotal

print(f"You did a total of {total} pushups.")
print(f"You hit your target in {i} days!")

