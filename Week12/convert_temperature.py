# Tan Jun Wei
# S10266704C

def display_menu():
    '''
    displays the main menu as shown in the sample output below
    '''
    print("Temperature Conversion")
    print("[1]Fahrenheit to Celsius")
    print("[2]Celsius to Fahrenheit")
    print("[3]Exit")

def fahr_to_cel(f):
    '''
    receives the temperature in Fahrenheit as the parameter, calculates the Celsius equivalent and returns the value
    '''
    celsius = 5.0/ 9.0 * (f - 32) 

    return celsius

def cel_to_fahr(c):
    '''
    receives the temperature in Celsius as the parameter, calculates the Fahrenheit equivalent and returns the value
    '''
    Fahrenheit = 9.0/ 5.0 * c + 32

    return Fahrenheit  

def validate_input(option, lower, upper):
    '''
    receives 3 integer values as the parameter, checks whether option is within lower and upper, returns True if it is, False otherwise.
    '''
    if lower <= option <= upper:
        return True
    else:
        return False

while True:
    display_menu()
    option = int(input("Please enter your option: "))
    if validate_input(option,1,3):
        if option == 3:
            print("Thank you")
            break
        elif option == 1:
            f = int(input("Please enter the temperature in Fahrenheit:"))
            print(f"The temperature in celsius is {round(fahr_to_cel(f),1)} degrees")
        elif option == 2:
            c = int(input("Please enter the temperature in celsius: "))
            print(f"The temperature in fahrenheit is {round(cel_to_fahr(c),1)} degrees")
    else:
        print("Invalid option, please try again")

