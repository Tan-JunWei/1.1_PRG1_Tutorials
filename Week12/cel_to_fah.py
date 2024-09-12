# Tan Jun Wei
# S10266704C

c = float(input("Enter the temperature in degree Celsius: "))  # consider possibility of float

def celsiuc_to_fahrenheit(c):
    f = (c * 9 / 5) + 32
    return f

print(f"The temperature is equivalent to {celsiuc_to_fahrenheit(c)} Fahrenheit.")
