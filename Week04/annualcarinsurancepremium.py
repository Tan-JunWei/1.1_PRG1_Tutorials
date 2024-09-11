print("Car Insurance Calculator\n"
      "========================")
gender = input("Enter gender [M/F]: ")
age = int(input(("Enter age: ")))
traffic_accident = input("Have you been in a traffic accident before? [Y/N]")
base_annual_premium = 800

if gender == "M":
    if age < 25:
        base_annual_premium *= 1.8
    elif age <= 34:
        base_annual_premium *= 1.5
    elif age <= 44:
        base_annual_premium *= 1.2
    elif age <= 54:
        base_annual_premium *= 1.0
    elif age <= 64:
        base_annual_premium *= 1.4
    else:
        base_annual_premium *= 1.7

else:
    if age < 25:
        base_annual_premium *= 1.4
    elif age <= 34:
        base_annual_premium *= 1.3
    elif age <= 44:
        base_annual_premium *= 1.1
    elif age <= 54:
        base_annual_premium *= 0.9
    elif age <= 64:
        base_annual_premium *= 1.2
    else:
        base_annual_premium *= 1.4

if traffic_accident == "Y":
    base_annual_premium += 300

print(f"Your annual premium is: {base_annual_premium:.1f}")