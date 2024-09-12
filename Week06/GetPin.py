# Student name: Tan Jun Wei
# Student ID: S10266704C

correctpin = "12345"
first_attempt = input("Enter pin:")
attempt = first_attempt
wrong_tries = 0
max = 3

while attempt != correctpin:
    wrong_tries += 1
    if max-wrong_tries == 0:
        print("Invalid pin. You have no more tries.\n"
              "Your account is locked.")
        break

    print("Invalid pin. Please try again.\n"
          f"You have {max-wrong_tries} tries left.")
    
    attempt = input("Enter pin: ")

if attempt == correctpin:
    print("Correct pin entered.")