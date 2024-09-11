#Student Name: Tan Jun Wei
#Student ID: S10266704C

password = input("Enter password: ")

if len(password) < 8:
    print("Password must be at least 8 characters long.")

elif not any(char.isdigit() for char in password):
    # print(any(chr.isdigit() for chr in password))
    print("Password must contain at least one digit.")

elif not any(char.isupper() for char in password):
    print("Password must contain at least one uppercase letter.")
    
else:
    print("Password is valid.")
