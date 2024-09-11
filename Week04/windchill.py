outside_temperature = float(input("Please enter the outside temperature in Fahrenheit:"))
wind_speed = float(input("Please enter the wind speed in miles per hour:"))

if not(-58 <= outside_temperature <= 41) or wind_speed < 2:
    print("Incorrect input")

wind_chill = 35.74 + 0.6215*outside_temperature - 35.75*(wind_speed**0.16) + 0.4275*outside_temperature*(wind_speed**0.16)
print(f"The wind-chill index is {wind_chill:.2f}")

