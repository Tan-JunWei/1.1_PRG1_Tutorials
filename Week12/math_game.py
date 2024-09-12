# Tan Jun Wei
# S10266704C

import random

def menu():
    print("Math Game")
    print("[1]Addition")
    print("[2]Subtraction")
    print("[3]Multiplication")
    print("[4]Division")
    print("[5]Random")

def print_incorrect_msg():
    incorrect_msgs = ["No. Please try again.",
                      "Wrong. Try once more.",
                      "Don't give up!",
                      "No. Keep trying."]
    random_msg = incorrect_msgs[random.randint(0,3)]
    return random_msg

def print_correct_msg():
    correct_msgs = ["Very good!",
                      "Excellent!",
                      "Nice work!",
                      "Keep up the good work!"]
    random_msg = correct_msgs[random.randint(0,3)]
    return random_msg

def question(option):
    if option == 1:
        print(f"How much is {random_number1} + {random_number2}?")
        ans = int(input("Answer: "))
        if random_number1 + random_number2 == ans:
            print(print_correct_msg())
        else:
            print(print_incorrect_msg())
    
    elif option == 2:
        print(f"How much is {random_number1} - {random_number2}?")
        ans = int(input("Answer: "))
        if random_number1 - random_number2 == ans:
            print(print_correct_msg())
        else:
            print(print_incorrect_msg())

    elif option == 3:
        print(f"How much is {random_number1} * {random_number2}?")
        ans = int(input("Answer: "))
        if random_number1 * random_number2 == ans:
            print(print_correct_msg())
        else:
            print(print_incorrect_msg())

    elif option == 4:
        print(f"How much is {random_number1} / {random_number2}?")
        ans = float(input("Answer: "))
        if random_number1 / random_number2 == ans:
            print(print_correct_msg())
        else:
            print(print_incorrect_msg())

while True:
    menu()
    option = int(input("Enter option: "))

    random_number1 = random.randint(1,10)
    random_number2 = random.randint(1,10)
    
    if 1 <= option <= 4:
        question(option)

    elif option == 5:
        question(random.randint(1,4))

    else:
        print("Invalid option. ")


